from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# JWT means "JSON Web Tokens".It's a standard to codify a JSON object in a long dense string without spaces.
# Debemos instalar: 
# pip install pyjwt
# pip install "passlib[bcrypt]"
import jwt #https://jwt.io/
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext # passLib is a great Python package to handle password hashes
from datetime import datetime, timezone, timedelta 

ALGORITHM = "HS256" #Algoritmo de encriptación
ACCESS_TOKEN_DURATION = 1 #Duración en minutos
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b" #Semilla o clave secreta segura para firmar los tokens
#Una forma de crearla: openssl rand -hex 32

# Configuración del router en FastAPI
router = APIRouter(prefix="/jwtauth",
                   tags=["jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Configuración del esquema de autenticación OAuth2
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Contexto para manejar el cifrado de contraseñas con bcrypt
crypt = CryptContext(schemes=["bcrypt"])

# Modelos de usuario
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str  # Se agrega el campo de contraseña solo en la base de datos

# Base de datos simulada con usuarios predefinidos
users_db = {
    "mouredev": {
        "username": "nazadev",
        "full_name": "Nazaret Duque",
        "email": "duquediazn@nazadev.com",
        "disabled": False,
        "password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6" #bcrypt para 123456 https://bcrypt-generator.com/
    },
    "mouredev2": {
        "username": "nazadev2",
        "full_name": "Nazaria Díaz",
        "email": "duquediazn@nazadev.com",
        "disabled": True,
        "password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU4S" #bcrypt para 654321 https://bcrypt-generator.com/
    }
}

# Función para buscar un usuario en la base de datos
# Devuelve un objeto UserDB si lo encuentra
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

# Función para buscar un usuario en la base de datos sin la contraseña
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# Función para autenticar un usuario a través del token JWT
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        # Decodificamos el token y obtenemos el nombre de usuario
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except InvalidTokenError:
        raise exception

    return search_user(username)

# Función para obtener el usuario actual autenticado
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user

# Endpoint para autenticación y generación del token
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    # Verificamos si la contraseña ingresada coincide con la almacenada
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    # Creamos un access_token con tiempo de expiración
    access_token = {"sub": user.username,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    #Creamos un access_token de forma segura y con un tiempo de validez para el token. 
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

# Endpoint para obtener información del usuario autenticado
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user