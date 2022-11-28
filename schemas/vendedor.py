from typing import Optional
from pydantic import BaseModel, Field, EmailStr, SecretStr

class VendedorBase(BaseModel):
  id_vendedor: Optional[int]
  email_vendedor: EmailStr = Field(...)
  password: Optional[SecretStr]

class Vendedor(VendedorBase):
  id_tienda: int = Field(...)
  nombre_vendedor: str = Field(...)
  apellido_vendedor: str = Field(...)
  