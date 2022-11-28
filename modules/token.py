from datetime import datetime, timedelta
from typing import Union
from jose import jwt
from schemas.token import Token

SECRET_KEY = "d20c9a83f171d311899476531e16d1767d8e9b7c0bbccd6bb05727ef352a064e"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 15

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow()+ timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt