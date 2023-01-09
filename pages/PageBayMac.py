from tests.locators.locators import PageSearchLocators
from tests.pages.BaseApp import BasePage


class BayMac(BasePage):
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

    def move_mac_page(self):
        self.find_element(PageSearchLocators.deckstope).click()
        move = self.find_element(PageSearchLocators.Mac)
        move.click()
        return move

    def bay_mac(self):
        bay = self.find_element(PageSearchLocators.BUTTON_ADD_TABLETS_TO_CART)
        bay.click()
        return bay

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


