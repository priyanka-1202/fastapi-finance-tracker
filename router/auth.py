from fastapi import APIRouter, Depends, HTTPException
from schemas import UserCreate, UserLogin
from sqlalchemy.orm import Session 
from database import get_db
from models import User
from security import hash_password, verify_password, create_access_token
from sqlalchemy import select

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user:UserCreate, db:Session = Depends(get_db)):
    password = hash_password(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message" : "user registered successfully",
        "user_id" : new_user.id
    }

@router.post("/login")
def login(user:UserLogin, db:Session = Depends(get_db)):
    #db.execute is a query method that allows you to execute raw SQL queries or SQLAlchemy Core expressions against the database. It returns a Result object that contains the results of the query.
    db_user = db.execute(select(User).where(User.email == user.email)).scalar_one_or_none()
    if not db_user:
        return HTTPException(
            status_code=401, 
            detail="Invalid email or password")
    
    if not verify_password(user.password, db_user.hashed_password):
        return HTTPException(
            status_code=401, 
            detail="Invalid email or password")

    #if email n pwd is correct, return token to the user
    token = create_access_token(db_user.id)
    return {
        "message" : "Login successful",
        "access_token" : token
    }

@router.get("/me")
def profile(credentials: HTTPAuthorizationCredential = Depends(Session)):
    pass

