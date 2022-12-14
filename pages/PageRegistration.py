from tests.locators import locators
from tests.pages.BaseApp import BasePage
from tests.generator.generation import generation_user


class RegistrationPage(BasePage):

    def move_to_registration(self):
        move = self.find_element(locators.PageSearchLocators.login_or_registration).click()
        move = self.find_element(locators.PageSearchLocators.page_registration).click()
        return move


    def registration_form(self):
        person_info = next(generation_user())
        first_name = person_info.first_name
        last_name = person_info.last_name
        telephone = person_info.telepfone
        email = person_info.email
        password = person_info.password
        self.find_element(locators.PageSearchLocators.FIRST_NAME_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.FIRST_NAME_REGISTRATION).send_keys(first_name)
        self.find_element(locators.PageSearchLocators.lAST_NAME_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.lAST_NAME_REGISTRATION).send_keys(last_name)
        self.find_element(locators.PageSearchLocators.EMAIL_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.EMAIL_REGISTRATION).send_keys(email)
        self.find_element(locators.PageSearchLocators.TELEPHONE_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.TELEPHONE_REGISTRATION).send_keys(telephone)
        self.find_element(locators.PageSearchLocators.PASSWORD_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.find_element(locators.PageSearchLocators.CONFIRM_PASSWORD_REGISTRATION).send_keys(password)
        self.find_element(locators.PageSearchLocators.TICK).click()
        self.find_element(locators.PageSearchLocators.CONTINUE_BUTTON).click()
        return first_name, last_name, telephone, email, password

    def registration_form_not_telephone(self):
        person_info = next(generation_user())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        password = person_info.password
        self.find_element(locators.PageSearchLocators.FIRST_NAME_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.FIRST_NAME_REGISTRATION).send_keys(first_name)
        self.find_element(locators.PageSearchLocators.lAST_NAME_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.lAST_NAME_REGISTRATION).send_keys(last_name)
        self.find_element(locators.PageSearchLocators.EMAIL_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.EMAIL_REGISTRATION).send_keys(email)
        self.find_element(locators.PageSearchLocators.PASSWORD_REGISTRATION).click()
        self.find_element(locators.PageSearchLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.find_element(locators.PageSearchLocators.CONFIRM_PASSWORD_REGISTRATION).send_keys(password)
        self.find_element(locators.PageSearchLocators.TICK).click()
        self.find_element(locators.PageSearchLocators.CONTINUE_BUTTON).click()
        return first_name, last_name, email, password

    def check_telephone(self):
        return self.find_element(locators.PageSearchLocators.NO_TELEPHONE).text

    def logout_account(self):
        logout = self.find_element(locators.PageSearchLocators.login_or_registration).click()
        logout = self.find_element(locators.PageSearchLocators.logout_button).click()
        return logout





