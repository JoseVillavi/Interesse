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
    def validar_headless(cls, v):
        if isinstance(v, bool):
            return v
        raise HTTPException(status_code=422, detail="El valor de 'headless' debe ser booleano (true/false)")
    
    @validator("username", pre=True)
    def validar_username(cls, v):
        if isinstance(v, str):
            return v
        raise HTTPException(status_code=422, detail="El usuario debe ser una cadena de texto")
    
    @validator("password", pre=True)
    def validar_password(cls, v):
        if isinstance(v, str):
            return v
        raise HTTPException(status_code=422, detail="La contraseña debe ser una cadena de texto")
    

@app.get("/")
async def root():
    return{"message": "mi primera fastAPI"}


@app.post("/login/")
async def login(login:Login):
    headless_status = None
    # Hedless?
    if login.headless:
        headless_status = "el modo headless esta activo"
        
    elif login.headless == False:
            headless_status = "el modo headless esta inactivo"

    # Login
    if login.username != "villavicenciojosfer@gmail.com":
        raise HTTPException(status_code=500, detail="Usuario invalido")
    elif login.password != "fernandotest123":
        raise HTTPException(status_code=500, detail="Contraseña invalida")
    return{
        "mensaje": f"bienvenido {login.username}, {headless_status}"
    }
