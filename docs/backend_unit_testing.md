# Guía de Unit Testing con pytest y FastAPI

Una guía completa sobre testing de APIs con pytest en FastAPI, enfocada en arquitecturas asincronizadas modernas. Los ejemplos están basados en los tests reales de [**Tabulae**](https://github.com/duquediazn/tabulae): FastAPI con AsyncSession, PostgreSQL, y autenticación JWT async.

## Índice

1. [¿Qué es un test y para qué sirve?](#1-qué-es-un-test-y-para-qué-sirve--volver-al-inicio)
2. [Conceptos clave de pytest](#2-conceptos-clave-de-pytest--volver-al-inicio)
3. [`AsyncClient` de FastAPI con httpx](#3-asyncclient-de-fastapi-con-httpx--volver-al-inicio)
4. [`dependency_overrides`](#4-dependency_overrides--volver-al-inicio)
5. [Fixtures encadenadas](#5-fixtures-encadenadas--volver-al-inicio)
6. [Aislamiento entre tests](#6-aislamiento-entre-tests--volver-al-inicio)
7. [Ejemplo completo y anotado](#7-ejemplo-completo-y-anotado--volver-al-inicio)
8. [Un test de ejemplo anotado](#8-un-test-de-ejemplo-anotado--volver-al-inicio)
9. [Variaciones comunes del setup según el proyecto](#9-variaciones-comunes-del-setup-según-el-proyecto--volver-al-inicio)
10. [Errores comunes y cómo reconocerlos](#10-errores-comunes-y-cómo-reconocerlos--volver-al-inicio)

---

## 1. ¿Qué es un test y para qué sirve? [🔝 Volver al inicio](#)

Un test es código que comprueba que otro código se comporta como debe.

En el contexto de una API, un test no suele mirar cómo está implementado internamente un endpoint, sino qué comportamiento expone hacia fuera. Por ejemplo:

- si `POST /products/` devuelve `201` cuando un admin crea un producto válido,
- si devuelve `403` cuando lo intenta un usuario sin permisos,
- si devuelve `422` cuando el body no cumple la validación,
- o si `GET /products/` devuelve la estructura paginada esperada.

Eso es importante porque el valor de una API está en su contrato observable: códigos HTTP, JSON de respuesta, validaciones, permisos y efectos sobre la base de datos.

### Qué verifica un test

Un test puede verificar una o varias de estas cosas:

- El código HTTP correcto.
- La forma del JSON de respuesta.
- El contenido concreto de la respuesta.
- Que se aplica una regla de negocio.
- Que un error se maneja como esperas.
- Que un cambio nuevo no rompe algo que ya funcionaba.

### Por qué merece la pena escribirlos

Porque te permiten:

- refactorizar sin ir a ciegas,
- detectar regresiones antes de producción,
- documentar el comportamiento real de la API,
- y reducir el número de bugs que aparecen por efectos secundarios o cambios aparentemente pequeños.

Una idea útil para empezar: un test no sirve para demostrar que el código existe. Sirve para demostrar que el comportamiento sigue siendo correcto.

---

## 2. Conceptos clave de pytest [🔝 Volver al inicio](#)

Pytest es el framework de testing. Su ventaja principal es que hace muy fácil preparar contexto, reutilizar setup y ejecutar pruebas sin mucho boilerplate.

### 2.1 Qué es una test function

Una test function es una función normal de Python cuyo nombre empieza por `test_`.

```python
@pytest.mark.asyncio
async def test_admin_can_create_product(client, session):
    ...
```

No hay una clase obligatoria, no hay que heredar de nada y no hay que registrar el test a mano.

### 2.2 Cómo pytest descubre los tests

Pytest busca automáticamente:

- archivos llamados `test_*.py` o `*_test.py`,
- funciones llamadas `test_*`,
- métodos de clases cuyo nombre también empiece por `test_`.

Por eso en este repositorio existen archivos como:

- `test_auth.py`
- `test_products.py`
- `test_users.py`
- `test_stock.py`

Cada archivo se centra en una parte de la API.

### 2.3 Qué es un fixture

Un fixture es una función especial que prepara algo que un test necesita: una sesión de base de datos, un cliente HTTP, datos base, un usuario autenticado, etc.

En este repositorio hay dos fixtures clave:

- `session`: abre una `AsyncSession` y limpia la base antes de cada test.
- `client`: crea el `AsyncClient` de httpx y hace que la app use esa misma sesión de test.

La gracia de los fixtures es que los pides por nombre como parámetro y pytest te los inyecta automáticamente.

```python
@pytest.mark.asyncio
async def test_admin_can_list_all_products(client, session):
    ...
```

Ese test no crea ni el `client` ni la `session` a mano. Pytest lo hace por ti.

### 2.4 Cómo funciona `yield` dentro de un fixture

Dentro de un fixture, `yield` separa el setup del teardown:

- lo que va antes de `yield` prepara el recurso,
- lo que se hace después de `yield` limpia el recurso.

Ejemplo simple:

```python
@pytest.fixture
def resource():
    obj = create_resource()
    yield obj
    cleanup(obj)
```

Ese patrón es especialmente útil cuando necesitas:

- abrir una sesión y cerrarla después,
- aplicar un `dependency_override` y quitarlo al final,
- crear un cliente HTTP y asegurarte de que se cierra bien.

### 2.5 Qué es el `scope` de un fixture

El `scope` define cada cuánto se ejecuta un fixture.

#### `scope="function"`

Se ejecuta una vez por cada test function.

Úsalo cuando el recurso debe estar aislado entre tests.

Ejemplos típicos:

- la sesión de base de datos de test,
- el cliente HTTP,
- datos temporales que no quieres compartir.

En este repositorio, `session` y `client` son de este tipo porque cada test debe empezar limpio.

#### `scope="module"`

Se ejecuta una vez por archivo de test.

Úsalo cuando varios tests de un mismo archivo pueden compartir un setup caro sin romper el aislamiento que necesitas.

Ejemplo típico:

- una carga de datos estática para todos los tests de un módulo,
- un recurso que tarda bastante en inicializar y no cambia entre tests.

#### `scope="session"`

Se ejecuta una vez para toda la ejecución de pytest.

Úsalo para inicialización global y pesada.

Ejemplo típico:

- crear tablas una sola vez,
- arrancar un contenedor externo,
- construir un engine global.

En este repositorio, `create_test_database` tiene `scope="session"` porque no tiene sentido crear el schema completo antes de cada test.

### Regla práctica sobre `scope`

- `function` da más aislamiento.
- `session` da más velocidad.
- La elección correcta depende de cuánto estado compartido puedes permitirte.

Cuando estás empezando, es más seguro pecar por demasiado aislamiento que por demasiado estado compartido.

---

## 3. `AsyncClient` de FastAPI con httpx [🔝 Volver al inicio](#)

Tabulae usa `httpx.AsyncClient` con `ASGITransport` para testear endpoints async de forma directa, sin levantar un servidor separado.

Ejemplo básico:

```python
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
```

### Qué resuelve

Te evita tener que:

- arrancar Uvicorn para ejecutar tests,
- gestionar URLs reales de red,
- depender de un proceso externo para hablar con la app,
- o mezclar código sync y async en el contexto de test.

La app corre dentro del mismo proceso del test, permitiendo tests rápidos y directos.

### `AsyncClient` con context manager (recomendado)

La forma preferible es usar context manager para respetar el lifespan de la aplicación:

```python
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

@pytest_asyncio.fixture
async def client(app):
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client
```

Esto garantiza que:

- los eventos de startup/shutdown se ejecutan correctamente,
- los recursos se inicializan y liberan al inicio/fin de cada test,
- y el comportamiento es coherente con producción.

### Ventajas del patrón async en tests

- Los tests pueden esperar de verdad (`await`), lo que refleja el comportamiento real.
- No hay bloqueos artificiales; la concurrencia funciona de forma natural.
- La sesión de BD y todas las dependencias pueden ser genuinamente asincronizadas.
- El código bajo test no necesita adaptaciones falsas para pasar tests.

---

## 4. `dependency_overrides` [🔝 Volver al inicio](#)

`dependency_overrides` es una de las herramientas más importantes para testear una app FastAPI con dependencias.

### Qué problema resuelve

En producción, tus endpoints dependen de funciones como:

- `get_db`
- `get_current_user`
- `require_admin`

Si dejas esas dependencias tal cual en tests, la app usará la base de datos real, la sesión real o el flujo completo real aunque no te interese.

En tests, normalmente quieres sustituir alguna dependencia por una versión controlada.

Eso es exactamente lo que hace `app.dependency_overrides`.

### Cómo se sustituye `get_db` con una sesión de test

En este repositorio, el patrón real es este:

```python
async def override_get_db():
    yield session


app.dependency_overrides[get_db] = override_get_db
```

Eso significa que cualquier endpoint que haga:

```python
db: AsyncSession = Depends(get_db)
```

recibirá la sesión del fixture de test, no la sesión normal de producción.

Este paso es clave porque hace que:

- el test escriba en la base de datos de test,
- el código del endpoint y el del test compartan la misma sesión,
- y puedas sembrar datos con `session.add(...)` antes de llamar a la API.

### Por qué es imprescindible limpiarlos después del test

Después de usar un override, hay que limpiarlo:

```python
app.dependency_overrides.clear()
```

Si no lo haces, el override se queda vivo para el siguiente test. Eso puede provocar:

- contaminación entre tests,
- resultados que dependen del orden de ejecución,
- falsos positivos,
- y bugs muy molestos de diagnosticar.

Este detalle parece pequeño, pero no lo es. Muchas suites de tests empiezan a volverse inestables precisamente porque alguien aplica un override y olvida quitarlo.

---

## 5. Fixtures encadenadas [🔝 Volver al inicio](#)

Una de las mejores partes de pytest es que un fixture puede depender de otro fixture, y pytest resuelve esa cadena automáticamente.

En este repositorio, el ejemplo más claro es:

- `client` depende de `session`.

Código simplificado:

```python
@pytest_asyncio.fixture
async def session():
    ...
    yield session


@pytest_asyncio.fixture
async def client(session):
    ...
    yield client
```

### Qué pasa internamente

Si un test declara:

```python
@pytest.mark.asyncio
async def test_something(client):
    ...
```

pytest razona así:

1. El test necesita `client`.
2. Para crear `client`, antes necesita `session`.
3. Ejecuta `session`.
4. Ejecuta `client` usando la `session` ya creada.
5. Ejecuta el test.
6. Hace el teardown de `client`.
7. Hace el teardown de `session`.

Tú no llamas a los fixtures manualmente. Ni decides el orden a mano. Pytest monta el grafo de dependencias por ti.

### Ventaja práctica

Este sistema te permite construir setups complejos sin meter todo en un solo fixture gigante.

Por ejemplo:

- `session`
- `client(session)`
- `active_user(session)`
- `admin_headers(client, session)`

Cada pieza hace una sola cosa y pytest las encadena.

Eso hace que los tests sean más legibles y que el setup se pueda reutilizar mejor.

---

## 6. Aislamiento entre tests [🔝 Volver al inicio](#)

Si una suite de tests toca base de datos y no aísla bien cada prueba, tarde o temprano se vuelve poco fiable.

### Por qué hay que limpiar la base de datos antes de cada test

Porque cada test debe empezar desde un estado conocido.

Si un test deja datos detrás, el siguiente puede:

- encontrar filas que no esperaba,
- fallar por duplicados,
- pasar por accidente,
- o fallar solo cuando se ejecuta junto con otros.

Eso rompe una regla básica del testing: cada test debe poder ejecutarse solo y seguir dando el mismo resultado.

### Cómo se hace en este repositorio

El fixture `session` borra las tablas antes de cada test usando `delete()` y siguiendo un orden seguro para las claves foráneas.

Patrón real:

```python
session.exec(delete(StockMoveLine))
session.exec(delete(StockMove))
session.exec(delete(Stock))
session.exec(delete(Product))
session.exec(delete(User))
session.exec(delete(Warehouse))
session.exec(delete(ProductCategory))
session.exec(delete(RevokedToken))
session.commit()
```

### Por qué importa el orden FK-safe

No puedes borrar primero una fila padre si siguen existiendo filas hijas que la referencian.

Por eso el borrado se hace de más dependiente a menos dependiente:

- primero `StockMoveLine`,
- luego `StockMove`,
- luego `Stock`,
- etc.

Si cambias el modelo de datos y añades tablas nuevas, ese orden puede tener que actualizarse.

### Por qué las pruebas no deben depender del orden de ejecución

Porque pytest puede ejecutar un archivo solo, un test solo, varios archivos o toda la suite. Incluso en algunos proyectos se ejecutan en paralelo.

Si un test solo pasa porque antes se ejecutó otro que le deja datos preparados, en realidad ese test está roto.

Un test sano:

- prepara sus propios datos,
- hace su comprobación,
- y no asume nada sobre lo que ocurrió antes.

### Nota práctica sobre secuencias de base de datos

Un detalle importante: `DELETE` borra filas, pero no necesariamente reinicia secuencias o contadores autoincrementales.

Eso significa que el primer registro de un test puede no tener `id == 1`, aunque la tabla esté vacía.

Por eso casi nunca conviene afirmar cosas como:

```python
assert response.json()["id"] == 1
```

Es mejor comprobar que el `id` existe o que coincide con un objeto que acabas de crear.

---

## 7. Ejemplo completo y anotado [🔝 Volver al inicio](#)

Debajo tienes un `conftest.py` realista para Tabulae:

- PostgreSQL de test en Docker,
- `AsyncSession` con `asyncpg`,
- creación de tablas una sola vez por sesión,
- limpieza por test,
- `AsyncClient` con context manager,
- y `dependency_overrides` para compartir la misma sesión entre app y test.

El objetivo aquí es didáctico: cada línea está explicada.

```python
import asyncio  # Se usa para ejecutar la creación inicial de tablas una vez por sesión.
import pytest  # Pytest define fixtures sync y gestiona su ciclo de vida.
import pytest_asyncio  # Extensión para fixtures async.
from httpx import ASGITransport, AsyncClient  # Cliente HTTP async para tests.
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine  # SQLAlchemy async.
from sqlalchemy.pool import NullPool  # Evita reutilizar conexiones entre tests.
from sqlmodel import SQLModel, delete  # Metadata y borrado de filas.

from app.main import app  # La instancia FastAPI que vamos a testear.
from app.models.database import get_db  # Dependencia real que entrega la sesión de producción.
from app.models.product import Product
from app.models.product_category import ProductCategory
from app.models.revoked_token import RevokedToken
from app.models.stock import Stock
from app.models.stock_move import StockMove
from app.models.stock_move_line import StockMoveLine
from app.models.user import User
from app.models.warehouse import Warehouse

TEST_DATABASE_URL = "postgresql+asyncpg://test_user:test_pass@db_test:5432/test_db"
engine = create_async_engine(TEST_DATABASE_URL, echo=True, poolclass=NullPool)
TestAsyncSession = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    """Crea las tablas una sola vez al arrancar la suite."""

    async def _create():
        tmp_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
        async with tmp_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        await tmp_engine.dispose()

    asyncio.run(_create())


@pytest_asyncio.fixture()
async def session():
    """Entrega una AsyncSession limpia por test."""
    async with TestAsyncSession() as session:
        await session.execute(delete(StockMoveLine))
        await session.execute(delete(StockMove))
        await session.execute(delete(Stock))
        await session.execute(delete(Product))
        await session.execute(delete(User))
        await session.execute(delete(Warehouse))
        await session.execute(delete(ProductCategory))
        await session.execute(delete(RevokedToken))
        await session.commit()
        yield session


@pytest_asyncio.fixture()
async def client(session):
    """Inyecta la sesión de test en FastAPI y entrega un AsyncClient."""

    async def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac

    app.dependency_overrides.clear()
```

### Qué hace cada pieza

- `engine`: representa la conexión async base a la BD de test.
- `TestAsyncSession`: generador de sesiones async para la suite.
- `create_test_database`: crea las tablas una sola vez al inicio de pytest.
- `session`: abre una `AsyncSession` limpia antes de cada test.
- `client`: hace que la app use esa misma sesión y devuelve el cliente HTTP async.

```python
import asyncio
import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool
from sqlmodel import SQLModel

from app.main import app
from app.models.database import get_db

TEST_DATABASE_URL = "postgresql+asyncpg://test_user:test_pass@db_test:5432/test_db"
engine = create_async_engine(TEST_DATABASE_URL, echo=True, poolclass=NullPool)
TestAsyncSession = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    async def _create():
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    asyncio.run(_create())


@pytest_asyncio.fixture
async def session():
    async with TestAsyncSession() as session:
        yield session


@pytest_asyncio.fixture
async def client(session):
    async def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client

    app.dependency_overrides.clear()
```

La idea estructural es la misma. Lo que cambia es:

- la sesión,
- el engine,
- el cliente,
- y el uso consistente de `async def` y `await`.

---

## 8. Un test de ejemplo anotado [🔝 Volver al inicio](#)

Vamos a ver dos tests de estilo muy parecido a los de este repositorio:

- uno de creación con `POST`,
- y otro de consulta con `GET`.

La idea no es memorizar el código, sino entender el patrón.

### 8.1 Test de creación de recurso (`POST`) anotado

Este ejemplo sigue el mismo tipo de caso que se ve en `test_products.py`, donde un admin crea un producto y el test comprueba tanto el código HTTP como el contenido del JSON.

```python
import pytest
from app.models.product_category import ProductCategory  # Necesitamos una categoría previa para cumplir la FK category_id.
from app.tests.utils import get_admin_headers  # Helper real del repo: crea admin, hace login y devuelve headers Bearer.


@pytest.mark.asyncio
async def test_admin_can_create_product_successfully(client, session):
    headers, _ = await get_admin_headers(client, session)  # Usa los fixtures para obtener un admin autenticado.

    category = ProductCategory(name="Electronics")  # Prepara una categoría válida que existirá en la BD.
    session.add(category)  # Inserta la categoría en la sesión de test.
    await session.commit()  # Confirma la transacción para que la categoría exista de verdad.
    await session.refresh(category)  # Recarga el objeto para asegurarte de que category.id está disponible.

    product_data = {
        "sku": "PROD001",  # SKU único y válido según la validación del proyecto.
        "short_name": "Smartphone",  # Nombre corto que cumple las restricciones del schema.
        "description": "A high-end phone",  # Campo opcional de descripción.
        "category_id": category.id,  # FK válida a la categoría creada justo antes.
    }

    response = await client.post("/products/", json=product_data, headers=headers)  # Llama al endpoint real con auth real.

    assert response.status_code == 201  # Un POST de creación correcto debe devolver 201 Created.

    data = response.json()  # Convierte la respuesta JSON a dict para poder inspeccionarla.
    assert data["sku"] == "PROD001"  # Comprueba que la API devuelve el SKU que acabas de enviar.
    assert data["short_name"] == "Smartphone"  # Comprueba otro campo funcional del recurso creado.
    assert data["category_id"] == category.id  # Verifica que quedó asociada a la categoría esperada.
    assert data["category_name"] == category.name  # Verifica que el endpoint también resuelve el nombre de categoría.
```

### Qué está comprobando cada `assert`

- `status_code == 201`: el contrato HTTP de creación.
- `data["sku"] == ...`: que se devolvió el recurso correcto.
- `data["short_name"] == ...`: que el body se guardó como esperabas.
- `data["category_id"] == ...`: que la relación con la categoría es correcta.
- `data["category_name"] == ...`: que la serialización de salida incluye el dato relacionado esperado.

### 8.2 Test de consulta (`GET`) anotado

Este ejemplo refleja el mismo patrón que aparece en los tests de listado de productos: primero se siembran datos, luego se llama al endpoint y finalmente se validan la forma y el contenido de la respuesta.

```python
import pytest
from app.models.product import Product  # Modelo para sembrar productos en la BD de test.
from app.models.product_category import ProductCategory  # Modelo de categoría.
from app.tests.utils import get_admin_headers  # Helper real para autenticarse como admin.


@pytest.mark.asyncio
async def test_admin_can_list_all_products(client, session):
    headers, _ = await get_admin_headers(client, session)  # Como admin, este endpoint debe mostrar activos e inactivos.

    category = ProductCategory(name="TestCat")  # Crea una categoría base.
    session.add(category)  # La inserta en la BD.
    await session.commit()  # Confirma para poder usar category.id en los productos.

    session.add_all(
        [
            Product(sku="SKU1", short_name="Prod A", description="Test", category_id=category.id, is_active=True),
            Product(sku="SKU2", short_name="Prod B", description="Test", category_id=category.id, is_active=False),
        ]
    )  # Crea dos productos, uno activo y otro inactivo.
    await session.commit()  # Persiste ambos antes de hacer la llamada GET.

    response = await client.get("/products/", headers=headers)  # Llama al endpoint real.

    assert response.status_code == 200  # Un listado correcto debe devolver 200 OK.

    body = response.json()  # Lee el JSON devuelto por la API.
    assert body["total"] == 2  # Como admin, debe ver los dos productos creados.
    assert any(item["sku"] == "SKU1" for item in body["data"])  # Verifica que aparece el primero.
    assert any(item["sku"] == "SKU2" for item in body["data"])  # Verifica que aparece el segundo.
```

### Cómo usar los fixtures en estos tests

Fíjate en que el test solo declara parámetros:

```python
async def test_admin_can_list_all_products(client, session):
    ...
```

No crea el `client` a mano.
No crea la `session` a mano.
No llama a `conftest.py` directamente.

Pytest resuelve todo por nombre.

### Dónde están los helpers útiles en este repositorio

Además de los fixtures, este proyecto tiene helpers reutilizables para auth en `backend/app/tests/utils.py`:

- `create_user_in_db(...)`
- `get_token_for_user(...)`
- `get_auth_headers(token)`
- `get_admin_headers(client, session)`

Es una buena práctica porque evita repetir en cada test el mismo código de login y creación de usuarios.

---

## 9. Variaciones comunes del setup según el proyecto [🔝 Volver al inicio](#)

El `conftest.py` anterior es una forma sólida de montar tests para FastAPI, pero no es la única. Según el tamaño del proyecto, el coste del setup y el grado de fidelidad que necesites respecto a producción, hay varias variantes igual de válidas.

### 9.1 SQLite en memoria vs PostgreSQL en Docker

| Variante | Cuándo tiene sentido | Ventajas | Inconvenientes |
|---|---|---|---|
| SQLite en memoria | Proyectos pequeños, tests muy rápidos, lógica simple, pocas diferencias SQL | Muy rápido, setup mínimo, fácil de correr sin servicios externos | Menor fidelidad a producción, diferencias en tipos, constraints, transacciones y features específicas de PostgreSQL |
| PostgreSQL en Docker | APIs que usan PostgreSQL en producción y dependen de su comportamiento real | Máxima fidelidad, mismo motor, mejor detección de bugs reales de SQL y constraints | Más lento, requiere contenedor y más infraestructura |

En este repositorio se usa PostgreSQL en Docker porque el objetivo es parecerse más a producción que exprimir al máximo la velocidad.

Si tu aplicación depende de:

- constraints reales,
- tipos específicos de PostgreSQL,
- comportamiento de transacciones,
- o consultas más complejas,

normalmente PostgreSQL de test merece la pena.

### 9.2 `DELETE` antes de cada test vs rollback de transacción

| Variante | Cómo funciona | Ventajas | Limitaciones |
|---|---|---|---|
| `DELETE` antes de cada test | Limpias tablas explícitamente y arrancas desde vacío | Fácil de entender, robusto, muy explícito | Puede ser más lento cuando hay muchas tablas o muchos tests |
| Rollback al final del test | Abres transacción al inicio, el test trabaja dentro de ella y al final haces rollback | Suele ser más rápido, evita borrar tabla por tabla | Puede complicarse si el código bajo test abre sus propias transacciones, hace commits internos o usa varias sesiones |

El patrón de rollback suele verse así, de forma simplificada:

```python
connection = engine.connect()
transaction = connection.begin()
session = Session(bind=connection)

yield session

session.close()
transaction.rollback()
connection.close()
```

Cuándo suele ser mejor el rollback:

- cuando tienes una suite grande,
- cuando casi todos los tests solo necesitan aislar cambios temporales,
- y cuando el código de la app no rompe ese modelo con commits difíciles de controlar.

Cuándo suele ser mejor `DELETE`:

- cuando quieres un enfoque muy claro,
- cuando estás aprendiendo,
- o cuando tu app hace commits reales dentro de los endpoints y prefieres un aislamiento fácil de razonar.

En este repositorio, el enfoque con `DELETE` es directo y bastante resistente a sorpresas.

### 9.3 `create_all` vs Alembic migrations

| Variante | Qué crea el schema de test | Ventajas | Inconvenientes |
|---|---|---|---|
| `SQLModel.metadata.create_all()` | El schema se genera directamente desde los modelos | Simple, rápido de montar, ideal si no usas migraciones todavía | Puede diferir del schema real si en producción el schema evoluciona vía migraciones |
| Ejecutar migraciones de Alembic | El schema de test se crea igual que en producción | Máxima fidelidad entre test y producción | Setup más complejo y más lento |

Este proyecto no usa Alembic ahora mismo, así que la opción natural es `create_all()`.

Pero si un proyecto sí usa migraciones, correr las migraciones reales en tests tiene una ventaja muy clara: garantizas que el schema que pruebas es el mismo que desplegarías.

Eso reduce el riesgo de tener modelos que parecen correctos en código pero no coinciden exactamente con la base de datos real.

### 9.4 Por qué `AsyncClient` es la elección de Tabulae

Tabulae usa `pytest_asyncio` con `httpx.AsyncClient` porque todo el stack es asincronizado:

- todas las rutas son `async def`,
- la sesión de BD es `AsyncSession`,
- las dependencias son async,
- y el driver es `asyncpg`.

**Ventajas de este patrón:**

- Los tests no necesitan adaptar el código; todo funciona como en producción.
- Los fixtures y overrides son async nativamente; no hay trucos de threads.
- El código bajo test puede ejecutar operaciones realmente concurrentes sin bloqueos artificiales.
- Los tests reflejan fielmente el comportamiento real.

**Por qué `AsyncClient` encaja mejor que `TestClient` en Tabulae:**

Si una app usa rutas async pero el código de test fuera síncrono, FastAPI puede ejecutar las rutas en un threadpool. Pero esto crea una brecha entre tests y producción: los tests no verían problemas de concurrencia real, deadlocks, race conditions o ineficiencias en operaciones async.

En un stack como Tabulae, mantener cliente, dependencias y sesión en async evita esa brecha y hace que los tests reproduzcan mejor el comportamiento real.

**Ejemplo del patrón actual en Tabulae:**

```python
import pytest_asyncio
from httpx import ASGITransport, AsyncClient


@pytest_asyncio.fixture
async def client(session):
    async def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client

    app.dependency_overrides.clear()
```

Y los tests se escriben como async:

```python
@pytest.mark.asyncio
async def test_create_product(client):
    response = await client.post("/products/", json={...}, headers={...})
    assert response.status_code == 201
```

### 9.5 Auth real vs auth mockeada

| Variante | Cómo funciona | Ventajas | Inconvenientes |
|---|---|---|---|
| Auth real | El test hace login de verdad y obtiene JWT real | Más fidelidad, cubre login, permisos, tokens y dependencias reales | Más lento, más setup, el test cubre más piezas a la vez |
| Auth mockeada | Sobrescribes `get_current_user` o `require_admin` para devolver un usuario fijo | Tests más rápidos y más focalizados | Menor fidelidad, no detecta bugs de auth/token/dependencias reales |

En este repositorio se usa auth real en bastantes tests. Por ejemplo, helpers como `get_token_for_user(...)` o `get_admin_headers(...)` hacen login real vía `/auth/login`.

Eso tiene una ventaja fuerte: cuando un test de permisos pasa, sabes que la cadena completa está funcionando:

- creación del usuario,
- hash de contraseña,
- login,
- emisión de JWT,
- lectura del token,
- y dependencia de usuario actual.

Pero a veces interesa mockear la auth. Por ejemplo, si quieres probar solo la lógica de un endpoint y no te importa el flujo completo de login.

Sería algo así:

```python
def override_get_current_user():
    return User(id=1, email="admin@example.com", role="admin", is_active=True)


app.dependency_overrides[get_current_user] = override_get_current_user
```

Cuándo suele compensar mockear:

- tests muy unitarios,
- rutas con muchas ramas de lógica,
- o cuando el login real añade demasiado ruido al test.

Cuándo suele compensar mantener auth real:

- tests de integración de API,
- tests de permisos,
- y suites donde la seguridad forma parte del comportamiento que quieres garantizar.

---

## 10. Errores comunes y cómo reconocerlos [🔝 Volver al inicio](#)

Los problemas más frecuentes al empezar con pytest y FastAPI no suelen venir del endpoint en sí, sino del setup del test: fixtures, limpieza de BD, overrides y estado compartido.

### Tabla de diagnóstico rápido

| Síntoma | Qué suele significar | Cómo reconocerlo | Qué revisar |
|---|---|---|---|
| `AssertionError` dentro de un helper en vez de dentro del test | El helper está haciendo demasiadas comprobaciones o escondiendo lógica de test | El traceback apunta a `utils.py` o a una función auxiliar, no al propio test | Mueve los `assert` importantes al test para que el fallo sea más claro |
| Sesión expirada, objeto desenganchado o datos que “desaparecen” tras `commit` | El ciclo de vida de la sesión no es el que creías o el objeto ya no está ligado a una sesión válida | Errores al acceder a atributos después del commit o fuera del fixture | Revisa dónde se crea y cierra la sesión, y si el objeto se usa fuera de su contexto |
| Datos de un test anterior aparecen en otro | Falta aislamiento entre tests | Un test falla solo si se ejecuta después de otro, o el `total` de un listado es mayor de lo esperado | Revisa limpieza de tablas, overrides no limpiados y fixtures con scope demasiado grande |
| Las secuencias de la BD no se resetean | `DELETE` vacía filas pero no reinicia contadores | Esperabas `id == 1` y recibes `id == 7` aunque la tabla esté vacía | No asserts sobre IDs fijos; si hace falta, usa reset explícito de secuencias o compara contra objetos creados en el test |

### 10.1 `AssertionError` en un helper vs en el test

Si el fallo aparece dentro de un helper reutilizable, el diagnóstico suele ser peor porque el traceback te lleva a una capa más lejana del comportamiento que realmente querías comprobar.

Ejemplo menos recomendable:

```python
def assert_product_created(response):
    assert response.status_code == 201
    assert response.json()["sku"] == "PROD001"
```

Si falla, el error apunta al helper, no al caso de negocio concreto.

Mejor:

```python
response = client.post(...)
assert response.status_code == 201
assert response.json()["sku"] == "PROD001"
```

Los helpers están bien para preparar datos o encapsular acciones repetidas. Para asserts críticos, normalmente es mejor que el test sea explícito.

### 10.2 Sesión expirada o uso de objetos fuera de contexto

Síntomas típicos:

- lees un atributo y falla después de un `commit`,
- el objeto parece “desconectado”,
- o accedes a algo fuera del contexto del fixture y ya no existe la sesión activa.

Diagnóstico:

- revisa si ese objeto se creó con una sesión y se usa más tarde fuera de ella,
- revisa si el fixture terminó antes de que el test use ese objeto,
- y revisa si estás mezclando varias sesiones distintas en el mismo test.

En este repositorio se evita bastante confusión porque tanto el test como la app comparten la misma sesión mediante `dependency_overrides`.

### 10.3 Datos que vienen de un test anterior

Este es uno de los fallos más comunes.

Síntomas:

- un listado devuelve más filas de las que debería,
- un test de duplicados falla a veces y a veces no,
- o la suite completa falla, pero el test aislado pasa.

Diagnóstico:

- la limpieza no se está ejecutando,
- el orden FK-safe está incompleto,
- o un fixture dejó estado compartido con un `scope` demasiado grande.

Si además has hecho un override y no lo limpiaste, el problema puede parecer de base de datos cuando en realidad es un problema de dependencia sobreescrita.

### 10.4 Secuencias de BD no reseteadas

Este fallo desconcierta mucho al principio.

Has borrado todos los registros, pero PostgreSQL no vuelve automáticamente a empezar en `1` para los IDs autoincrementales.

Así que esto es frágil:

```python
assert response.json()["id"] == 1
```

Mejor opciones:

- comprobar que existe `id`,
- comparar con el objeto que acabas de crear,
- o si de verdad lo necesitas, resetear secuencias explícitamente.

### 10.5 Errores típicos extra que merece la pena vigilar

Aunque no estén en la tabla principal, estos aparecen mucho:

- olvidar `app.dependency_overrides.clear()` al terminar,
- usar una sesión para sembrar datos y otra distinta dentro del endpoint sin darte cuenta,
- asumir que el login o los tokens no forman parte del comportamiento bajo prueba,
- escribir tests demasiado grandes que prueban muchas cosas a la vez.

Cuando un test falla, intenta localizar primero en cuál de estas capas está el problema:

1. preparación de datos,
2. fixtures,
3. overrides,
4. llamada HTTP,
5. asserts,
6. o estado residual de base de datos.

Ese orden suele acortar bastante el diagnóstico.

---

## Cierre [🔝 Volver al inicio](#)

Si te quedas con tres ideas, que sean estas:

1. pytest gira alrededor de fixtures y aislamiento.
2. FastAPI se testea bien cuando controlas `AsyncClient` y `dependency_overrides`.
3. La base de datos de test debe ser predecible para que la suite sea fiable.

El setup de Tabulae (PostgreSQL en Docker, `pytest_asyncio`, `AsyncClient`, auth real) es una base sólida y representativa del estado real del stack.

La idea importante es mantener el testing coherente con la aplicación real: mismas dependencias, misma base de datos de test, mismo modelo de concurrencia y el menor número posible de atajos ocultos.

### 🔗 Navegación [🔝 Volver al inicio](#)
⬅️ [Lección anterior](./backend_fastapi_2.md) | [Volver al índice principal](../README.md) 