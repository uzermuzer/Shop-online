
from tests.locators.locators import PageSearchLocators
from tests.pages.BaseApp import BasePage


class AddToCartPage(BasePage):

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

    #def add_to_cart(self):
