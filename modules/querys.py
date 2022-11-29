from db.connection import conn
from models.usuario import usuario
from schemas.usuario import Usuario

def get_user(email: str):
    user = conn.execute(
        usuario.select().where(usuario.c.email_usuario == email)
    ).first()
    if user:
        user_dict = user
    return Usuario(**user_dict)