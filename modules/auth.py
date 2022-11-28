from passlib.context import CryptContext
from db.connection import conn
from models.vendedor import vendedores

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(login_password: str, hashed_password: str):
    return pwd_context.verify(login_password, hashed_password)


def auth_user(username: str, password: str):
    user = conn.execute(
        vendedores.select().where(vendedores.c.email_vendedor == username)
    ).first()
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user