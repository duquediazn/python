from fastapi import APIRouter, Depends, HTTPException, status
# Depends: Mecanismo de FastAPI para inyección de dependencias. 
# Permite incluir funciones o clases que deben ejecutarse antes de llamar a una ruta.
# status: Contiene constantes con códigos de estado HTTP.
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Módulo de autenticación
# OAuth2PasswordBearer: define el esquema de autenticación
# OAuth2PasswordRequestForm: maneja los datos del formulario de login.

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# OAuth2PasswordBearer: Define el esquema de autenticación. 
# Indica que los usuarios deben enviar un token de acceso como parte de las peticiones HTTP.
# tokenUrl="basicauth/login": Especifica la URL que manejará la autenticación. 
# En este caso, está asociada al endpoint /basicauth/login.
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

#UserDB: Extiende User y agrega un campo password. Este modelo representa cómo se almacenan 
# los datos en la base de datos (o un diccionario en este caso).
class UserDB(User):
    password: str

# Diccionario que simula una base de datos. 
# Cada clave es un username y los valores son las propiedades del usuario.
users_db = {
    "mouredev": {
        "username": "nazadev",
        "full_name": "Nazaret Duque",
        "email": "duquediazn@nazadev.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "nazadev2",
        "full_name": "Nazaria Díaz",
        "email": "duquediazn@nazadev2.com",
        "disabled": True,
        "password": "654321"
    }
}

# Funciones auxiliares: 

# Busca un usuario en la base de datos (simulada) por username.
# Si lo encuentra, devuelve un objeto UserDB.
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
        # El operador ** en Python se llama desempaquetado de diccionarios (dictionary unpacking) 
        # y se utiliza para descomponer las claves y valores de un diccionario como argumentos de 
        # palabra clave (keyword arguments) en una función o constructor. Similar a expand/rest (...) en JS.

# Similar a search_user_db, pero devuelve un objeto User, omitiendo la contraseña.
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# Dependencia: Usuario acutual.
# token: str = Depends(oauth2): Extrae el token enviado en la cabecera Authorization.
# Busca el usuario asociado al token.
# Si no encuentra el usuario o si está deshabilitado, lanza excepciones con los códigos de error correspondientes.
# Si todo es válido, devuelve el usuario actual.
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user

# Endpoints:
# Login: 
# Endpoint POST en /basicauth/login. 
# Extrae username y password del formulario de autenticación. 
# Valida las credenciales contra la base de datos. 
# Si son correctas, devuelve un token (el nombre de usuario) y el tipo de token (bearer).
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username) #.get() sobre un diccionario equivale a dict["key"]
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}

# Usuario actual 
# Endpoint GET en /basicauth/users/me:
# Utiliza la dependencia current_user para obtener al usuario autenticado.
# Devuelve los datos del usuario.
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user