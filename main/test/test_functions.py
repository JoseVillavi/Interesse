import asyncio 
from playwright.async_api import async_playwright
import requests
from main.locators import AmazonLocators
from main.base_test import iniciar_sesion_amazon

async def test():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)  # Muy importante para que respete la resolución completa
        page = await context.new_page()

        # llamando a la funcion...
        await iniciar_sesion_amazon(page)

        # Cerrar navegador
        browser.close()
asyncio.run(test())