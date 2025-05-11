from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import List
from fastapi import HTTPException

app = FastAPI()

class Fruta(BaseModel):
    nombre: str
    color: str
    cantidad: int

class Modo(BaseModel):
    headless: bool

    @validator("headless", pre=True)
    def validar_headless(cls, v):
        if isinstance(v, bool):
            return v
        raise HTTPException(status_code=422, detail="El valor de 'headless' debe ser booleano (true/false)")

class Login(BaseModel):
    username: str
    password: str

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

@app.post("/modo/")
async def modo(modo:Modo):
    if modo.headless:
        return{
            "mensaje":"El modo headless esta activo"
        }
    elif modo.headless == False:
        return{
            "mensaje":"El modo headless esta inactivo"
        }
    else:
        raise HTTPException(status_code=422, detail="Elige un modo valido")

@app.post("/login/")
async def login(login:Login):
    if login.username != "villavicenciojosfer@gmail.com":
        raise HTTPException(status_code=500, detail="Usuario invalido")
    elif login.password != "fernandotest123":
        raise HTTPException(status_code=500, detail="Contraseña invalida")
    return{
        "mensaje": f"Inicio de sesion exitoso, bienvenido {login.username}"
    }


# @app.get("/login/")
# async def login():
#     return{
#         "Username":"villavicenciojosfer@gmail.com",
#         "Password":"fernandotest123"
#     }

@app.post("/agregar_fruta/")
async def agregar_fruta(fruta:Fruta):
    return{
        "mensaje": f"Fruta recibida: {fruta.nombre}, color: {fruta.color}, cantidad: {fruta.cantidad}"
    }
