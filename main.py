# fastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Body

# others
from datetime import timedelta

# Local Package

from schemas.usuario import Usuario
from modules.auth import auth_user
from modules.token import ACCES_TOKEN_EXPIRE_MINUTES
from modules.token import create_access_token, get_current_user

app = FastAPI()

# Paths

@app.post("/prueba")
async def prueba(dato):
  print(dato)
  data_return = {'message': 'esto fue lo que enviaste', 'data': {dato}}
  return data_return

@app.post("/login")
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
    return {"access_token": acces_token, "token_type": "bearer"}

@app.get("/usuario/me", response_model=Usuario)
async def usuario_info(current_user: Usuario = Depends(get_current_user)):
    return current_user
