from tests.locators.locators import PageSearchLocators
from tests.pages.BaseApp import BasePage


class PageCurrency(BasePage):
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

    def euro_selection(self):
        euro = self.find_element(PageSearchLocators.CURRENCY_SELECTION)
        euro.click()
        euro = self.find_element(PageSearchLocators.EURO_SELECTION)
        euro.click()
        return euro

    def usd_selection(self):
        euro = self.find_element(PageSearchLocators.CURRENCY_SELECTION)
        euro.click()
        euro = self.find_element(PageSearchLocators.USD_SELECTION)
        euro.click()
        return euro

    def pound_selection(self):
        euro = self.find_element(PageSearchLocators.CURRENCY_SELECTION)
        euro.click()
        euro = self.find_element(PageSearchLocators.POUND_SELECTION)
        euro.click()
        return euro


    def go_to_cart(self):
        go = self.find_element(PageSearchLocators.BUTTON_CART)
        go.click()
        return go

    def clear_add(self):
        clear = self.find_element(PageSearchLocators.BUTTON_CART)
        clear.click()
        clear = self.find_element(PageSearchLocators.CLEAR_ADD)
        clear.click()
        return clear

    def move_mac_page(self):
        move= self.find_element(PageSearchLocators.deckstope)
        move.click()
        move = self.find_element(PageSearchLocators.Mac)
        move.click()
        return move

    def chek_currency(self):
        go = self.find_element(PageSearchLocators.CURRENCY_MAC)
        return go

