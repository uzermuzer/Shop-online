from lokators import SearchHelper
import time



def test_goToLogin(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.search_login()
    main_page.move_login()
    main_page.bay_Mac()
    assert "Mac" in browser.title, "Не перешли на страницу Mac"



