#Doc oficial FastAPI: https://fastapi.tiangolo.com/

#Instalar la API: pip install "fastapi[all]" | En Windows: py -m pip install "fastapi[all]

from fastapi import FastAPI
from routers import users, products, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles 

app = FastAPI() #Instancia de FastAPI. Con ella definimos las rutas, etc.

# Routers:
app.include_router(users.router) # Así incluímos los enrutadores 
app.include_router(products.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

# Recursos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
# Podemos acceder a: http://127.0.0.1:8000/static/images/utopia.png

@app.get("/") #Define una ruta HTTP GET asociadia a la ruta raíz (root): localhost:puerto |  http://127.0.0.1:8000
async def root(): #La función manejadora root se define asíncrona
        return "¡Hola FastApi!"

#Arrancar servidor: fastapi dev nombre_archivo.py | Windows: py -m fastapi dev nombre_archivo.py || uvicorn app.main:app --reload
#FastAPI nos indicará la dirección en la que se ha iniciado el servidor: http://127.0.0.1:8000

@app.get("/url")  # http://127.0.0.1:8000/url
async def url(): 
        return {"url":" https://fastapi.tiangolo.com/"}

#Documentación interactiva de la API: http://127.0.0.1:8000/docs (Swagger UI)
#Alternativa:  http://127.0.0.1:8000/redoc (ReDoc)

#Con la extensión: Thunder Client, podemos probar peticiones (similar a Postman pero integrado en VS Code)
