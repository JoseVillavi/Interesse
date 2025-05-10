import requests

response = requests.get("http://localhost:8000/login")

if response.status_code == 200:
    data = response.json()
    usuario = data["Username"]
    contrasena = data["Password"]

    print("Usuario:", usuario)
    print("Contraseña:", contrasena)
else:
    print("Error:", response.status_code)