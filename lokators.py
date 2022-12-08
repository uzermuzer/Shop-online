from selenium.webdriver.common.by import By
from BaseApp import BasePage
import pyautogui


class PageSearchLocators:
    login_or_registration = (By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/a")
    page_login = (By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a")
    page_registration = (By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a")
    email_form = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input")
    password_form = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input")
    go_account = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')
    deckstope = (By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[1]")
    Mac = (By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a")
    add_IMAC = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[1]")
    basket = (By.XPATH, "")
    #actual_browser = webdriver.current_url


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





