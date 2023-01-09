import time

from tests.pages.PageCurrency import PageCurrency

class TestCurrency:

    def test_change_EUR(self,browser):
        main_page = PageCurrency(browser)
        main_page.go_to_site()
        main_page.search_login()
        main_page.move_login()
        main_page.move_mac_page()
        main_page.euro_selection()
        txt = main_page.go_to_cart().text
        cur = main_page.chek_currency().text
        assert txt == "0 item(s) - 0.00€", "Валюта в корзине не поменялась"
        assert '€' in cur, "Валюта каталоге не поменялась"


    def test_change_POUND(self,browser):
        main_page = PageCurrency(browser)
        time.sleep(2)
        main_page.pound_selection()
        time.sleep(3)
        txt = main_page.go_to_cart().text
        cur = main_page.chek_currency().text
        assert txt == "0 item(s) - £0.00", "Валюта в корзине не поменялась"
        assert '£' in cur, "Валюта в катологе не поменялась"

    def test_change_USD(self, browser):
        main_page = PageCurrency(browser)
        main_page.usd_selection()
        txt = main_page.go_to_cart().text
        cur = main_page.chek_currency().text
        assert txt == "0 item(s) - $0.00", "Валюта в корзине не поменялась"
        assert '$' in cur, "Валюта в каталоге не поменялась"

