### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Endpoint para obtener todos los usuarios
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

# Endpoint para obtener un usuario por ID a través de la ruta
@router.get("/{id}")  # Path
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Endpoint para obtener un usuario por ID a través de una consulta (query)
@router.get("/")  # Query
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Endpoint para crear un nuevo usuario
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    # Verifica si el usuario ya existe en la base de datos
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"] #Mongo genera su propio ID

    # Inserta el nuevo usuario en la base de datos y obtiene su ID
    id = db_client.users.insert_one(user_dict).inserted_id

    # Busca el usuario recién creado y lo devuelve
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

# Endpoint para actualizar un usuario existente
@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        # Reemplaza el usuario en la base de datos
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))

# Endpoint para eliminar un usuario por ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Función auxiliar para buscar un usuario en la base de datos por un campo específico
def search_user(field: str, key):

    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}