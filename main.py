# fastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Body, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# others
from datetime import timedelta
from os import getcwd

# Local Package
from schemas.usuario import Usuario
from modules.auth import auth_user
from modules.token import ACCES_TOKEN_EXPIRE_MINUTES
from modules.token import create_access_token, get_current_user
from modules.image import send_image

app = FastAPI(
    title="API OCR-app Cruz Verde Colombia",
    description="This api contains a many features to automatizate about the process to sign up a new customers on the club cruz verde program",
)


# Paths

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login", tags=["Auth"])
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


@app.get("/user/me", response_model=Usuario, tags=["User data"])
async def usuario_info(current_user: Usuario = Depends(get_current_user)):
    return current_user


# dependencies=[Depends(get_current_user)]
@app.post("/image/send", tags=["Images"], status_code=status.HTTP_202_ACCEPTED)
async def upload_image(image: UploadFile = File(...)):
    if image.content_type != "image/jpeg":
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="El tipo de archivo debe ser una imagen/jpg",
        )
    with open(getcwd() + "/temp/" + image.filename, "wb") as file:
        content = image.file.read()
        file.write(content)
        file.close()
    message = await send_image()
    if message:
      return {'message': 'El archivo se envio correctamente'}
    return {'message': 'El archivo no se envio con exito, por favor vuelva a intentarlo'}
