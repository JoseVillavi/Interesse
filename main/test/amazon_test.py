import asyncio 
import requests
import logging
from playwright.async_api import async_playwright
from main.locators import AmazonLocators
from main.base_test import *

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

async def test():
    async with async_playwright() as p:
        # Send the data of head mode, user and password to the endpoint
        login = await Start_API(headless=True, user="villavicenciojosfer@gmail.com",pas="fernandotest123")

        # Set the page settings
        browser = await p.chromium.launch(headless=login.get("headless"))
        context = await browser.new_context(
            viewport={"width": 1600, "height": 900},
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # Calling the login function
        await Login_amazon(page,user=login.get("username"),password=login.get("password"))

        # Calling the function that go to the 55" menu
        await Go_to_tv_55(page)

        # Function to add the first item
        await Add_first_item_to_cart(page)

        # Funtion to finish the purchase
        await Finish_purchase(page)

        logging.info("Process completed, first item purchased")

        # Close the browser
        await browser.close()

asyncio.run(test())