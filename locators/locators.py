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
    basket = (By.XPATH, "")


    #login_page
    email_form = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input")
    password_form = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input")
    go_account = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')




class SearchHelper(BasePage):
    def search_login(self):
        login = self.find_element(PageSearchLocators.login_or_registration)
        login.click()
        login = self.find_element(PageSearchLocators.page_login)
        login.click()
        return login

    def move_login(self):
        forma = self.find_element(PageSearchLocators.email_form)
        forma.click()
        forma.send_keys("basirinaleksandr@gmail.com")
        forma = self.find_element(PageSearchLocators.password_form)
        forma.click()
        forma.send_keys("raz-raz")
        forma = self.find_element(PageSearchLocators.go_account).click()
        return forma

    def bay_Mac(self):
        bay = self.find_element(PageSearchLocators.deckstope)
        bay.click()
        bay = self.find_element(PageSearchLocators.Mac)
        bay.click()
        return bay

    def add_mac(self):
        button = self.find_element(PageSearchLocators.add_IMAC)
        button.click()

        return button





