from PageRegistration import RegistrationPage
import time

def test_registr_form(browser):
    main_page = RegistrationPage(browser)
    main_page.go_to_site()
    main_page.move_to_registration()
    main_page.registration_form()
    new = browser.current_url
    assert new == 'http://tutorialsninja.com/demo/index.php?route=account/success', 'Не удалось зарегистрироваться'

def test_crash_registr_form(browser):
    main_page = RegistrationPage(browser)
    main_page.go_to_site()
    main_page.logout_account()
    main_page.move_to_registration()
    main_page.registration_form_not_telephone()
    text = main_page.check_telephone()
    assert text == "Telephone must be between 3 and 32 characters!", "Регистрация проходит без ввода телефона"



