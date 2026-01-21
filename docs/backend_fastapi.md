# Introducción a FastAPI

Guía práctica paso a paso para aprender a construir **APIs REST con FastAPI**, el framework moderno y veloz de Python para desarrollo backend.

En este documento recorrerás desde los fundamentos hasta la autenticación con JWT y la conexión a bases de datos reales como **MongoDB**, usando un **proyecto completo de ejemplo** incluido en este repositorio.

📁 **Proyecto de ejemplo:** [Backend/FastAPI](../backend/FastApi/)  
(contiene el código base con rutas, autenticación y conexión a MongoDB)

---

## Índice

1. [Qué es FastAPI y por qué usarlo](#1-qué-es-fastapi-y-por-qué-usarlo--volver-al-inicio)
2. [Estructura del proyecto](#2-estructura-del-proyecto--volver-al-inicio)
3. [Primeros pasos con FastAPI](#3-primeros-pasos-con-fastapi--volver-al-inicio)
4. [Routers y modularización](#4-routers-y-modularización--volver-al-inicio)
5. [Modelos y validación con Pydantic](#5-modelos-y-validación-con-pydantic--volver-al-inicio)
6. [Operaciones CRUD](#6-operaciones-crud--volver-al-inicio)
7. [Autenticación básica (OAuth2 Password)](#7-autenticación-básica-oauth2-password--volver-al-inicio)
8. [Autenticación con JWT (JSON Web Tokens)](#8-autenticación-con-jwt-json-web-tokens--volver-al-inicio)
9. [Conexión a MongoDB](#9-conexión-a-mongodb--volver-al-inicio)
10. [Recursos estáticos](#10-recursos-estáticos--volver-al-inicio)
11. [Buenas prácticas y próximos pasos](#11-buenas-prácticas-y-próximos-pasos--volver-al-inicio)

---

## 1. Qué es FastAPI y por qué usarlo [🔝 Volver al inicio](#)

FastAPI es un framework moderno, rápido y fácil de usar para construir **APIs RESTful con Python**. Su nombre viene precisamente de su objetivo principal: **velocidad**. Está construido sobre **Starlette** (para el manejo del servidor web) y **Pydantic** (para la validación de datos), combinando lo mejor de ambos mundos: rendimiento y tipado estático.

FastAPI está diseñado desde el inicio para aprovechar al máximo las características modernas de Python, como **type hints**, **asincronía (async/await)** y la **autogeneración de documentación**.

---

### Ventajas principales

- **Rápido**: Su rendimiento es comparable a frameworks como **Node.js** o **Go** gracias a Starlette y Uvicorn.
- **Productivo**: Reduce la cantidad de código repetitivo gracias al tipado y la validación automática.
- **Seguro**: Integra fácilmente autenticación, validación de datos y manejo de errores.
- **Documentado automáticamente**: Genera documentación interactiva (Swagger UI y ReDoc) sin escribir una sola línea extra.
- **Basado en estándares**: Cumple con las especificaciones **OpenAPI** y **JSON Schema**.
- **Intuitivo**: Aprovecha los tipos de Python para ofrecer autocompletado en el editor y errores más claros.

---

### Instalación y primer servidor

Para empezar, crea un entorno virtual y ejecuta:

**Instalación:**  
`pip install "fastapi[all]"`  
Esto instala FastAPI junto a **Uvicorn**, el servidor ASGI recomendado.

**Ejecución del servidor:**  
`fastapi dev main.py`  
o alternativamente:  
`uvicorn main:app --reload`

**Accede a la API:**

- Endpoint principal: http://127.0.0.1:8000
- Documentación interactiva (Swagger UI): http://127.0.0.1:8000/docs
- Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc

---

### Conceptos clave

**ASGI**: (Asynchronous Server Gateway Interface) — sucesor de WSGI. Permite manejar peticiones de forma asíncrona y eficiente.  
**OpenAPI**: estándar que define cómo describir y documentar una API REST. FastAPI lo genera automáticamente.  
**Pydantic**: librería que valida y serializa datos usando anotaciones de tipo de Python.  
**Uvicorn**: servidor ultrarrápido basado en ASGI para ejecutar la aplicación FastAPI.

---

### Ejemplo mínimo

El archivo más simple que puedes crear para iniciar una API con FastAPI es:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "¡Hola FastAPI!"}
```

Ejecuta el servidor y visita `http://127.0.0.1:8000/docs` para probar el endpoint desde la interfaz Swagger.

---

## 2. Estructura del proyecto [🔝 Volver al inicio](#)

Este proyecto es una **aplicación REST construida con FastAPI**, diseñada como ejemplo de aprendizaje progresivo.  
La estructura está organizada en módulos para mantener el código **limpio, reutilizable y escalable**, separando las responsabilidades en distintos archivos y carpetas.

---

### Estructura general

```
├── db
│   ├── client.py
│   ├── models
│   │   └── user.py
│   └── schemas
│       └── user.py
├── main.py
├── routers
│   ├── basic_auth_users.py
│   ├── jwt_auth_users.py
│   ├── products.py
│   ├── users_db.py
│   └── users.py
└── static
    └── images
        └── utopia.png
```

---

### Descripción de carpetas y archivos

### `main.py`

Es el punto de entrada de la aplicación.  
Aquí se crea la instancia principal de FastAPI (`app = FastAPI()`) y se incluyen los distintos **routers** que organizan las rutas de la API.

Además:

- Define las rutas base (`/` y `/url`).
- Monta los recursos estáticos (imágenes, CSS, etc.) con `StaticFiles`.
- Contiene los comentarios sobre cómo ejecutar el servidor y acceder a la documentación.

Ejemplo desde el archivo:

```python
app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
```

---

### 📁 `routers/`

Contiene los diferentes módulos de rutas o endpoints de la API.  
Cada archivo agrupa un conjunto de funcionalidades específicas, lo que facilita mantener y escalar la aplicación.

- **`users.py`** → CRUD completo sobre una lista de usuarios (sin base de datos).
- **`products.py`** → Endpoints simples para listar productos (ejemplo básico).
- **`basic_auth_users.py`** → Ejemplo de autenticación básica usando OAuth2.
- **`jwt_auth_users.py`** → Ejemplo avanzado con autenticación JWT y contraseñas cifradas.
- **`users_db.py`** → CRUD real conectado a una base de datos MongoDB.

Cada uno define un `APIRouter` con su propio prefijo, etiquetas y respuestas personalizadas.

---

### 📁 `db/`

Contiene toda la lógica relacionada con la base de datos.

- **`client.py`** → Configura la conexión a MongoDB, tanto local como remota (MongoDB Atlas).
- **`models/user.py`** → Define el modelo de usuario usando `Pydantic` para validar datos.
- **`schemas/user.py`** → Define las funciones que transforman los datos de MongoDB a un formato compatible con FastAPI (maneja los `_id` y los convierte a `str`).

---

### 📁 `static/`

Carpeta de recursos estáticos servidos por FastAPI, como imágenes o archivos públicos.

- En este ejemplo: `static/images/utopia.png`
- Accesible desde: `http://127.0.0.1:8000/static/images/utopia.png`

---

### Flujo general de la aplicación

1. **El servidor arranca** con `main.py`, creando una instancia de FastAPI.
2. **Se incluyen los routers** desde la carpeta `routers/`, agrupando la lógica por módulos.
3. **Cada router define endpoints** con sus modelos y dependencias.
4. **Los modelos y esquemas** en `/db` garantizan que los datos tengan la estructura y validación adecuadas.
5. **El cliente de MongoDB** maneja la persistencia de datos real en `users_db.py`.
6. **Los recursos estáticos** se sirven desde la carpeta `/static`.

---

### Claves de esta estructura

- Facilita el mantenimiento y la legibilidad.
- Separa la lógica de negocio (routers) de la persistencia de datos (db).
- Permite escalar fácilmente la aplicación añadiendo nuevos módulos o routers.
- Es compatible con despliegues en la nube, por ejemplo en **Deta** o **Render**.

---

En resumen, esta estructura representa una **base sólida y modular** para cualquier aplicación FastAPI real.  
Cada archivo tiene un propósito claro, y juntos componen una aplicación REST moderna, documentada y lista para escalar.

---

## 3. Primeros pasos con FastAPI [🔝 Volver al inicio](#)

En esta sección aprenderás a crear una aplicación básica con FastAPI, definir tus primeras rutas y probar los endpoints desde el navegador o la documentación interactiva.

---

### Crear la aplicación

Toda app en FastAPI comienza creando una **instancia de la clase `FastAPI`**.  
Esa instancia (`app`) será el núcleo donde se registran las rutas, middlewares, eventos, dependencias, etc.

Ejemplo básico:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "¡Hola FastAPI!"}
```

Guarda este código en un archivo llamado `main.py`.

---

### Ejecutar el servidor

Para arrancar la aplicación puedes usar cualquiera de estos dos comandos:

- `fastapi dev main.py` → ejecuta el servidor en modo desarrollo (recarga automática).
- `uvicorn main:app --reload` → alternativa equivalente usando Uvicorn directamente.

Cuando el servidor arranca, verás un mensaje como:

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Abre tu navegador y visita:

👉 `http://127.0.0.1:8000`  
Deberías ver la respuesta JSON:  
`{"message": "¡Hola FastAPI!"}`

---

### Documentación automática

FastAPI genera automáticamente la documentación de tu API gracias a **OpenAPI**.  
Puedes acceder a dos interfaces diferentes:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
  Permite probar los endpoints directamente desde el navegador.
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
  Ofrece una visualización más orientada a la lectura técnica de la API.

Ambas se generan a partir de los decoradores (`@app.get`, `@app.post`, etc.) y de los **tipos de datos** definidos con Pydantic.

---

### Definir rutas y métodos

FastAPI usa **decoradores** para asociar rutas HTTP a funciones.  
Cada decorador indica el método (GET, POST, PUT, DELETE...) y la ruta.

Ejemplo básico con varios métodos:

```python
@app.get("/items")
async def get_items():
    return ["item1", "item2", "item3"]

@app.post("/items")
async def create_item(item: dict):
    return {"message": "Item creado", "data": item}
```

Puedes usar tipos nativos (`int`, `str`, `dict`) o modelos Pydantic para la validación automática.

---

### Tipado y validación automática

FastAPI valida y convierte automáticamente los tipos de datos gracias a las anotaciones de tipo en Python.  
Por ejemplo:

```python
@app.get("/users/{id}")
async def read_user(id: int):
    return {"user_id": id}
```

Si accedes a `/users/5`, devolverá `{"user_id": 5}`.  
Pero si intentas `/users/abc`, FastAPI devolverá automáticamente un error **422 Unprocessable Entity** porque esperaba un número entero.

---

### Probar endpoints

Puedes probar tus endpoints de tres formas:

1. **Desde la interfaz Swagger UI** (`/docs`)  
   → Ideal para desarrollo y testing rápido.
2. **Desde un cliente HTTP** como Thunder Client, Postman o cURL.
3. **Desde código Python o frontend**, realizando peticiones con `requests` o `fetch`.

---

En resumen:  
Con solo unas pocas líneas puedes tener una API totalmente funcional, documentada y validada automáticamente.  
FastAPI se encarga del resto: documentación, validación de tipos y manejo de errores.

---

## 4. Routers y modularización [🔝 Volver al inicio](#)

A medida que tu aplicación crece, tener todas las rutas dentro de `main.py` se vuelve poco práctico.  
FastAPI ofrece una herramienta muy poderosa para organizar el código: **`APIRouter`**.

Los _routers_ permiten dividir la API en **módulos independientes**, agrupando las rutas por tema o funcionalidad (por ejemplo: usuarios, productos, autenticación, etc.).  
Esto mejora la legibilidad, el mantenimiento y la escalabilidad del proyecto.

---

### Qué es un `APIRouter`

Un `APIRouter` es un objeto que agrupa un conjunto de rutas.  
Cada módulo puede definir su propio router y luego integrarse en la aplicación principal con `include_router()`.

Ejemplo básico:

```python
# routers/products.py
from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
async def get_products():
    return ["Producto 1", "Producto 2", "Producto 3"]
```

Y luego, en el archivo `main.py`, lo incluimos:

```python
from fastapi import FastAPI
from routers import products

app = FastAPI()
app.include_router(products.router)
```

Con esto, el endpoint quedará disponible en:  
👉 `http://127.0.0.1:8000/products`

---

### Ventajas de usar routers

- **Modularidad:** separa cada grupo de rutas por tema (usuarios, productos, auth, etc.).
- **Mantenibilidad:** puedes editar o eliminar un módulo sin afectar al resto.
- **Reutilización:** puedes importar routers en otros proyectos.
- **Documentación organizada:** gracias a `tags`, cada conjunto de rutas aparece agrupado en Swagger UI.

---

### Estructura modular en este proyecto

En este proyecto, todas las rutas están organizadas dentro de la carpeta `/routers`, cada una representando una parte del sistema:

```
routers/
├── users.py
├── products.py
├── basic_auth_users.py
├── jwt_auth_users.py
└── users_db.py
```

Cada archivo define su propio router con un prefijo y etiquetas personalizadas.

Ejemplo tomado de `routers/users.py`:

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"])

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

@router.get("/users")
async def users():
    return [
        User(id=1, name="Pedro", surname="Hdez", url="https://phdez.dev", age=35),
        User(id=2, name="Nazaret", surname="Duque", url="https://duquediazn.dev", age=36)
    ]
```

Y en `main.py` se importa así:

```python
from routers import users, products, basic_auth_users, jwt_auth_users, users_db

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
```

---

### Prefijos, etiquetas y respuestas

Al crear un router puedes definir tres parámetros muy útiles:

```python
router = APIRouter(
    prefix="/products",          # Añade un prefijo común a todas las rutas del módulo
    tags=["products"],           # Agrupa las rutas bajo una misma etiqueta en Swagger
    responses={404: {"message": "No encontrado"}}  # Respuesta personalizada por defecto
)
```

Esto evita repetir código y mantiene las rutas más limpias.

---

### Cómo se combinan en la documentación

Gracias al uso de `tags`, FastAPI organiza automáticamente la documentación en grupos.  
Por ejemplo, verás secciones separadas en `/docs` como:

- **users**
- **products**
- **basicauth**
- **jwtauth**
- **userdb**

Cada grupo corresponde a uno de los routers definidos en la aplicación.

---

### Conclusión

Usar `APIRouter` es una **buena práctica esencial** en FastAPI.  
Permite escalar tu aplicación sin perder claridad, y mantener cada parte del sistema aislada y bien documentada.

En este proyecto:

- Las rutas básicas están en `users.py` y `products.py`.
- Las rutas más avanzadas (autenticación y base de datos) se separan en sus propios routers.
- `main.py` actúa como punto de unión de todos ellos.

---

En la siguiente sección veremos cómo **definir modelos de datos y validarlos con Pydantic**, el corazón de la validación automática en FastAPI.

---

## 5. Modelos y validación con Pydantic [🔝 Volver al inicio](#)

FastAPI utiliza **Pydantic** para manejar la validación y serialización de datos.  
Gracias a los **modelos Pydantic**, podemos definir la estructura de los datos esperados en nuestras peticiones y respuestas, asegurándonos de que cumplen con el formato correcto.

Esto permite:

- Validar automáticamente los datos de entrada (por ejemplo, del cuerpo de una solicitud POST).
- Generar documentación precisa y detallada.
- Convertir los datos en tipos nativos de Python sin esfuerzo.

---

### Qué es un modelo Pydantic

Un **modelo Pydantic** es una clase que hereda de `BaseModel`.  
Cada atributo de la clase representa un campo del modelo con su tipo de dato correspondiente.

Ejemplo tomado de `routers/users.py`:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
```

Con esta simple definición:

- FastAPI valida que cada campo tenga el tipo correcto.
- Si un campo falta o tiene un tipo incorrecto, se devuelve automáticamente un error **422 Unprocessable Entity**.
- En Swagger, la documentación se genera con la estructura exacta del modelo.

---

### Validación automática

FastAPI valida los datos de entrada automáticamente basándose en los tipos definidos.  
Por ejemplo, si esperas un `int` y el cliente envía un `string`, FastAPI genera una respuesta con el error y el detalle del fallo.

Ejemplo de endpoint:

```python
@router.post("/user/", response_model=User, status_code=201)
async def create_user(user: User):
    return user
```

Si envías el siguiente JSON correcto:

```json
{
  "id": 1,
  "name": "Nazaret",
  "surname": "Duque",
  "url": "https://duquediazn.dev",
  "age": 35
}
```

La respuesta será el mismo objeto validado.  
Pero si envías un tipo incorrecto (por ejemplo `"age": "treinta"`), FastAPI devolverá automáticamente:

```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

### Modelos opcionales y anidados

Puedes hacer que ciertos campos sean **opcionales** usando `Optional` del módulo `typing`.  
Esto es muy útil cuando trabajas con bases de datos, ya que los IDs pueden generarse automáticamente.

Ejemplo (desde `db/models/user.py`):

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
```

Aquí, el campo `id` no es obligatorio al crear un usuario, ya que lo genera MongoDB.

---

### Serialización y esquemas

En FastAPI, la **serialización** (convertir datos Python en JSON) también se maneja automáticamente con Pydantic.  
Cuando se devuelven objetos Pydantic desde un endpoint, FastAPI los convierte en JSON de forma automática.

Además, cuando se trabaja con bases de datos, podemos usar funciones auxiliares para transformar los datos antes de devolverlos.  
Ejemplo desde `db/schemas/user.py`:

```python
def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]
```

Estas funciones convierten el formato nativo de MongoDB (`ObjectId`) a tipos compatibles con JSON (`str`).

---

**Alternativa con Pydantic para esquemas de respuesta**

En lugar de usar funciones manuales para transformar los datos, también puedes definir **modelos Pydantic dedicados** para controlar la estructura de los datos devueltos por la API.  
Esto resulta especialmente útil cuando quieres diferenciar entre el modelo que se recibe al crear un recurso (**modelo de entrada**) y el que se devuelve al cliente (**modelo de salida**).

Por ejemplo:

```python
from pydantic import BaseModel
from typing import Optional

# Modelo de entrada (sin ID, porque lo genera la base de datos)
class UserCreate(BaseModel):
    username: str
    email: str

# Modelo de salida (incluye ID generado)
class UserResponse(BaseModel):
    id: str
    username: str
    email: str
```

Y en tu endpoint puedes especificar ambos modelos:

```python
@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    # Guardar en la base de datos...
    return user_creado
```

De esta manera:

- FastAPI valida automáticamente los datos tanto de entrada como de salida.
- Swagger muestra ambos modelos claramente diferenciados.
- Puedes prescindir de las funciones de conversión manual cuando los datos ya tienen el formato adecuado.

---

### Validación + Documentación automática

Cada vez que defines un modelo Pydantic, FastAPI lo usa para:

- Validar automáticamente las entradas y salidas.
- Mostrar en Swagger el esquema de datos esperado en cada endpoint.
- Generar ejemplos de peticiones y respuestas sin esfuerzo adicional.

Esto hace que tu API esté **autodocumentada** y sea **segura por diseño**.

---

### En resumen

- Usa `BaseModel` para definir la estructura de tus datos.
- Añade tipos de Python (`str`, `int`, `bool`, `list`, etc.) para activar la validación automática.
- Usa `Optional` para campos no obligatorios.
- Aprovecha las funciones de esquema (`schemas`) para adaptar los datos a tus respuestas JSON.
- La documentación en `/docs` se genera automáticamente según tus modelos.

---

En la siguiente sección implementaremos estas validaciones en acción, viendo cómo construir un **CRUD completo (Create, Read, Update, Delete)** con FastAPI.

---

## 6. Operaciones CRUD [🔝 Volver al inicio](#)

Las operaciones **CRUD** (Create, Read, Update, Delete) son la base de cualquier API REST.  
FastAPI facilita enormemente su implementación, gracias a la validación automática de datos, las respuestas tipadas y la documentación integrada.

En esta sección veremos cómo construir endpoints CRUD usando **Pydantic** y listas locales (sin base de datos), y más adelante aplicaremos el mismo patrón con **MongoDB**.

---

### Estructura CRUD básica

Cada operación CRUD corresponde a un método HTTP:

| Operación | Método | Descripción                    | Código de estado |
| --------- | ------ | ------------------------------ | ---------------- |
| Create    | POST   | Crear un nuevo recurso         | 201 Created      |
| Read      | GET    | Obtener uno o varios recursos  | 200 OK           |
| Update    | PUT    | Modificar un recurso existente | 200 OK           |
| Delete    | DELETE | Eliminar un recurso existente  | 204 No Content   |

---

### Ejemplo completo — CRUD de usuarios

El archivo `routers/users.py` incluye un ejemplo didáctico con todas las operaciones CRUD sobre una lista de usuarios.

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"])

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Base de datos simulada
users_list = [
    User(id=1, name="Pedro", surname="Hdez", url="https://phdex.dev", age=35),
    User(id=2, name="Nazaret", surname="Duque", url="https://duquediazn.dev", age=36),
    User(id=3, name="Darth", surname="Vader", url="https://darkside.dev", age=100)
]
```

---

### READ — Consultar datos

FastAPI permite capturar parámetros tanto desde la **ruta (path)** como desde la **query (URL)**.

Por ejemplo:

```python
# Obtener usuario por ID en la ruta
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Obtener usuario por ID como parámetro de consulta
@router.get("/user/")
async def user(id: int):
    return search_user(id)
```

La función auxiliar `search_user()` filtra la lista:

```python
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

---

### CREATE — Crear datos

Para crear un nuevo usuario usamos el método **POST**.  
FastAPI convierte automáticamente el cuerpo JSON en una instancia del modelo `User`.

```python
@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=422, detail="El usuario ya existe")
    users_list.append(user)
    return user
```

Si el usuario ya existe, se lanza una excepción HTTP con código 422 y un mensaje personalizado.

---

### UPDATE — Modificar datos

El método **PUT** permite reemplazar un usuario existente.  
Podemos buscar el usuario por ID y actualizarlo si existe.

```python
@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user
```

---

### DELETE — Eliminar datos

Para eliminar un recurso usamos el método **DELETE**.  
Aquí eliminamos un usuario de la lista según su ID.

```python
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    return {"success": "Usuario eliminado correctamente."}
```

---

### Manejo de errores con `HTTPException`

`HTTPException` es una herramienta de FastAPI que permite devolver errores personalizados con su código y mensaje.  
Se usa comúnmente para validar entradas o manejar casos donde el recurso no existe.

Ejemplo:

```python
if not user_found:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
```

Esto genera automáticamente una respuesta JSON como:

```json
{
  "detail": "Usuario no encontrado"
}
```

---

### Buenas prácticas CRUD

- Usa `response_model` para definir claramente lo que devuelve cada endpoint.
- Usa `status_code` para indicar correctamente el resultado (201, 200, 404, etc.).
- Lanza `HTTPException` en lugar de devolver diccionarios de error.
- Mantén funciones auxiliares separadas para la lógica de búsqueda o validación.
- Cuando uses bases de datos reales, recuerda usar identificadores únicos como `_id` o `uuid`.

---

En la siguiente sección veremos cómo añadir **autenticación** a nuestra API, empezando por un esquema **básico con OAuth2**.

---

## 7. Autenticación básica (OAuth2 Password) [🔝 Volver al inicio](#)

La autenticación es un paso esencial en cualquier API.  
FastAPI proporciona herramientas integradas para implementar **OAuth2**, un estándar ampliamente usado para gestionar la autenticación mediante **tokens de acceso (access tokens)**.

En esta sección veremos una implementación **básica de autenticación OAuth2 Password** usando el router `basic_auth_users.py`.  
Esta versión no cifra contraseñas ni genera tokens JWT — se usa principalmente para entender cómo funciona el flujo y las dependencias (`Depends`).

---

### Qué es OAuth2 Password

OAuth2 es un estándar que define cómo los clientes (aplicaciones, usuarios) pueden autenticarse y obtener acceso a recursos protegidos mediante **tokens**.  
El flujo “Password” implica que el usuario envía su **nombre de usuario** y **contraseña**, y el servidor devuelve un token que luego se utiliza para acceder a rutas protegidas.

---

### Estructura del router

Archivo: `routers/basic_auth_users.py`

Este módulo incluye:

- Un diccionario que simula una base de datos de usuarios.
- Modelos `User` y `UserDB` definidos con Pydantic.
- Funciones auxiliares para buscar usuarios.
- Endpoints para **login** y para obtener el **usuario autenticado**.

---

### Dependencias y esquema de seguridad

FastAPI implementa OAuth2 mediante el esquema `OAuth2PasswordBearer`.  
Este objeto indica que la API espera un token de autenticación en el encabezado HTTP `Authorization`.

```python
from fastapi.security import OAuth2PasswordBearer

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
```

Con esto, FastAPI:

- Añade un campo de autenticación en Swagger UI.
- Permite que el endpoint de login genere el token.
- Inyecta automáticamente el valor del token en las rutas protegidas.

---

### Modelos de usuario

```python
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str
```

- `User` → modelo público sin contraseña.
- `UserDB` → modelo interno que incluye el campo `password`.

---

### Base de datos simulada

```python
users_db = {
    "duquediazn": {
        "username": "duquediazn",
        "full_name": "Nazaret Duque",
        "email": "duquediazn@duquedev.com",
        "disabled": False,
        "password": "123456"
    },
    "duquediazn2": {
        "username": "duquediazn2",
        "full_name": "Nazaret Duque 2",
        "email": "duquediazn2@duquedev.com",
        "disabled": True,
        "password": "654321"
    }
}
```

Esta base de datos simulada sirve solo para pruebas, ya que las contraseñas se almacenan en texto plano.

---

### Endpoint de login

```python
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}
```

Aquí:

- Se reciben `username` y `password` desde un formulario.
- Se valida la existencia del usuario y la coincidencia de la contraseña.
- Si todo es correcto, se devuelve un **token** (el nombre de usuario).

Este token se usará para acceder a rutas protegidas.

---

### Dependencia `current_user`

```python
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return user
```

Esta función se inyecta como dependencia en cualquier ruta que requiera autenticación.  
FastAPI se encarga de extraer el token del encabezado y pasarlo automáticamente como parámetro.

---

### Endpoint protegido `/users/me`

```python
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
```

Este endpoint devuelve la información del usuario actual, siempre que esté autenticado.  
Si el token es inválido o el usuario está deshabilitado, se lanzará una excepción HTTP.

---

### Cómo probarlo

1. Accede a la documentación Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Busca el grupo **basicauth**.
3. Ejecuta el endpoint `/basicauth/login` con las credenciales de un usuario válido (por ejemplo: _duquediazn / 123456_).
4. Copia el token devuelto (el nombre de usuario).
5. Haz clic en el botón **Authorize** y pega el token como `Bearer <token>`.
6. Prueba el endpoint `/basicauth/users/me` para obtener los datos del usuario autenticado.

---

### Limitaciones de este enfoque

- Las contraseñas no están cifradas.
- El token no tiene expiración ni verificación real.
- Cualquiera que conozca un nombre de usuario válido podría autenticarse.

Por eso, en la siguiente sección implementaremos una versión más robusta:  
**autenticación con JWT (JSON Web Tokens)**, donde las contraseñas se cifran y los tokens tienen fecha de expiración.

---

## 8. Autenticación con JWT (JSON Web Tokens) [🔝 Volver al inicio](#)

En esta sección aprenderás a implementar un sistema de **autenticación con JWT (JSON Web Tokens)** en FastAPI, basado en el archivo `routers/jwt_auth_users.py`.  
Este método mejora la seguridad respecto al ejemplo anterior (autenticación básica), ya que:

- Las contraseñas se almacenan **cifradas**.
- Los tokens de acceso tienen **tiempo de expiración**.
- Se valida la autenticidad del token antes de conceder acceso.

---

### Qué es un JWT

Un **JSON Web Token (JWT)** es un estándar abierto (RFC 7519) para transmitir información entre partes de forma segura.  
Está compuesto por tres partes separadas por puntos:

```
header.payload.signature
```

- **Header**: indica el algoritmo de cifrado (por ejemplo, HS256).
- **Payload**: contiene los datos (claims), como el usuario o la expiración.
- **Signature**: asegura que el token no ha sido alterado.

Ejemplo visual de un JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.eyJzdWIiOiJicmFpcyIsImV4cCI6MTcxOTM3MjY1OX0
.DCOb6qfV9MzQZ7p7C7vHLUcmTXvDPg8lGZT7Ay7i7xE
```

---

### Dependencias necesarias

Para trabajar con JWT y contraseñas cifradas, instalamos dos librerías adicionales:

```
pip install pyjwt
pip install "passlib[bcrypt]"
```

- **PyJWT** → para crear y validar tokens.
- **Passlib** → para cifrar contraseñas de forma segura con el algoritmo bcrypt.

---

### Configuración del router

Archivo: `routers/jwt_auth_users.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
```

Variables principales:

```python
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1  # en minutos
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"
```

---

### Cifrado de contraseñas

FastAPI no cifra contraseñas por sí mismo, pero podemos hacerlo fácilmente con Passlib:

```python
crypt = CryptContext(schemes=["bcrypt"])
```

Luego, las contraseñas guardadas en la base de datos se almacenan así:

```python
"password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6"
```

(que corresponde al hash de `"123456"`).

Para verificar una contraseña ingresada:

```python
crypt.verify(form.password, user.password)
```

---

### Funciones de búsqueda y autenticación

```python
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
```

Para autenticar al usuario mediante el token:

```python
async def auth_user(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except InvalidTokenError:
        raise exception
    return search_user(username)
```

> El operador `**` en Python se llama desempaquetado de diccionarios (dictionary unpacking) y se utiliza para descomponer las claves y valores de un diccionario como argumentos de palabra clave (keyword arguments) en una función o constructor. Es similar a `expand/rest (...)` en JS.

---

### Generación del token de acceso

El endpoint `/jwtauth/login` genera un token JWT con un tiempo de expiración definido:

```python
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")

    access_token = {
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }

    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }
```

💡 **Importante:** el campo `"sub"` (subject) almacena el nombre de usuario y `"exp"` define la fecha de expiración del token.

---

### Verificación del usuario autenticado

El token se valida automáticamente al llamar a rutas protegidas.  
La dependencia `current_user` comprueba que el token sea válido y que el usuario esté activo.

```python
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return user
```

---

### Endpoint protegido `/users/me`

```python
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
```

Si el token es válido, devuelve los datos del usuario autenticado.  
Si no, se lanza una excepción **401 Unauthorized**.

---

### Cómo probarlo en Swagger

1. Ir a: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Abrir la sección **jwtauth**.
3. Ejecutar `/jwtauth/login` con:
   - username: `nazadev`
   - password: `123456`
4. Copiar el token devuelto.
5. Pulsar **Authorize** y pegarlo como: `Bearer <token>`.
6. Ejecutar `/jwtauth/users/me` → debe devolver el perfil del usuario autenticado.
7. Esperar más de 1 minuto y volver a intentarlo → el token habrá expirado.

---

### Diferencias clave con la autenticación básica

| Característica       | BasicAuth       | JWTAuth    |
| -------------------- | --------------- | ---------- |
| Contraseñas cifradas | ❌ No           | ✅ Sí      |
| Expiración de token  | ❌ No           | ✅ Sí      |
| Validación de firma  | ❌ No           | ✅ Sí      |
| Seguridad real       | Baja            | Alta       |
| Uso recomendado      | Pruebas / demos | Producción |

---

### En resumen

- FastAPI facilita la integración de JWT con PyJWT.
- Passlib permite cifrar y verificar contraseñas de forma segura.
- Los tokens pueden configurarse con expiración y campos personalizados.
- Es la forma recomendada de manejar autenticación en aplicaciones reales.

---

En la siguiente sección conectaremos nuestra API a una **base de datos MongoDB** para gestionar usuarios reales con persistencia de datos.

---

## 9. Conexión a MongoDB [🔝 Volver al inicio](#)

En esta sección integramos la API con **MongoDB** para tener persistencia real de datos. Veremos cómo configurar el cliente con `pymongo`, cómo modelar y **serializar** documentos, y cómo exponer **CRUD** completos en el router `users_db.py`.

---

### Requisitos e instalación

- Base de datos local: instala **MongoDB Community** y arráncala en tu equipo.
- Base de datos en la nube: crea un clúster en **MongoDB Atlas**.

Instala el driver de Python:

```
pip install pymongo
```

---

### Cliente de MongoDB (`db/client.py`)

Este archivo centraliza la conexión a la base de datos. Incluye dos opciones (local y Atlas):

```python
from pymongo import MongoClient
from dotenv import load_dotenv
import os

### Base de datos local MongoDB ###
# db_client = MongoClient().local

### Base de datos remota MongoDB Atlas (https://mongodb.com) ###
# Cargar variables del archivo .env
load_dotenv()

# Leer configuración del entorno
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")

# Inicializar el cliente y la base de datos
db_client = MongoClient(MONGODB_URI)[MONGODB_DB]

```

**Buenas prácticas recomendadas**

- No subas credenciales al repositorio. Usa variables de entorno:
  - `MONGODB_URI` (cadena de conexión)
  - `MONGODB_DB` (nombre de la base de datos)
- Usa `python-dotenv` o el sistema de configuración de tu framework para cargar variables.
- Define un **TTL** o índices cuando proceda (por ejemplo, para tokens o campos únicos como `email`).

Para que el código anterior funcione deberás crear un `.env` en la raíz del proyecto y añadir tus credenciales de MongoDB Atlas tal que así:

```
MONGODB_URI=mongodb+srv://TU_URI
MONGODB_DB=TU_DB
```

---

### Modelo de datos (`db/models/user.py`)

El **modelo Pydantic** de la entidad usuario valida la entrada/salida a nivel de API:

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
```

- `id` es opcional porque **MongoDB genera `_id`** automáticamente.
- `username` y `email` son obligatorios.

---

### Serialización (schemas) (`db/schemas/user.py`)

MongoDB usa `ObjectId` para `_id`, que **no es JSON serializable**. Este módulo convierte documentos de MongoDB a respuestas aptas para la API:

```python
def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]
```

- Convierte `_id` → `id: str`
- Selecciona y estandariza los campos de salida.

> Alternativa: también puedes usar **modelos Pydantic de respuesta** (p. ej. `UserResponse`) como se explicó en la sección 5 para evitar funciones manuales cuando el formato de salida ya es compatible.

---

### 🚦 Router CRUD real (`routers/users_db.py`)

Este router implementa un CRUD completo contra MongoDB con `pymongo` y utiliza los **schemas** para serializar.

**Prefijo y metadatos**

```python
router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)
```

**Listar usuarios**

```python
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())
```

- Recupera todo con `find()` y serializa con `users_schema`.
- Declara `response_model=list[User]` para documentación y validación de salida.

**Obtener por id (Path y Query)**

```python
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.get("/")
async def user(id: str):
    return search_user("_id", ObjectId(id))
```

- Acepta `id` tanto en **ruta** como en **query**.
- Usa `bson.ObjectId(id)` para buscar por `_id`.

**Crear usuario**

```python
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]  # lo genera Mongo
    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)
```

- Verifica duplicados por **email** antes de insertar.
- Elimina `id` del payload (Mongo genera `_id`).
- Devuelve el recurso creado con `201 Created`.

**Actualizar usuario**

```python
@router.put("/", response_model=User)
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    return search_user("_id", ObjectId(user.id))
```

- Reemplaza el documento completo. Devuelve el estado actual del recurso.

**Eliminar usuario**

```python
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error": "No se ha eliminado el usuario"}
```

- Elimina por `_id`.
- Usa `204 No Content`. **Nota**: con 204 no debe devolverse cuerpo; si quieres un mensaje, usa `200` o `202`.

**Búsqueda auxiliar**

```python
def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}
```

---

### Probar el flujo completo

1. Arranca el servidor:
   - `fastapi dev main.py`  
     o `uvicorn main:app --reload`
2. Ve a **Swagger UI**: `http://127.0.0.1:8000/docs`
3. En el grupo **userdb**:
   - `POST /userdb/` → crea un usuario `{ "username": "...", "email": "..." }`
   - `GET /userdb/` → lista todos
   - `GET /userdb/{id}` → recupera uno
   - `PUT /userdb/` → actualiza (incluye `id`)
   - `DELETE /userdb/{id}` → elimina por id

---

### Buenas prácticas y mejoras

- **Índices y unicidad**: crea un índice único en `email` para evitar duplicados a nivel de base de datos.
- **Validación de entrada/salida**: usa `response_model` y, si procede, **modelos separados** (`UserCreate`, `UserUpdate`, `UserResponse`).
- **Errores consistentes**: en lugar de devolver diccionarios con `{ "error": ... }`, usa `HTTPException` con códigos apropiados (`404`, `409`, `400`).
- **Conversión de tipos**: valida `ObjectId` y gestiona `InvalidId` para IDs mal formados.
- **Seguridad**: protege estos endpoints con autenticación (por ejemplo, JWT de la sección 8) si manejan datos sensibles.
- **Configuración**: mueve URIs y nombres de DB a variables de entorno; evita credenciales en el código.
- **Transacciones/consistencia**: para operaciones múltiples, considera transacciones en clústeres que lo soporten.

---

Con esto, tu API ya cuenta con **persistencia real** usando MongoDB y un **CRUD completo** y tipado. En la siguiente sección veremos cómo **servir recursos estáticos** (imágenes, CSS, JS) con FastAPI.

---

## 10. Recursos estáticos [🔝 Volver al inicio](#)

FastAPI (vía **Starlette**) permite servir archivos estáticos como imágenes, CSS, JS o fuentes. Esto es útil para exponer recursos públicos que tu frontend o documentación necesiten consumir directamente desde la API.

---

### Montaje de la carpeta estática

En este proyecto, los estáticos se exponen montando un directorio en una **ruta pública**:

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
```

- `"/static"` es el **prefijo de URL** bajo el que se servirán los archivos.
- `directory="static"` apunta a la carpeta local del repositorio.
- `name="static"` registra el subapp para referencia interna.

**Ejemplo incluido en el repo**

- Archivo: `static/images/utopia.png`
- URL pública: `http://127.0.0.1:8000/static/images/utopia.png`

Estructura mínima:

```
static/
└── images/
    └── utopia.png
```

---

### Cómo referenciar los archivos

- Desde HTML: `<img src="/static/images/utopia.png" alt="Utopia" />`
- Desde CSS: `background-image: url('/static/images/utopia.png');`
- Desde JS o un cliente HTTP: `fetch('/static/config.json')`

> Consejo: usa rutas **relativas** (`/static/...`) para evitar problemas entre entornos.

---

### Opciones y comportamiento

- **Cacheo**: los servidores intermedios y navegadores suelen cachear estáticos. Versiona tus ficheros (por ejemplo `app.3c1f.js`) si actualizas con frecuencia.
- **Tipos MIME**: se infieren por extensión (png, jpg, svg, css, js, woff2, etc.).
- **Errores 404**: si un archivo no existe, se devolverá un 404 con el detalle correspondiente.
- **Subaplicación**: `StaticFiles` es una “app” ASGI montada dentro de tu aplicación principal.

---

### Buenas prácticas

- **Organiza por tipo**: `static/images`, `static/css`, `static/js`, `static/fonts` para mayor claridad.
- **No mezcles secretos**: nunca coloques credenciales o archivos sensibles en `static/`; todo lo que haya ahí es **público**.
- **Versiona y minimiza**: para producción, usa nombres con hash y minimiza CSS/JS si sirves frontend estático.
- **CDN**: si esperas alto tráfico o archivos pesados, considera servir los estáticos desde un **CDN** o un bucket (S3, etc.) y deja a FastAPI solo la lógica de API.

---

### Comprobación rápida

1. Arranca el servidor: `fastapi dev main.py` (o `uvicorn main:app --reload`).
2. Abre en el navegador: `http://127.0.0.1:8000/static/images/utopia.png`.
3. Deberías ver la imagen servida por la API.

---

Con esto ya puedes exponer cualquier recurso estático necesario (imágenes, estilos, scripts) desde tu API. En la siguiente sección cerraremos con **buenas prácticas, mejoras y próximos pasos** para llevar tu API a producción con calidad.

---

## 11. Buenas prácticas y próximos pasos [🔝 Volver al inicio](#)

Esta sección recopila recomendaciones para que tu API con FastAPI sea **mantenible, segura y lista para producción**. Incluye checklist, patrones de arquitectura, testing, seguridad, observabilidad y despliegue.

---

### Checklist rápido (mínimos recomendados)

- Definir `response_model` en endpoints y usar modelos de **entrada/salida** (DTOs) separados.
- Usar `HTTPException` con **códigos correctos** (201/200/204/400/401/403/404/409/422/500).
- Centralizar **configuración** (variables de entorno) y **secrets** (no en el repo).
- Activar **CORS** solo para orígenes permitidos.
- **Hashear contraseñas** (bcrypt/argon2) y tokens con **expiración** (JWT).
- Validar **IDs** (p. ej., `ObjectId`) y sanitizar entrada.
- Añadir **tests** (unitarios/integ) y **lint/format** (ruff/black, pre-commit).
- Logging estructurado, **healthchecks**, **tracing** y **monitorización**.
- Documentación OpenAPI clara con **tags**, ejemplos y descripciones.

---

### Arquitectura y organización

- **Separación por capas**:
  - `routers/` (interfaces HTTP, validación inicial)
  - `schemas/` o `models/` Pydantic para **DTOs** (entrada/salida)
  - `services/` (lógica de negocio, casos de uso)
  - `repositories/` o `db/` (acceso a datos; POA o patrón repositorio)
  - `core/config.py` (settings), `core/security.py` (JWT, hash), `core/errors.py` (excepciones)
- **Routers** por dominio (`users`, `products`, `auth`, …) con `prefix` y `tags`.
- **Versionado**: exponer `/api/v1/...` y planificar `/api/v2` para cambios breaking.

---

### Configuración y entorno

- Cargar settings desde **variables de entorno** (y opcional `.env`) con un objeto de configuración (por ejemplo, `BaseSettings`).
- Definir claves: `MONGODB_URI`, `MONGODB_DB`, `JWT_SECRET`, `JWT_EXPIRES_MINUTES`, `ENV`, `DEBUG`.
- Diferenciar **dev / staging / prod** con overrides de configuración.

---

### Seguridad

- **CORS**: habilitar sólo orígenes necesarios.
- **JWT**:
  - Usar `sub`, `exp`, y si aplica `aud`/`iss`.
  - Añadir **refresh tokens** (vida larga) + **access tokens** (vida corta).
- **Contraseñas**: hash con `passlib` (bcrypt/argon2), nunca en texto plano.
- **Autorización**: dependencias con **roles/permissions** (p. ej., `Depends(require_role("admin"))`).
- **Headers seguros**: considerar middlewares/cabeceras (`X-Content-Type-Options`, `X-Frame-Options`, `Content-Security-Policy` si sirves HTML).
- **Rate limiting**: bibliotecas tipo slowapi/redis para limitar peticiones.
- **Validación**: sanitizar entrada, controlar tamaños (payloads, arrays), y rechazar IDs inválidos.
- **Errores**: no exponer detalles internos en producción; usar manejadores globales.

---

### Datos y persistencia

- **MongoDB**:
  - Índices (único en `email`), TTL si aplica, y proyecciones para minimizar payload.
  - Manejar `ObjectId` inválido y no found → `400/404`.
  - Si necesitas ODM: considerar Motor (async) o Beanie (ODM sobre Motor).
- **SQL** (si migras): usar SQLAlchemy + Alembic (migraciones).
- **Pydantic en respuestas**: modelos específicos de salida (`UserResponse`) para ocultar campos sensibles.
- **Paginación/filtrado/ordenación** en listados (query params: `page`, `limit`, `sort`, `q`).

---

### Validación y documentación

- **Pydantic**: validadores, `constr`, `EmailStr`, `Field(..., example=...)`.
- **OpenAPI**:
  - `tags`, `summary`, `description`, `responses`, `response_model_exclude_unset`.
  - **Ejemplos** en request/response para mejorar `/docs`.
- **Mensajes de error** consistentes y localizables si es necesario.

---

### Testing y calidad

- **Tests**: `pytest` con `TestClient`/`httpx` (sincrónico/async).
- **Fixtures**: base de datos fake o **test database**; datos semilla para pruebas.
- **Mocks** de capa externa (correo, pagos, terceros).
- **Cobertura** mínima (p. ej. 80%).
- **CI**: GitHub Actions (lint, type-check opcional con mypy, tests).
- **Pre-commit**: hooks para `ruff`, `black`, trailing whitespace, end-of-file-fixer.

---

### Rendimiento y producción

- **Servidor**: `uvicorn` detrás de **gunicorn/uvicorn workers** o en plataforma gestionada.
- **Concurrencia**: preferir drivers **async** (Motor para Mongo) en rutas `async`.
- **Conexiones**: pools, tiempo de espera, reintentos y backoff.
- **Compresión**: GZip/Brotli si retornas cargas grandes.
- **Caching**: Redis para caché de consultas costosas; **ETag** y **Cache-Control** donde aplique.
- **Tareas en background**: `BackgroundTasks` o colas (Celery/RQ) para trabajos diferidos (emails, informes).
- **Eventos de ciclo de vida**: `lifespan`/`startup`/`shutdown` para abrir/cerrar conexiones.
- **Health checks**: `/health` o `/live` y `/ready` para orquestadores.

---

### Observabilidad

- **Logging** estructurado (JSON) con niveles por entorno.
- **Trazas** (OpenTelemetry) + **métricas** (Prometheus/Grafana).
- **Errores**: captura con Sentry o similar (PII off en producción).

---

### Despliegue

- **Contenedores**: Docker multi-stage, imagen mínima, variables por entorno, `read-only fs` si posible.
- **Plataformas**: Deta, Render, Railway, Fly.io, u orquestación en Kubernetes.
- **Serverless**: si optas por ello, revisar tiempos de arranque y límites de frío.
- **CDN** para estáticos pesados; la API sólo para JSON.

---

### Próximos pasos para este proyecto

- Proteger `users_db` con **JWT** (sección 8) y roles.
- Introducir **modelos de entrada/salida** (p. ej., `UserCreate`, `UserUpdate`, `UserResponse`) en `users_db`.
- Añadir **paginación** en `GET /userdb/`.
- Sustituir `find_one_and_replace` por updates parciales si procede.
- Crear **tests** de integración para `users_db` y un contenedor Mongo en CI.
- Añadir **índice único** en `email` y devolver `409 Conflict` en duplicados.
- Implementar **rate limiting** en `/login` y endpoints sensibles.

---

Con estas prácticas llevarás tu API FastAPI del estado didáctico a un entorno **robusto y productivo**, manteniendo código limpio, seguridad razonable y una base sólida para escalar y evolucionar.

---

## 🔗 Navegación

⬅️ [Lección anterior](./intermediate.md) | [Volver al índice principal](../README.md)
