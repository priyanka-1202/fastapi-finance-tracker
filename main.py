from fastapi import FastAPI
from database import Base, engine
import models
from router import auth 

app = FastAPI(title="finance tracker", description="A simple finance tracker API", version="1.0.0")
app.include_router(auth.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message" : "Welcome to the finance tracker API!"} 