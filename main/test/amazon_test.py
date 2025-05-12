import asyncio 
from playwright.async_api import async_playwright
import requests
from main.locators import AmazonLocators
from main.base_test import *

async def test():
    async with async_playwright() as p:
        # Send the data of head mode, user and password to the endpoint
        login = await Start_API(headless=True, user="villavicenciojosfer@gmail.com",pas="fernandotest123")

        # Set the page settings
        browser = await p.firefox.launch(headless=login.get("headless"), args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        # Calling the login function
        await Login_amazon(page,user=login.get("username"),password=login.get("password"))

        # Calling the function that go to the 55" menu
        await Go_to_tv_55(page)

        # Function to add the first item
        await Add_first_item_to_cart(page)

        # Funtion to finish the purchase
        await Finish_purchase(page)

        # Close the browser
        await browser.close()
asyncio.run(test())