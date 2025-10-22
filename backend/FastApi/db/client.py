### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Conexión extensión de VS para Mongo: mongodb://localhost

from pymongo import MongoClient

# Descomentar el db_client local o remoto correspondiente

### Base de datos local MongoDB ###
# db_client = MongoClient().local

### Base de datos remota MongoDB Atlas (https://mongodb.com) ###
# Instalar dotenv para cargar variables de entorno: pip install python-dotenv
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer configuración del entorno
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")

# Inicializar el cliente y la base de datos
db_client = MongoClient(MONGODB_URI)[MONGODB_DB]

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/

