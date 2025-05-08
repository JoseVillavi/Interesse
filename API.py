from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "mi primera fastAPI"}

@app.get("/headless/")
async def headless():
    return{
        "Status": True 
    }

@app.get("/head/")
async def head():
    return{
        "Status": False 
    }

@app.get("/login/")
async def login():
    return{
        "Username":"villavicenciojosfer@gmail.com",
        "Password":"fernandotest123"
    }