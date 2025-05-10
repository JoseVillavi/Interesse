from dataclasses import dataclass

@dataclass
class AmazonLocators:
    
    AmazonWeb: str = 'https://www.amazon.com.mx'
    Cuenta_menu: str = '#nav-link-accountList'
    Usuario_campo: str = '#ap_email_login'
    Boton_usuario: str ='#continue'
    Contraseña_campo: str = '#ap_password'
    Boton_enviar_cuenta: str = '#signInSubmit'
    Todo_menu : str = "#nav-hamburger-menu"
    Menu_electronicos: str = "Electrónicos"
    Tv_video: str = 'a[href="/gp/browse.html?node=9687925011&ref_=nav_em__tv_and_video_0_2_10_2"]'
    Tv_55: str = 'text=Más de 55"'
    Boton_primer_articulo: str = '#a-autoid-1-announce'
    Agregar_al_carrito: str = '#add-to-cart-button'
    Ir_al_carrito : str ='#nav-cart'
    Proceder_pago : str = '#sc-buy-box-ptc-button'

