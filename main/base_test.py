import asyncio 
from playwright.async_api import async_playwright
import requests
from main.locators import AmazonLocators

async def iniciar_sesion_amazon(page):
    await page.goto(AmazonLocators.AmazonWeb)
    # Iniciar sesión
    await page.click(AmazonLocators.Cuenta_menu)

    # API
    response = requests.get("http://localhost:8000/login")

    assert response.status_code == 200, "La conexión con la API falló"

    data = response.json()
    usuario = data["Username"]
    contrasena = data["Password"]

    # Login function
    await page.click(AmazonLocators.Usuario_campo)
    await page.fill(AmazonLocators.Usuario_campo, usuario)
    await page.click(AmazonLocators.Boton_usuario)
    await page.click(AmazonLocators.Contraseña_campo)
    await page.fill(AmazonLocators.Contraseña_campo, contrasena)
    await page.click(AmazonLocators.Boton_enviar_cuenta)

