from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage


class PageSearchLocators:

    #home_page
    login_or_registration = (By.CSS_SELECTOR, "a[title = 'My Account']")
    page_login = (By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a")
    page_registration = (By.CSS_SELECTOR, "a[href ='http://tutorialsninja.com/demo/index.php?route=account/register']")
    logout_button = (By.CSS_SELECTOR, "a[href ='http://tutorialsninja.com/demo/index.php?route=account/logout']")


    #registrarion_page
    FIRST_NAME_REGISTRATION = (By.CSS_SELECTOR, '#input-firstname')
    lAST_NAME_REGISTRATION = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_REGISTRATION = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_PASSWORD_REGISTRATION  = (By.CSS_SELECTOR, '#input-confirm')
    TICK = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[class='btn btn-primary']")

    #Ошибки регистрации
    NO_TELEPHONE = (By.CSS_SELECTOR, "div[class= 'text-danger']")

    #
    deckstope = (By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[1]")
    Mac = (By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a")
    add_IMAC = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[1]")


    #login_page
    email_form = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input")
    password_form = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input")
    go_account = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')

    #selection_currency
    CURRENCY_SELECTION = (By.CSS_SELECTOR, 'i[class="fa fa-caret-down"]')
    EURO_SELECTION = (By.CSS_SELECTOR, "button[name='EUR']")
    USD_SELECTION = (By.CSS_SELECTOR, "button[name='USD']")
    POUND_SELECTION =(By.CSS_SELECTOR, "button[name='GBP']")
    CURRENCY_MAC = (By.CSS_SELECTOR, 'p[class="price"]')



    #add item to cart
    BUTTON_ADD_TABLETS_TO_CART = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[1]")
    BUTTON_CART = (By.CSS_SELECTOR, 'button[class= "btn btn-inverse btn-block btn-lg dropdown-toggle"]')
    PRICE_OF_THE_PRODUCT = (By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[1]/table/tbody/tr/td[4]')
    TOTAL_PRICE = (By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[1]/table/tbody/tr/td[4]')
    PAGE_MAC = (By.CSS_SELECTOR, "div[class='image']")
    CLEAR_ADD = (By.CSS_SELECTOR, "i[class='fa fa-times']")
    ADD_MAC_IN_PAGE = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, "button[class='btn btn-primary btn-lg btn-block']")
    SUCSES_ADD = (By.XPATH, '/html/body/div[2]/div[1]/a[1]')
    BUTTON_CART_IN_PAGE = (By.CSS_SELECTOR, 'span[id="cart-total"]')

    #link_page
    SIMPLE_LINK =(By.CSS_SELECTOR, 'a[id= "simleLink"]')
    BAD_REQUEST =(By.CSS_SELECTOR, 'a[id= "bad-request"]')












