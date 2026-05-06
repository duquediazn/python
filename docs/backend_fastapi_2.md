# Guía de FastAPI Asíncrono con Python

Una guía completa sobre FastAPI, asincronía en Python y construcción de APIs REST de alto rendimiento. Usa [**Tabulae**](https://github.com/duquediazn/tabulae) (un repositorio de gestión de inventarios en producción con FastAPI + SQLModel + PostgreSQL) como ejemplo de referencia para todos los patrones.

Esta guía está pensada para desarrolladores que conocen Python y quieren aprender FastAPI desde los fundamentos, con énfasis en la asincronía y patrones reales de producción.

---

## Índice

### Bloque 1 — Introducción a FastAPI
- [1.1 Qué es FastAPI y sobre qué está construido](#11-qué-es-fastapi-y-sobre-qué-está-construido--volver-al-inicio)
- [1.2 Stack de dependencias del proyecto](#12-stack-de-dependencias-del-proyecto--volver-al-inicio)
- [1.3 Estructura de un proyecto FastAPI](#13-estructura-de-un-proyecto-fastapi--volver-al-inicio)
- [1.4 El ciclo de vida de una petición](#14-el-ciclo-de-vida-de-una-petición--volver-al-inicio)
- [1.5 SQLModel, SQLAlchemy y SQL textual: cómo conviven](#15-sqlmodel-sqlalchemy-y-sql-textual-cómo-conviven--volver-al-inicio)

### Bloque 2 — Asincronía en Python
- [Fundamentos de la Asincronía y Concurrencia](#fundamentos-de-la-asincronía-y-concurrencia--volver-al-inicio)
- [Asincronía aplicada a FastAPI](#asincronía-aplicada-a-fastapi--volver-al-inicio)
- [Recomendaciones y Mejores Prácticas](#recomendaciones-y-mejores-prácticas--volver-al-inicio)
- [Cuándo la asincronía no mejora el rendimiento](#cuándo-la-asincronía-no-mejora-el-rendimiento--volver-al-inicio)
- [Manejo de excepciones y transacciones en async](#manejo-de-excepciones-y-transacciones-en-async--volver-al-inicio)

### Bloque 3 — Arquitectura Asíncrona en Tabulae
- [3.1 Dependencias y cadena de conexión async](#31-dependencias-y-cadena-de-conexión-async--volver-al-inicio)
- [3.2 Capa de base de datos async](#32-capa-de-base-de-datos-async--volver-al-inicio)
- [3.3 Endpoints y dependencias async](#33-endpoints-y-dependencias-async--volver-al-inicio)
- [3.4 Consultas: estructura y patrones en AsyncSession](#34-consultas-estructura-y-patrones-en-asyncsession--volver-al-inicio)
- [3.5 Autenticación y autorización en async](#35-autenticación-y-autorización-en-async--volver-al-inicio)
- [3.6 Servicios de negocio en async](#36-servicios-de-negocio-en-async--volver-al-inicio)
- [3.7 Startup/lifespan y creación de tablas](#37-startuplifespan-y-creación-de-tablas--volver-al-inicio)

---

## Bloque 1 — Introducción a FastAPI 

### 1.1 Qué es FastAPI y sobre qué está construido [🔝 Volver al inicio](#)

FastAPI es un framework web moderno para construir APIs con Python, diseñado desde cero para ser rápido, fácil de usar y producir código listo para producción con muy poco boilerplate.

**Sobre qué está construido:**

| Capa | Librería | Responsabilidad |
|---|---|---|
| HTTP / routing | **Starlette** | Servidor ASGI, routing, middleware, WebSockets |
| Validación y serialización | **Pydantic** | Validar datos de entrada, serializar respuestas, generar el schema OpenAPI |
| Servidor | **Uvicorn** / **Gunicorn** | Ejecutar la aplicación ASGI (Uvicorn en dev, Gunicorn+Uvicorn workers en producción) |
| Concurrencia | **AnyIO** | Abstracción sobre `asyncio` que usa Starlette internamente |

FastAPI en sí mismo es relativamente pequeño — su valor está en cómo orquesta estas capas: usa las anotaciones de tipo de Python para que Pydantic valide automáticamente los datos de entrada y genere la documentación interactiva (Swagger en `/docs`).

**Características que lo diferencian:**
- Validación automática de request bodies, query params y path params gracias a Pydantic
- Documentación OpenAPI generada automáticamente desde el código
- Soporte nativo para `async def` y `def` en el mismo proyecto
- Sistema de inyección de dependencias (`Depends`) potente y composable

---

### 1.2 Stack de dependencias del proyecto [🔝 Volver al inicio](#)

El `requirements.txt` del proyecto refleja las capas habituales de un backend FastAPI con PostgreSQL:

```
# Framework y servidor
fastapi==0.121.1
uvicorn==0.34.0       # Servidor ASGI para desarrollo
gunicorn==23.0.0      # Process manager para producción (lanza workers Uvicorn)
anyio==4.7.0          # Motor de concurrencia subyacente

# Validación
pydantic==2.12.4
email-validator==2.2.0    # Extiende Pydantic para validar emails
python-multipart==0.0.9   # Necesario para recibir formularios (OAuth2PasswordRequestForm)

# Base de datos
SQLAlchemy==2.0.44
sqlmodel==0.0.27       # Capa sobre SQLAlchemy + Pydantic
asyncpg==0.30.0        # Driver asíncrono para PostgreSQL

# Autenticación
PyJWT==2.10.1
bcrypt==4.2.1          # Hash de contraseñas

# Utilidades
python-dotenv==1.2.1   # Carga variables de entorno desde .env
python_dateutil==2.9.0.post0

# Tests
pytest
pytest-asyncio==0.23.6
httpx==0.27.2          # Cliente HTTP asíncrono para tests
websockets==14.1
```

**Nota sobre el driver de PostgreSQL:** `asyncpg` es el driver asíncrono moderno para PostgreSQL en Python. Permite usar `AsyncSession` de SQLAlchemy para obtener máximo rendimiento en operaciones de I/O.

---

### 1.3 Estructura de un proyecto FastAPI [🔝 Volver al inicio](#)

No existe una estructura oficial obligatoria, pero hay un patrón que se ha consolidado en la comunidad para proyectos medianos-grandes. Tabulae lo sigue:

```
backend/app/
├── main.py              # Punto de entrada: crea la app FastAPI, registra routers y middleware
├── dependencies.py      # Dependencias compartidas (get_current_user, require_admin)
│
├── models/              # SQLModel ORM — definen las tablas de la base de datos
│   ├── database.py      # Engine, sesión (get_db) y create_db_and_tables()
│   ├── product.py
│   └── user.py
│
├── schemas/             # Pydantic — definen qué entra y qué sale por la API
│   ├── product.py       # ProductCreate, ProductUpdate, ProductResponse
│   └── user.py
│
├── routers/             # Endpoints agrupados por recurso
│   ├── products.py      # GET /products, POST /products, etc.
│   └── auth.py
│
├── services/            # Lógica de negocio compleja (separada del router)
│   └── stock_move_service.py
│
├── utils/               # Helpers reutilizables
│   ├── authentication.py  # JWT: create_access_token, decode_access_token
│   └── getenv.py
│
└── tests/
    ├── conftest.py      # Fixtures compartidos (client, session)
    └── test_products.py
```

**Por qué `models/` y `schemas/` son carpetas separadas:**

Aunque SQLModel permite que el mismo objeto sea a la vez tabla ORM y schema Pydantic, en este proyecto se separan deliberadamente. Los modelos (`models/`) representan la estructura interna de la base de datos; los schemas (`schemas/`) controlan exactamente qué datos acepta y expone la API. Esto evita filtrar campos internos (como contraseñas o flags de auditoría) por accidente.

---

### 1.4 El ciclo de vida de una petición [🔝 Volver al inicio](#)

Entender qué ocurre desde que llega una petición HTTP hasta que se devuelve la respuesta ayuda a orientarse en el código:

```
HTTP Request
    │
    ▼
Uvicorn (servidor ASGI)
    │
    ▼
FastAPI / Starlette — middleware stack
    │  CORSMiddleware (main.py) — valida origen, añade headers
    │
    ▼
Router — empareja la ruta con el endpoint correcto
    │  Ej: POST /products → routers/products.py → create_product()
    │
    ▼
Resolución de dependencias (Depends)
    │  get_db()          → abre sesión de BD, la inyecta en el endpoint
    │  get_current_user() → valida JWT, consulta usuario en BD
    │  require_admin()   → comprueba rol
    │
    ▼
Función del endpoint
    │  Recibe parámetros ya validados por Pydantic
    │  Ejecuta queries contra la BD vía AsyncSession
    │  Devuelve un objeto Python
    │
    ▼
Pydantic serialización (response_model)
    │  Convierte el objeto en JSON según el schema de respuesta
    │  Filtra campos no incluidos en el response_model
    │
    ▼
HTTP Response
```

**En código, `main.py` registra este stack:**

```python
# main.py — fragmento real del proyecto
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()  # Se ejecuta al arrancar el servidor
    yield                    # Aquí vive la app; lo que venga después del yield se ejecuta al apagar

app = FastAPI(title="Tabulae API", lifespan=lifespan)

app.add_middleware(CORSMiddleware, allow_origins=origins, ...)

app.include_router(auth.router)       # prefix="/auth"
app.include_router(products.router)   # prefix="/products"
# ...
```

**Nota sobre `lifespan`:** el patrón `@asynccontextmanager` con `lifespan` es la forma moderna de gestionar el startup y shutdown de la app (reemplaza los eventos `@app.on_event("startup")` que aparecen en documentación antigua).

---

### 1.5 SQLModel, SQLAlchemy y SQL textual: cómo conviven [🔝 Volver al inicio](#)

Una de las dudas más comunes al entrar en un proyecto FastAPI es si realmente se está usando "SQLModel" o "SQLAlchemy". En la práctica, aquí se usan ambos, pero no como dos herramientas rivales, sino como capas complementarias.

#### Qué aporta cada una

- **SQLAlchemy** es la base técnica: engine, sesiones, transacciones, excepciones, tipos de columna, constraints y la API ORM/Core.
- **SQLModel** se apoya sobre SQLAlchemy y Pydantic para ofrecer modelos tipados más cómodos en proyectos FastAPI.
- **Librerías centradas en SQL textual**, como `databases`, priorizan consultas SQL explícitas o construcción de sentencias con menos peso de ORM.

En otras palabras: cuando en este proyecto defines un modelo con `SQLModel`, por debajo sigue existiendo SQLAlchemy.

#### Cómo se ve esto en Tabulae

Hay modelos que usan solamente `SQLModel` y `Field(...)` con opciones simples. Por ejemplo:

```python
class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: int = Field(default=None, primary_key=True, nullable=False)
    sku: str = Field(unique=True, index=True, nullable=False)
    category_id: int = Field(foreign_key="product_category.id", nullable=False)
```

Ese estilo cubre muy bien el CRUD habitual.

Pero en este repo también hay modelos donde se baja un nivel para usar primitivas de SQLAlchemy dentro de `SQLModel` mediante `sa_column=...`. Esto aparece cuando hace falta más control sobre la columna o la restricción.

Ejemplos reales del repositorio:

```python
quantity: int = Field(
    sa_column=Column(Integer, CheckConstraint("quantity >= 0"), nullable=False)
)
```

```python
line_id: int = Field(
    sa_column=Column(Integer, CheckConstraint("line_id > 0"), primary_key=True)
)
```

```python
name: str = Field(
    sa_column=Column("name", String(255), nullable=False)
)
```

Esto significa que el proyecto no está mezclando dos ORMs distintos. Está usando `SQLModel` como capa principal de modelado y `SQLAlchemy` como capa subyacente para personalizaciones más finas.

#### Dónde aparece SQLAlchemy además de en los modelos

SQLAlchemy no solo aparece al definir tablas. También se usa en:

- **Sesiones y engine**: `create_async_engine`, `AsyncSession` y `async_sessionmaker`.
- **Excepciones**: `IntegrityError`, `SQLAlchemyError`.
- **Construcción de consultas**: `select`, `func`, subqueries y joins.
- **Configuración avanzada de columnas**: `Column`, `String`, `Integer`, `CheckConstraint`.

Por eso es normal ver imports de SQLAlchemy en routers, servicios y algunos modelos aunque el proyecto se presente como basado en SQLModel.

#### Cómo leer y escribir consultas con SQLModel/SQLAlchemy

La parte que más suele costar al principio no son los modelos, sino la sintaxis de consulta. Para entenderla bien, lo más útil es leerla ya en su forma async, que es hacia donde apunta la guía.

Ejemplo representativo, simplificado a partir de `products.py` pero escrito ya en estilo async:

```python
statement = select(Product, ProductCategory.name).join(
    ProductCategory, Product.category_id == ProductCategory.id
)

if search:
    search_like = f"%{search.lower()}%"
    statement = statement.where(
        func.lower(Product.short_name).ilike(search_like)
        | func.lower(Product.sku).ilike(search_like)
    )

statement = statement.order_by(Product.short_name).limit(limit).offset(offset)
result = await db.execute(statement)
products_raw = result.all()
```

La forma útil de leerlo es esta:

1. `select(Product, ProductCategory.name)`
   - Equivale al `SELECT ...` de SQL.
   - Indica qué columnas o entidades quieres devolver.

2. `.join(ProductCategory, Product.category_id == ProductCategory.id)`
   - Equivale al `JOIN ... ON ...`.
   - Une tablas explícitamente.

3. `.where(...)`
   - Equivale al `WHERE`.
   - Puedes encadenarlo varias veces; SQLAlchemy compone la condición final.

4. `func.lower(...).ilike(...)`
   - `func` representa funciones SQL del motor (`LOWER`, `COUNT`, etc.).
   - `ilike` equivale a un `LIKE` case-insensitive en PostgreSQL.

5. `.order_by(...)`, `.limit(...)`, `.offset(...)`
   - Son traducciones casi literales de `ORDER BY`, `LIMIT` y `OFFSET`.

En este estilo, lo normal es construir la sentencia gradualmente y reasignarla a la misma variable (`statement = ...`). Eso permite añadir filtros de forma condicional sin escribir SQL manualmente.

#### Traducción mental rápida: SQL -> SQLAlchemy

```sql
SELECT p.*, pc.name
FROM product p
JOIN product_category pc ON p.category_id = pc.id
WHERE LOWER(p.short_name) LIKE '%milk%'
ORDER BY p.short_name
LIMIT 10 OFFSET 0;
```

```python
statement = (
    select(Product, ProductCategory.name)
    .join(ProductCategory, Product.category_id == ProductCategory.id)
    .where(func.lower(Product.short_name).ilike("%milk%"))
    .order_by(Product.short_name)
    .limit(10)
    .offset(0)
)
result = await db.execute(statement)
rows = result.all()
```

La ventaja es que sigues pensando en SQL, pero con objetos Python tipados y composición segura.

#### Patrones frecuentes de consulta en este proyecto

**1. Buscar una sola fila**

```python
statement = select(Product).where(Product.id == product_id)
result = await db.execute(statement)
product = result.scalars().first()
```

**2. Listar varias filas**

```python
statement = select(Product).where(Product.is_active == True)
result = await db.execute(statement)
products = result.scalars().all()
```

**3. Contar resultados**

```python
result = await db.execute(
    select(func.count()).select_from(statement.subquery())
)
total_records = result.scalar_one()
```

**4. Consultar con join y devolver varias columnas**

```python
statement = select(Product, ProductCategory.name).join(
    ProductCategory, Product.category_id == ProductCategory.id
)
result = await db.execute(statement)
rows = result.all()
```

En este último caso, cada fila no es solo un `Product`, sino una tupla con los elementos seleccionados.

Nota rápida sobre `scalars()`:
- Úsalo cuando el `select(...)` devuelve una única entidad o columna por fila (por ejemplo, `select(Product)`), para obtener directamente esa entidad/valor.
- Evítalo cuando el `select(...)` devuelve múltiples columnas/entidades (por ejemplo, `select(Product, ProductCategory.name)`), porque `scalars()` tomaría solo el primer elemento y perderías el resto.

#### Comparación práctica: SQLModel/SQLAlchemy vs `databases`

La diferencia clave no es solo de librería, sino de estilo mental.

**Con SQLModel/SQLAlchemy en estilo async:**

```python
statement = (
    select(Product, ProductCategory.name)
    .join(ProductCategory, Product.category_id == ProductCategory.id)
    .where(Product.is_active == True)
    .order_by(Product.short_name)
    .limit(limit)
    .offset(offset)
)
result = await db.execute(statement)
rows = result.all()
```

**Con `databases` + SQL más explícito:**

```python
query = """
SELECT p.*, pc.name AS category_name
FROM product p
JOIN product_category pc ON p.category_id = pc.id
WHERE p.is_active = true
ORDER BY p.short_name
LIMIT :limit OFFSET :offset
"""

rows = await database.fetch_all(query=query, values={
    "limit": limit,
    "offset": offset,
})
```

Qué cambia entre ambos enfoques:

- **SQLModel/SQLAlchemy** te deja construir consultas como objetos Python, reutilizar fragmentos, apoyarte en entidades del modelo y reducir errores estructurales al renombrar columnas o tablas.
- **`databases`** te deja escribir SQL casi tal cual lo piensas, lo que puede ser más directo para quien domina SQL y quiere control explícito desde el principio.

#### Ventajas concretas de cada sintaxis

**Ventajas de SQLModel/SQLAlchemy para consultas:**
- composición incremental de filtros;
- integración más natural con los modelos ya definidos;
- más reutilización de expresiones y subqueries;
- transición más homogénea a async dentro del ecosistema SQLAlchemy.

**Ventajas de `databases` o SQL más textual:**
- lectura inmediata para perfiles muy orientados a SQL;
- consultas complejas a veces más fáciles de copiar, perfilar y comparar con el motor;
- menor distancia entre la consulta escrita y la SQL final ejecutada.

**Inconvenientes prácticos de `databases`:**
- más mapping manual de resultados;
- más responsabilidad al mantener nombres de columnas, alias y tipos;
- menos cohesión con el modelado ya existente en este repo.

#### Recomendación práctica para aprender la sintaxis

Si tu objetivo es entender bien SQLAlchemy en este proyecto, la mejor estrategia es leer las queries con esta plantilla mental:

1. Qué selecciono: `select(...)`
2. Con qué uno: `.join(...)`
3. Qué filtro: `.where(...)`
4. Cómo ordeno/pagino: `.order_by(...).limit(...).offset(...)`
5. Qué forma tiene el resultado: `scalars().first()`, `scalars().all()`, `all()`, contadores

Si dominas esa secuencia, ya puedes leer la mayoría de queries del repo sin problema. El salto a `databases` sería más un cambio de estilo de escritura que de conceptos de base de datos.

#### Cuándo conviene usar SQLModel y cuándo bajar a SQLAlchemy

**Usa SQLModel directamente cuando:**
- quieres modelos tipados y legibles;
- el caso es un CRUD típico;
- las restricciones de columna son simples;
- quieres una integración natural con FastAPI y Pydantic.

**Baja a primitivas de SQLAlchemy cuando:**
- necesitas `CheckConstraint` u otras restricciones avanzadas;
- quieres definir un tipo de columna concreto, como `String(255)`;
- necesitas más control sobre la definición SQL real;
- estás trabajando con sesiones async y consultas más cercanas a SQLAlchemy 2.x.

En este repo, ese punto intermedio ya existe: el modelado es principalmente SQLModel, pero no renuncia a capacidades de SQLAlchemy cuando hacen falta.

#### Comparación con alternativas basadas en SQL más explícito

Una alternativa habitual es usar una librería como `databases`, o incluso escribir SQL más explícito con menos capa ORM.

**Ventajas de SQLModel + SQLAlchemy:**
- modelos tipados y coherentes con FastAPI;
- menos boilerplate al definir entidades;
- restricciones y columnas avanzadas disponibles cuando hacen falta;
- transición razonable hacia async con la infraestructura de SQLAlchemy.

**Ventajas de SQL textual o herramientas como `databases`:**
- control muy directo sobre la consulta;
- menor abstracción conceptual en consultas complejas;
- a veces más claridad cuando el equipo prefiere pensar en SQL puro.

**Costes de ir a SQL textual puro:**
- más trabajo manual para mapear resultados;
- menos cohesión entre estructura de datos y acceso a base de datos;
- más dispersión si conviven muchas consultas escritas a mano.

#### Recomendación para este proyecto

Para Tabulae, la estrategia más coherente es:

1. Mantener `SQLModel` como capa principal de modelos.
2. Seguir usando `SQLAlchemy` puntualmente para constraints, tipos y control fino.
3. No reescribir el proyecto hacia SQL textual puro salvo que exista una necesidad clara de rendimiento o de control muy específico.

Con esa combinación se obtiene un equilibrio bueno entre productividad, legibilidad y capacidad de extensión.

---

## Bloque 2 — Asincronía en Python

La asincronía en Python es una herramienta fundamental para el desarrollo de aplicaciones web de alto rendimiento. Basada en la biblioteca asyncio, permite gestionar operaciones de entrada y salida (I/O) de manera eficiente, optimizando el tiempo de espera del procesador.

### Fundamentos de la Asincronía y Concurrencia [🔝 Volver al inicio](#)

El código asíncrono permite que un programa notifique a la computadora que debe esperar a que una tarea externa finalice (como una operación de red o lectura de disco) para que, mientras tanto, el sistema pueda ejecutar otras tareas.

#### Concurrencia vs. Paralelismo: La Analogía de las Hamburguesas

Para entender la diferencia entre estos conceptos, se utiliza a menudo el ejemplo de un restaurante de comida rápida:

**1. Concurrencia (Asincronía):** Es equivalente a pedir dos hamburguesas, recibir un número de turno y sentarse a conversar con un acompañante mientras la cocina las prepara. No se está "ocioso" frente al mostrador; se aprovecha el tiempo de espera para otra actividad productiva (la conversación). Cuando el número aparece en la pantalla, se interrumpe la charla momentáneamente para recoger el pedido.
**2. Paralelismo:** Sería equivalente a tener múltiples cajeros que también son cocineros. Cada cliente espera frente a su cajero hasta que la hamburguesa esté lista. Si hay 8 cajeros, se procesan 8 pedidos a la vez, pero cada procesador (cajero) está bloqueado e inactivo mientras la carne se cocina, impidiendo otras tareas (como hablar con el acompañante).

En el desarrollo web, la concurrencia es generalmente más beneficiosa porque las aplicaciones pasan la mayor parte del tiempo esperando respuestas de bases de datos, APIs remotas o conexiones de clientes lentas (operaciones I/O bound). El paralelismo es preferible para tareas intensivas de cálculo matemático o procesamiento de imágenes (CPU bound).

#### Conceptos Clave en Python

Python utiliza una nomenclatura específica para gestionar la ejecución asíncrona:

- **Corrutina (Coroutine):** Es el objeto devuelto por una función definida con async def. Python sabe que puede iniciarla, pausarla y que terminará en algún momento.
- **Task (Tarea):** Es un envoltorio para una corrutina que permite programar su ejecución de forma concurrente dentro del bucle de eventos (event loop).
- **Future:** Un objeto que representa un resultado que aún no se ha obtenido pero que se obtendrá en el futuro.
- **Await:** Palabra clave que indica a Python que debe pausar la ejecución de la corrutina actual y ceder el control al bucle de eventos hasta que la tarea esperada finalice.

#### Sintaxis async y await

El uso de estas palabras clave permite que el código asíncrono se lea de forma secuencial, facilitando su comprensión y mantenimiento.

```python
async def obtener_hamburguesas(cantidad: int):
    # Simulación de una operación que requiere espera
    await asyncio.sleep(1) 
    return f"{cantidad} hamburguesas listas"

async def main():
    # El uso de await permite que Python haga otras cosas mientras espera
    burgers = await obtener_hamburguesas(2)
    print(burgers)
```

#### Reglas de uso

1. await solo puede utilizarse dentro de funciones declaradas con `async def`.
2. Las funciones async def deben ser "esperadas" (utilizando await) para obtener su resultado; de lo contrario, solo devuelven el objeto de la corrutina.

### Paralelismos con JavaScript (Promises) [🔝 Volver al inicio](#)

Para desarrolladores familiarizados con JavaScript, la transición a Python `asyncio` es intuitiva, ya que comparten patrones similares:

|JavaScript (Promises)|	Python (asyncio)|	Caso de Uso|
|---------------------|-----------------|--------------|
|Promise.all(promises)|	asyncio.gather(*coroutines)|	Esperar todas las tareas; falla si una falla.|
|Promise.allSettled(promises)|	asyncio.wait(tasks, return_when=ALL_COMPLETED)|	Esperar todas, sin importar éxito o error.|
|Promise.race(promises)|	asyncio.wait(tasks, return_when=FIRST_COMPLETED)|	Retornar el resultado de la primera que termine.|
|.then().catch()|	try: await ... except:|	Manejo de resultados y errores.|
|async function()|	async def function():|	Definición de operación asíncrona.|

**Nota técnica:** En Python 3.11+, se introdujo TaskGroup, que ofrece una forma más estructurada y segura de manejar grupos de tareas concurrentes con mejor gestión de errores.

### Asincronía aplicada a FastAPI [🔝 Volver al inicio](#)

FastAPI está construido sobre `Starlette` y `AnyIO`, lo que le permite alcanzar un rendimiento comparable a `NodeJS` o `Go`. Una de sus mayores ventajas es la flexibilidad en la definición de las funciones de operación de ruta (path operation functions).

#### ¿Cuándo usar async def vs def?

FastAPI gestiona ambos tipos de funciones de manera inteligente:

- **Usar async def**:
  - Si utilizas bibliotecas de terceros que requieren el uso de `await` (ej. clientes de BD asíncronos).
  - Si tu función no realiza ninguna operación de comunicación pero quieres mantener la estructura asíncrona.
  - Si tienes operaciones puramente de computación triviales (el rendimiento es mejor que con def normal).
- **Usar def normal**:
  - Si utilizas bibliotecas que realizan operaciones de I/O bloqueantes (bases de datos tradicionales, acceso a sistema de archivos sin soporte async). En este caso, FastAPI ejecutará la función en un threadpool (hilo separado) externo para no bloquear el bucle de eventos principal.

#### Ejemplo en FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

# Caso 1: Biblioteca asíncrona
@app.get("/items-async")
async def read_items_async():
    results = await some_async_library.get_data()
    return results

# Caso 2: Biblioteca bloqueante (sincrónica)
@app.get("/items-sync")
def read_items_sync():
    # FastAPI ejecutará esto en un hilo separado automáticamente
    results = some_sync_library.get_data()
    return results
```

#### Dependencias y Sub-dependencias

FastAPI permite mezclar `def` y `async def` en las dependencias. Si una dependencia es def, se ejecuta en el `threadpool`; si es `async def`, FastAPI la "espera" adecuadamente. Esto permite una integración fluida entre código moderno asíncrono y código legado bloqueante.

### Recomendaciones y Mejores Prácticas [🔝 Volver al inicio](#)

1. **I/O Bound:** Para operaciones de red, utiliza bibliotecas diseñadas para asincronía, como `aiohttp` en lugar de `requests`.
2. **Manejo de Errores:** Utiliza bloques `try/except` alrededor de los await para capturar excepciones de tareas específicas, similar al `.catch()` de las Promesas.
3. **No bloquear el bucle:** Nunca realices operaciones pesadas de CPU o I/O bloqueante dentro de una función `async def` sin `await`, ya que esto detendrá todo el servidor. Si es inevitable, declara la función con def normal para que FastAPI la mueva a un hilo separado.
4. **Uso de asyncio.gather:** Es la forma más común de ejecutar tareas concurrentes en Python, similar a `Promise.all`. Utiliza el parámetro `return_exceptions=True` si deseas manejar fallos individuales sin detener el grupo completo.

### Cuándo la asincronía no mejora el rendimiento [🔝 Volver al inicio](#)

La asincronía no es una mejora automática. Mejora principalmente workloads **I/O bound** (espera de red, BD, APIs externas). Si el cuello de botella es CPU, cambiar `def` a `async def` no aporta ventaja por sí solo.

Casos donde `async` suele no mejorar (o puede empeorar):

1. **Trabajo CPU-bound dentro del endpoint**
    - Ejemplos: hash masivo de archivos, compresión pesada, procesamiento de imágenes grande.
    - Problema: el event loop queda ocupado y no atiende otras corrutinas.
    - Solución típica: mover ese trabajo a workers externos (Celery/RQ) o procesos dedicados.

2. **Código "async" que llama librerías bloqueantes**
    - Ejemplo: un endpoint `async def` que internamente usa un cliente HTTP bloqueante o un driver de BD síncrono.
    - Problema: parece asíncrono, pero bloquea igual.
    - Solución: usar librerías realmente async (`httpx.AsyncClient`, `asyncpg`, etc.) o mantener `def` y asumir threadpool.

3. **Concurrencia excesiva sin límites**
    - Ejemplo: lanzar cientos de tareas con `asyncio.gather` sin semáforos ni control de pool de conexiones.
    - Problema: saturación de recursos y aumento de latencia global.
    - Solución: limitar concurrencia y dimensionar correctamente pools y timeouts.

4. **Endpoints simples en sistemas de baja carga**
    - Si la aplicación tiene tráfico moderado y consultas rápidas, adoptar async en toda la superficie puede no compensar su complejidad operativa.

Regla práctica para Tabulae:
- Async aporta especialmente en rutas con mucha espera de I/O (consultas concurrentes, integraciones externas, WebSockets).
- En operaciones de negocio CPU-heavy, prioriza paralelismo por proceso/worker antes que `await`.

### Manejo de excepciones y transacciones en async [🔝 Volver al inicio](#)

Con `AsyncSession`, todas las operaciones de sesión son awaitables. Esto incluye las ramas de excepción: olvidar `await` en un `rollback` deja la transacción abierta y puede causar estados inconsistentes.

#### Patrón estándar

```python
try:
     db.add(entity)
     await db.commit()
     await db.refresh(entity)
except IntegrityError:
     await db.rollback()
     raise HTTPException(status_code=409, detail="Conflict")
except SQLAlchemyError:
     await db.rollback()
     raise HTTPException(status_code=500, detail="Database error")
```

Puntos clave:

1. **`rollback` también lleva `await`**
    - Es uno de los errores más comunes: olvidar `await db.rollback()` en ramas de excepción.

2. **`await db.execute(...)` devuelve un `CursorResult`**
    - Hay que obtener filas con `result.scalars().first()` o `result.scalars().all()`.

3. **El `try` debe envolver la operación transaccional completa**
    - `IntegrityError` se dispara en `commit` o `flush`, no en `add()`. Si `add()` está fuera del `try`, el error no se captura.

4. **Errores de concurrencia**
    - En async aparecen con más frecuencia timeouts de pool y cancelaciones de tareas; conviene mapearlos a respuestas HTTP controladas y logs claros.

---

## Bloque 3 — Arquitectura Asíncrona en Tabulae

Tabulae es un ejemplo de referencia de una arquitectura FastAPI orientada a async en producción. Este bloque describe cómo está estructurado su backend: desde la capa de base de datos hasta los endpoints, servicios y tests.

### 3.1 Dependencias y cadena de conexión async [🔝 Volver al inicio](#)

El proyecto usa `asyncpg` como driver asíncrono de PostgreSQL. La cadena de conexión incluye el prefijo `+asyncpg` para indicar a SQLAlchemy que use el driver asíncrono:

```env
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db
```

El `requirements.txt` refleja esta estructura:

```
SQLAlchemy==2.0.44
sqlmodel==0.0.27
asyncpg==0.30.0        # Driver asíncrono para PostgreSQL
pytest-asyncio==0.23.6
httpx==0.27.2          # Cliente HTTP asíncrono para tests
```

### 3.2 Capa de base de datos async [🔝 Volver al inicio](#)

En `models/database.py`, el engine y la sesión están completamente asincronizados:

```python
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

engine = create_async_engine(DATABASE_URL, echo=echo)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

Notas importantes:
- `create_async_engine` en lugar de `create_engine`.
- `async_sessionmaker` en lugar de `sessionmaker`.
- `expire_on_commit=False` evita lecturas inesperadas tras `commit`.
- `get_db` es `async def` y usa `async with`.

Esta dependencia se usa en los endpoints que trabajan con base de datos vía `Depends(get_db)`.

### 3.3 Endpoints y dependencias async [🔝 Volver al inicio](#)

Los endpoints de negocio en Tabulae son `async def` y reciben `AsyncSession` vía dependencia:

```python
@router.post("/")
async def create_product(
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        new_product = Product(**product_data.model_dump())
        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)
        return new_product
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Product already exists")
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
```

Puntos clave:
- Firma `async def`.
- Tipo `AsyncSession`.
- `await` en todas las operaciones de sesión: `commit()`, `refresh()`, `rollback()`, `flush()`.
- Manejo explícito de excepciones con rollback.

### 3.4 Consultas: estructura y patrones en AsyncSession [🔝 Volver al inicio](#)

Las consultas siguen el mismo patrón que con sesiones síncronas, pero con `await db.execute()`:

```python
statement = select(Product, ProductCategory.name).join(
    ProductCategory, Product.category_id == ProductCategory.id
)

if search:
    search_like = f"%{search.lower()}%"
    statement = statement.where(
        func.lower(Product.short_name).ilike(search_like)
        | func.lower(Product.sku).ilike(search_like)
    )

statement = statement.order_by(Product.short_name).limit(limit).offset(offset)
result = await db.execute(statement)
products_raw = result.all()

total_query = select(func.count()).select_from(statement.subquery())
total_result = await db.execute(total_query)
total_records = total_result.scalar_one()
```

Mapeo de métodos:
- `db.execute(stmt)` devuelve un `CursorResult`.
- `result.scalars().first()` — obtiene el primer objeto.
- `result.scalars().all()` — obtiene todas las filas como objetos.
- `result.all()` — obtiene todas las filas como tuplas (útil con joins de múltiples columnas).
- `result.scalar_one()` — obtiene un único valor escalar.

#### Métodos comunes en AsyncSession

Además de `execute()`, AsyncSession ofrece:

```python
# Obtener por clave primaria
user = await db.get(User, user_id)

# Borrar una instancia
await db.delete(product)
await db.commit()
```

Todos estos métodos incluyen `await`.

### 3.5 Autenticación y autorización en async [🔝 Volver al inicio](#)

`get_current_user` y `require_admin` son dependencias asincronizadas en `dependencies.py`:

```python
async def get_current_user(
    token: str = Depends(oauth2),
    db: AsyncSession = Depends(get_db),
):
    payload = decode_access_token(token, expected_type="access")
    user_id = int(payload.get("sub"))
    
    statement = select(User).where(User.id == user_id)
    result = await db.execute(statement)
    user = result.scalars().first()
    
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user


async def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    return current_user
```

Estas dependencias se reutilizan en todos los routers, manteniendo la seguridad centralizada.

#### WebSocket en async

Los WebSockets en Tabulae se autentican en el primer mensaje recibido, usando una sesión async para validar el token:

```python
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        data = await websocket.receive_text()
        token = json.loads(data).get("token")
        
        # Validar token con sesión async
        async with AsyncSessionLocal() as db:
            result = await db.execute(select(User).where(User.id == user_id))
            user = result.scalars().first()
        
        if not user:
            await websocket.close(code=1008, reason="Unauthorized")
            return
        
        # ... resto del handler
    except Exception as e:
        await websocket.close(code=1011, reason="Internal error")
```

### 3.6 Servicios de negocio en async [🔝 Volver al inicio](#)

Los servicios en `services/` encapsulan lógica de negocio compleja con operaciones async:

```python
async def create_stock_movement(
    movement_data: StockMoveCreate,
    user_id: int,
    db: AsyncSession,
):
    # Validaciones
    _validate_movement_input(movement_data)
    
    # Crear cabecera del movimiento
    new_movement = StockMove(
        movement_type=movement_data.movement_type,
        warehouse_id=movement_data.warehouse_id,
        created_by_id=user_id,
    )
    db.add(new_movement)
    await db.flush()  # Obtiene el ID para usarlo en las líneas
    
    # Crear líneas del movimiento
    for line_data in movement_data.lines:
        new_line = StockMoveLine(
            stock_move_id=new_movement.id,
            product_id=line_data.product_id,
            quantity=line_data.quantity,
        )
        db.add(new_line)
    
    await db.commit()
    await db.refresh(new_movement)
    return new_movement
```

### 3.7 Startup/lifespan y creación de tablas [🔝 Volver al inicio](#)

El lifespan de la aplicación maneja la creación de tablas de forma asíncrona:

```python
async def create_db_and_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(
    title="Tabulae API",
    lifespan=lifespan,
)
```


### 🔗 Navegación [🔝 Volver al inicio](#)
⬅️ [Lección anterior](./backend_fastapi.md) | [Volver al índice principal](../README.md) | [Siguiente lección ➡️](./backend_unit_testing.md)