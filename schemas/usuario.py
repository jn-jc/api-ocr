from typing import Optional
from pydantic import BaseModel, Field, EmailStr, SecretStr

class UsuarioBase(BaseModel):
  id_usuario: Optional[int]
  email_usuario: EmailStr = Field(...)
  password: Optional[SecretStr]

class Usuario(UsuarioBase):
  id_tienda: int = Field(...)
  nombre_usuario: str = Field(...)
  apellido_usuario: str = Field(...)
  