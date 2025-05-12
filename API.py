from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import List
from fastapi import HTTPException

app = FastAPI()

class Login(BaseModel):
    headless: bool
    username: str
    password: str

    @validator("headless", pre=True)
    def validate_head(cls, v):
        if isinstance(v, bool):
            return v
        raise HTTPException(status_code=422, detail="The 'headless' valeu needs to be boolean (true/false)")
    
    @validator("username", pre=True)
    def validate_username(cls, v):
        if isinstance(v, str):
            return v
        raise HTTPException(status_code=422, detail="The user needs to be a string")
    
    @validator("password", pre=True)
    def validate_password(cls, v):
        if isinstance(v, str):
            return v
        raise HTTPException(status_code=422, detail="The password needs to be a string")
    

@app.get("/")
async def root():
    return{"message": "my first fastAPI"}


@app.post("/login")
async def login(login:Login):
    headless_status = None
    # Hedless?
    if login.headless:
        headless_status = "The headless mode its active"
        
    elif login.headless == False:
            headless_status = "The headed mode its active"

    # Login
    if login.username != "villavicenciojosfer@gmail.com":
        raise HTTPException(status_code=500, detail="Invalid user")
    elif login.password != "fernandotest123":
        raise HTTPException(status_code=500, detail="Invalid password")
    return{
        "mensaje": f"Welcome {login.username}, {headless_status}",
        "headless": login.headless,
        "username": login.username,
        "password": login.password
    }
