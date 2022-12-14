from tests.pages.BaseApp import BasePage
from selenium import webdriver
from tests.pages.PageLogin import SearchHelper
import time

def test_goToLogin(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.search_login()
    main_page.move_login()
    new = browser.current_url
    assert new == 'http://tutorialsninja.com/demo/index.php?route=account/account', ' не удалось'






