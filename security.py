import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from jose import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredential
from fastapi import Depends

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
#if fields in .env file is not found, then set default value for ACCESS_TOKEN_EXPIRE_MINUTES to 30
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

'''HTTPBearer is a class that provides a way to extract and validate the Authorization header from 
incoming HTTP requests. It is used to implement token-based authentication in FastAPI applications.
'''
security = HTTPBearer() 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#generaete a JWT token for the user after successful login
def create_access_token(user_id:int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {
        "user_id": user_id,
        "exp": expire
    }
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token

def verify_token(token:str):
    pass

def get_current_user(credentials: HTTPAuthorizationCredential = Depends(security)):
    pass






