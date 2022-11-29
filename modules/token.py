from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta
from typing import Union
from jose import jwt, JWTError

from schemas.token import TokenData
from modules.querys import get_user

SECRET_KEY = "d20c9a83f171d311899476531e16d1767d8e9b7c0bbccd6bb05727ef352a064e"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 8

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow()+ timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Validación de credenciales sin exito",
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