#Entidad user
from fastapi import APIRouter, HTTPException 
from pydantic import BaseModel

'''
El enrutado (routing) en el contexto de una API se refiere al proceso de mapear las solicitudes (requests) 
que llegan a la API a funciones específicas o manejadores de esos eventos. Básicamente, cuando una solicitud HTTP 
es enviada a la API, el "enrutador" es el encargado de identificar cuál es la función o método que debe ejecutar 
para esa solicitud, dependiendo de factores como el método HTTP (GET, POST, PUT, DELETE, etc.), la URL solicitada 
y otros parámetros. Así, en lugar de tener todo el enrutamiento en un solo archivo, puedes dividir las rutas en 
diferentes módulos o archivos, mejorando la legibilidad y mantenibilidad del código.
'''

 #  APIRouter ayuda a gestionar el enrutado dentro de una API. 
router = APIRouter(tags=["users"]) # Con "tags", conseguimos agrupar en la documentación los distintos enrutados de la API. 

#Con BaseModel vamos a poder crear una entidad de manera más sencilla:
# Hacemos que en nuestra difinición de la clase, esta herede de BaseModel pasándola como parametro. Conseguimos:
# Validación Automática de los tipos de datos.
# Conversión de tipos.
# Documentación automática.
# Facilidad de serialización. 

class User(BaseModel): 
    id: int
    name: str
    surname: str
    url: str
    age: int

# FastAPI/Pydantic generará un constructor como este implícitamente:
'''
class User:
    def __init__(self, id: int, name: str, surname: str, url: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.url = url
        self.age = age

'''

@router.get("/userclass")
async def userclass():
       return User(id=1, name="Nazaret", surname="Duque", url="https://duquediazn.dev", age=35) #Crea el objeto y en la respuesta tendremos un json con los datos (lo hace BaseModel)

'''
Respuesta: 
{
  "id":1,
  "name": "Nazaret",
  "surname": "Duque",
  "url": "https://duquediazn.dev",
  "age": 35
}
'''

#Definimos una lista de usuarios: 
users_list=[User(id=1, name="Pedro", surname="Hdez", url="https://phdez.dev", age=35),
           User(id=2, name="Nazaret", surname="Duque", url="https://duquediazn.dev", age=36),
           User(id=3, name="Darth", surname="Vader", url="https://darkside.dev", age=100)]

@router.get("/users")
async def users():
       return users_list

'''
Respuesta: 
[
  {
    "id":1,
    "name": "Pedro",
    "surname": "Hdez",
    "url": "https://phdez.dev",
    "age": 35
  },
  {
    "id":2,
    "name": "Nazaret",
    "surname": "Duque",
    "url": "https://duquediazn.dev",
    "age": 36
  },
  {
    "id":3,
    "name": "Darth",
    "surname": "Vader",
    "url": "https://darkside.dev",
    "age": 100
  }
]
'''

#Parámetros en el path:
@router.get("/user/{id}") #http://127.0.0.1:8000/users/1
async def user(id: int): #Tipado del parámetro
    return search_user(id)
    

#Parámetros por query:
@router.get("/user/") #http://127.0.0.1:8000/user/?id=2
async def user(id: int): 
    return search_user(id)
    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
          return list(users)[0]
    except:
          return {"error":"No se ha encontrado el usuario"}
    

'''
Recuerda: 
- POST: para crear datos
- GET: para leer datos
- PUT: para actualizar datos
- DELETE: para borrar datos
'''

#POST:
# Definimos status_code si queremos que devuelva un HTTP Status Code diferente y 
# response_model para indicar qué tipo de dato devuelve
@router.post("/user/", response_model= User, status_code=201)  # http://127.0.0.1:8000/user/
async def user(user: User): 
  if type(search_user(user.id)) == User:
    # Podemos especificar un HTTP Status Code en el caso de error al intentar crear el usuario. 
    raise HTTPException(status_code=422, detail="El usuario ya existe") # "raise" es como un return para excepciones
  else:
    users_list.append(user)
    return user
  
# HTTP Status Code: https://developer.mozilla.org/es/docs/Web/HTTP/Status

#PUT:
@router.put("/user/")
async def user(user: User):

  found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      found = True

  if not found:
    return {"error":"No se ha actualizado el usuario"}
  else:
    return user


#DELETE:
@router.delete("/user/{id}")
async def user(id: int):

  found = False  

  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
     #del_user=saved_user
     del users_list[index]
     #users_list.remove(saved_user)
     found = True

  if not found:
    return {"error": "No se ha eliminado el usuario"}
  else: 
    return {"succes": "Usuario eliminado correctamente."}
    #return del_user


