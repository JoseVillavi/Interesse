import asyncio 
from playwright.async_api import async_playwright
import requests
from main.locators import AmazonLocators
from main.base_test import *

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)  # Muy importante para que respete la resolución completa
        page = await context.new_page()

        # llamando a la funcion login
        await iniciar_sesion_amazon(page)

        # Llamando funcion ir a menu TV 55 pulgadas
        await ir_a_TV_55(page)

        # Agregar primer item al carrito
        await agregar_primer_item(page)

        # Finalizar compra
        await finalizar_compra(page)

        # Cerrar navegador
        await browser.close()
asyncio.run(test())