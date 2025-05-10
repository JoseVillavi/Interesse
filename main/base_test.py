import asyncio 
from playwright.async_api import async_playwright
import requests
from main.locators import AmazonLocators

async def iniciar_sesion_amazon(page):

    print("Inicio de sesión iniciado...")

    # Ve a amazon
    await page.goto(AmazonLocators.AmazonWeb)

    # Click en iniciar sesión
    await page.locator(AmazonLocators.Cuenta_menu).click()

    # Endpoint
    response = requests.get("http://localhost:8000/login")
    assert response.status_code == 200, "La conexión con la API falló"
    data = response.json()
    usuario = data["Username"]
    contrasena = data["Password"]

    # Click en username e inserccion
    await page.locator(AmazonLocators.Usuario_campo).click()
    await page.locator(AmazonLocators.Usuario_campo).fill(usuario)

    # Click en continuar
    await page.locator(AmazonLocators.Boton_usuario).click()

    # Click en password e inserccion
    await page.locator(AmazonLocators.Contraseña_campo).click()
    await page.locator(AmazonLocators.Contraseña_campo).fill(contrasena)

    # Click para logear
    await page.locator(AmazonLocators.Boton_enviar_cuenta).click()

    print("Inicio de sesión finalizado")


async def ir_a_TV_55(page):

    print("Rutina ir a TV 55 pulgadas iniciada...")

    # Click en TODO navbar
    await page.locator(AmazonLocators.Todo_menu).click()

    # Click en Electronicos
    await page.locator(AmazonLocators.Menu_electronicos).click()
        
    # Television y video menu
    await page.locator(AmazonLocators.Tv_video).first.click()

    # Selecciona 55 pulgadas
    await page.locator(AmazonLocators.Tv_55).click()

    print("Rutina ir a TV 55 pulgadas finalizada")
   

async def agregar_primer_item(page):

    print("Rutina agregar el primer item iniciada...")

    # Obtener el texto que aparece dentro del botón del primer item
    boton_texto = await page.locator(AmazonLocators.Boton_primer_articulo).text_content()

    # Verifica si el botón es 'Ver opciones' o 'Agregar al carrito'
    if "Ver opciones" in boton_texto:

        # Damos click en 'Ver opciones'
        await page.locator(AmazonLocators.Boton_primer_articulo).click()

        # Damos click en 'Agregar al carrito'
        await page.locator(AmazonLocators.Agregar_al_carrito).click()

    else:
        # Solo damos click en agregar al carrito desde la pestaña
        await page.locator(AmazonLocators.Boton_primer_articulo).click()
    
    print("Rutina ir a TV 55 pulgadas finalizada")


async def finalizar_compra(page):

    print("Finalizando compra...")

    # Ir al carrito
    await page.locator(AmazonLocators.Ir_al_carrito).click()

    # Proceder al pago
    await page.locator(AmazonLocators.Proceder_pago).click()

    print("Compra finalizada")

