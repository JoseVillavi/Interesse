import asyncio 
from playwright.async_api import async_playwright
import requests
from amazon_locators import AmazonLocators as Locators
async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)  # Muy importante para que respete la resolución completa
        page = await context.new_page()
        # Go to amazon
        await page.goto(Locators.AmazonWeb)

        # Iniciar sesión
        await page.click(Locators.Cuenta_menu)

        # API
        response = requests.get("http://localhost:8000/login")

        assert response.status_code == 200, "La conexión con la API falló"

        data = response.json()
        usuario = data["Username"]
        contrasena = data["Password"]

        # Login function
        await page.click(Locators.Usuario_campo)
        await page.fill(Locators.Usuario_campo, usuario)
        await page.click(Locators.Boton_usuario)
        await page.click(Locators.Contraseña_campo)
        await page.fill(Locators.Contraseña_campo, contrasena)
        await page.click(Locators.Boton_enviar_cuenta)
        
        # Click on TODO navbar
        await page.click(Locators.Todo_menu)
        # Go to Electronicos
        await page.get_by_role("button", name="Electrónicos").click()
        # Go to Television y video

        await page.locator(Locators.Tv_video).first.click()
        # Go to mas de 55"
        await page.get_by_role("link", name="Más de 55\"").click()

        # Boton del primer anuncio
        button_tv = "#a-autoid-1-announce"

        if page.locator("#shipping-address-selection-panel-card-id").is_visible():
            print("El panel de dirección está visible")
        else:
            print("El panel no está visible")
        
        # Obtener el texto que aparece dentro del botón
        boton_texto = await page.locator(button_tv).text_content()
        # Verify if ver opciones button doesn not appear
        if "Ver opciones" in boton_texto:
            # Damos click en agregar al carrito
            await page.locator("#a-autoid-1-announce").click()
            # Damos click en agregar al carrito
            await page.locator("#add-to-cart-button").click()
            # procedemos al pago 
            await page.locator("#sc-buy-box-ptc-button").click()

            print("El pago se realizó")
        else:
            # Solo damos click en agregar al carrito desde la pestaña
            await page.locator("#a-autoid-1-announce").click()

            # Ir al carrito
            await page.locator("#nav-cart").click()

            # Proceder al pago
            await page.locator("#sc-buy-box-ptc-button").click()

            print("El pago se realizó")
        
        await browser.close()
        

asyncio.run(run())
