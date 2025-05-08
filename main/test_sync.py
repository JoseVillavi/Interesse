from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)  # Muy importante para que respete la resolución completa
        page = context.new_page()
        
        # Go to amazon
        page.goto('https://www.amazon.com.mx/')
        
        # Click on TODO navbar
        page.click("#nav-hamburger-menu")
        
        # Go to Electrónicos
        page.get_by_role("button", name="Electrónicos").click()
        
        # Go to Televisión y Video
        page.locator('a[href="/gp/browse.html?node=9687925011&ref_=nav_em__tv_and_video_0_2_10_2"]').first.click()
        
        # Go to Más de 55"
        page.get_by_role("link", name='Más de 55"').click()
        
        # Botón del primer anuncio
        button_tv = "#a-autoid-1-announce"
        
        # Obtener el texto que aparece dentro del botón
        boton_texto = page.locator(button_tv).text_content()
        
        if "Ver opciones" in boton_texto:
            page.locator(button_tv).click()
            page.locator("#add-to-cart-button").click()
            page.locator("#sc-buy-box-ptc-button").click()
        else:
            page.locator(button_tv).click()
            page.locator("#nav-cart").click()
            page.locator("#sc-buy-box-ptc-button").click()

        browser.close()

run()
