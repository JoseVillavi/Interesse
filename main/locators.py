from dataclasses import dataclass

@dataclass
class AmazonLocators:
    
    AmazonWeb: str = 'https://www.amazon.com.mx'
    Account_menu: str = '#nav-link-accountList'
    User_space: str = '#ap_email_login'
    Send_user: str ='#continue'
    Password_space: str = '#ap_password'
    Send_password: str = '#signInSubmit'
    All_menu : str = "#nav-hamburger-menu"
    Electronics_menu: str = 'a.hmenu-item[role="button"]:has(div:text("Electrónicos"))'
    Tv_video: str = 'a[href="/gp/browse.html?node=9687925011&ref_=nav_em__tv_and_video_0_2_10_2"]'
    Tv_55: str = '#a-autoid-5-announce'
    First_item_button: str = '#a-autoid-1-announce'
    No_coverage_button: str = '#attachSiNoCoverage'
    Go_to_cart : str ='#nav-cart'
    Go_to_pay : str = '#sc-buy-box-ptc-button'
