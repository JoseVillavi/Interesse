import asyncio 
from playwright.async_api import async_playwright
import requests

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)  # Muy importante para que respete la resolución completa
        page = await context.new_page()
        # Go to amazon
        await page.goto('https://www.amazon.com.mx/')

        # Iniciar sesión
        await page.click('#nav-link-accountList')

        response = requests.get("http://localhost:8000/login")

        assert response.status_code == 200, "La conexión con la API falló"

        data = response.json()
        usuario = data["Username"]
        contrasena = data["Password"]

        # Login function
        await page.click("#ap_email_login")
        await page.fill('#ap_email_login', usuario)
        await page.click('#continue')
        await page.click('#ap_password')
        await page.fill('#ap_password', contrasena)
        await page.click('#signInSubmit')

        await page.screenshot(path="screen.jpg")
        
        # Click on TODO navbar
        await page.click("#nav-hamburger-menu")
        # Go to Electronicos
        await page.get_by_role("button", name="Electrónicos").click()
        # Go to Television y video

        await page.locator('a[href="/gp/browse.html?node=9687925011&ref_=nav_em__tv_and_video_0_2_10_2"]').first.click()
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

        if page.locator("#shipping-address-selection-panel-card-id").is_visible():
            print("El panel de dirección está visible")
        else:
            print("El panel no está visible")
        
        await browser.close()
        

asyncio.run(run())
