import asyncio 
from playwright.async_api import async_playwright
import requests
from main.locators import AmazonLocators
from playwright.async_api import expect
import httpx

async def Login_amazon(page,user,password):

    print("Login started...")

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

    print ("Wait")

    await page.wait_for_timeout(4000)

    print("Login ended")


async def Go_to_tv_55(page):

    print('Go to 55" TVs')

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

    print('Rutine of 55" Tvs ended')
   

async def Add_first_item_to_cart(page):

    print("Add the firts item started...")

    # Get the text of the first item
    button_text = await page.locator(AmazonLocators.First_item_button).text_content()

    # Verify if the button has 'Add to cart' or 'Options'
    if "Ver opciones" in button_text:

        print("Options in first item button")

        # Click on options
        await page.locator(AmazonLocators.First_item_button).click()

        # Click on add to cart into the item page
        await page.get_by_role("button", name="Agregar al Carrito", exact=True).click()

    else:
        print("Add to cart in the firts item button")
        # Click add to cart
        await page.locator(AmazonLocators.First_item_button).click()
    
    print("First item added to the cart")


async def Finish_purchase(page):

    print("Go to pay")

    # Go to cart 
    await page.locator(AmazonLocators.Go_to_cart).click()

    # Go to pay
    await page.locator(AmazonLocators.Go_to_pay).click()

    print("purchase completed")

async def Start_API(headless, user, pas):
    print("Send the information to the API")

    # URL of the Endpoint
    url = "http://localhost:8000/login"

    # Format of the data
    data ={
        "headless" : headless,
        "username": user,
        "password": pas
    }
    response = requests.post(url,json=data)

    # Verify the status of the request and return the data
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        response.raise_for_status()
        return response.json()
