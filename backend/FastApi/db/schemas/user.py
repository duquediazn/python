### User schema ###
"""
Convierte un documento de usuario de MongoDB en un diccionario con claves más manejables.
Convierte el _id de MongoDB (tipo ObjectId) en una cadena de texto (str), ya que FastAPI y Pydantic no manejan ObjectId de forma nativa.
Extrae y devuelve solo los campos necesarios: id, username, y email.
"""
def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}
"""
Recibe una lista de usuarios en formato MongoDB y aplica user_schema() a cada uno de ellos.
Devuelve una lista de diccionarios con los datos estructurados correctamente
"""
def users_schema(users) -> list:
    return [user_schema(user) for user in users]