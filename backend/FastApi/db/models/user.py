### User model ###
"""
BaseModel: Clase base de Pydantic que permite definir modelos de datos con validaciones.
Optional: Indica que un campo puede ser opcional.
"""
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None  # Puede estar presente o no, ya que MongoDB lo genera automáticamente
    username: str  # Nombre de usuario (obligatorio)
    email: str  # Correo electrónico (obligatorio)
