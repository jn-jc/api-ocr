# fastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Body


# others
from jose import JWTError, jwt
from datetime import timedelta

# Local Package
from db.connection import conn
from models.usuario import usuario
from schemas.usuario import Usuario
from schemas.token import TokenData
from modules.auth import auth_user, hash_password
from modules.token import SECRET_KEY, ALGORITHM, ACCES_TOKEN_EXPIRE_MINUTES
from modules.token import create_access_token


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(email: str):
    user = conn.execute(
        usuario.select().where(usuario.c.email_usuario == email)
    ).first()
    if user:
        user_dict = user
    return Usuario(**user_dict)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(email=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Paths

@app.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contrasña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acces_token_expires = timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    acces_token = create_access_token(
        data={"sub": user.email_usuario}, expires_delta=acces_token_expires
    )
    print(acces_token)
    return {"access_token": acces_token, "token_type": "bearer"}


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contrasña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acces_token_expires = timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    acces_token = create_access_token(
        data={"sub": user.email_usuario}, expires_delta=acces_token_expires
    )
    print(acces_token)
    return {"access_token": acces_token, "token_type": "bearer"}

@app.post('/post', dependencies=[Depends(get_current_user)])
async def posting(info: str):
  new_info = f'{info} con algo nuevo'
  return new_info

@app.get("/usuario/me", response_model=Usuario)
async def usuario_info(current_user: Usuario = Depends(get_current_user)):
    print(current_user.dict(exclude={"password"}))
    return current_user.dict(exclude={"password"})
