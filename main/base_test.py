import asyncio
import logging 
from playwright.async_api import async_playwright
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError
import requests
from main.locators import AmazonLocators
from playwright.async_api import expect
import httpx

async def Login_amazon(page,user,password):
    try:

        logging.info("Login started...")

        # This is necessary for the chromium headless speed
        await page.wait_for_timeout(4000)

        # Go to Amazon
        await page.goto(AmazonLocators.AmazonWeb)

        # Click on login
        await page.locator(AmazonLocators.Account_menu).click()

        # Click on username
        await page.locator(AmazonLocators.User_space).click()
        
        # Insert username
        await page.locator(AmazonLocators.User_space).fill(user)

        # Send username
        await page.locator(AmazonLocators.Send_user).click()

        # Click on password
        await page.locator(AmazonLocators.Password_space).click()

        # Insert password
        await page.locator(AmazonLocators.Password_space).fill(password)

        # Send password
        await page.locator(AmazonLocators.Send_password).click()

        # This is because the login it more faster than the screens
        await page.wait_for_timeout(4000)

        logging.info("Login ended")
    
    except PlaywrightTimeoutError as e:
        logging.error(f"Timeout error with the page: {e}")
    except Exception as e:
        logging.error(f"We hava an error during the login process: {e}")


async def Go_to_tv_55(page):
    try:

        logging.info('Go to 55" TVs')

        # Added for the speed of chrumium headless
        await page.wait_for_timeout(4000)
        
        # Get the coordinates of the all menu
        box = await page.locator(AmazonLocators.All_menu).bounding_box()

        # Mueve el mouse al centro del botón
        await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)

        # Wait as a real user
        await page.wait_for_timeout(500)

        # Click on all menu
        await page.locator(AmazonLocators.All_menu).click()

        # Click on Electronics menu
        await page.locator(AmazonLocators.Electronics_menu).first.click()
            
        # Tv and video menu
        await page.locator(AmazonLocators.Tv_video).first.click()

        # Select 55" tvs 
        await page.locator(AmazonLocators.Tv_55).click()

        logging.info('Rutine of 55" Tvs ended')
    
    except PlaywrightTimeoutError as e:
        logging.error(f"Timeout error while finishing purchase: {e}")
    except Exception as e:
        logging.error(f'An error ocurred when we try to go to the 55" TVs: {e}')
   

async def Add_first_item_to_cart(page):
    try:

        logging.info("Add the firts item started...")

        # Added for the speed of chrumium headless
        await page.wait_for_timeout(4000)

        # Get the text of the first item
        button_text = await page.locator(AmazonLocators.First_item_button).text_content()

        # Verify if the button has 'Add to cart' or 'Options'
        if "Ver opciones" in button_text:

            logging.info("Options in first item button")

            # Click on options
            await page.locator(AmazonLocators.First_item_button).click()

            # Wait for the load compleated of the page
            await page.wait_for_timeout(2000)

            # Click on add to cart into the item page
            await page.get_by_role("button", name="Agregar al Carrito", exact=True).click()

            if await page.locator(AmazonLocators.No_coverage_button).is_visible():
                logging.info("Coverage popup visible")
                # Press no add coverage
                await page.locator(AmazonLocators.No_coverage_button).click()

        else:
            logging.info("Add to cart in the firts item button")
            # Click add to cart
            await page.locator(AmazonLocators.First_item_button).click()
        
        logging.info("First item added to the cart")

    except PlaywrightTimeoutError as e:
        logging.error(f"Timeout error while adding first item to cart: {e}")
    except Exception as e:
        logging.error(f"An error occurred while adding the first item to the cart: {e}")


async def Finish_purchase(page):
    try:

        logging.info("Go to pay")

        await page.wait_for_timeout(4000)

        # Go to cart 
        await page.locator(AmazonLocators.Go_to_cart).click()

        # Go to pay
        await page.locator(AmazonLocators.Go_to_pay).click()
    
    except PlaywrightTimeoutError as e:
        logging.error(f"Timeout error while finishing purchase: {e}")
    except Exception as e:
        logging.error(f"An error occurred while finishing the purchase: {e}")


async def Start_API(headless, user, pas):
    logging.info("Send the information to the API")

    # URL of the Endpoint
    url = "http://localhost:8000/login"

    # Format of the data
    data ={
        "headless" : headless,
        "username": user,
        "password": pas
    }
    try:
        # Use httpx for async request
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)
            
            # Check for request status
            response.raise_for_status()
        
        logging.info("Request successfully sent with httpx.")
        return response.json()

    except httpx.RequestError as e:
        logging.error(f"An error occurred while sending the HTTP request with httpx: {e}")
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred with status code {e.response.status_code}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
