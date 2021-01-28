from random import randint

from page_objects.base_page import BasePage
from page_objects.registation.registration_locators import RegistrationLocators


class RegistrationPage(BasePage):
    def register_account(self):
        self.type(RegistrationLocators.EMAIL_INPUT, f'goraved@{randint(1000, 99999)}.com')
        self.click(RegistrationLocators.CREATE_BTN)
        self.click(RegistrationLocators.GENDER_OPTION)
        self.type(RegistrationLocators.CUSTOMER_FIRST_NAME_INPUT, "Test")
        self.type(RegistrationLocators.CUSTOMER_LAST_NAME_INPUT, "Goraved")
        self.type(RegistrationLocators.PASSWORD_INPUT, "123asd")
        self.select_option(RegistrationLocators.DAYS_SELECTOR, "1")
        self.select_option(RegistrationLocators.MONTHS_SELECTOR, "1")
        self.select_option(RegistrationLocators.YEARS_SELECTOR, "2020")
        self.click(RegistrationLocators.AGREE_CHECKBOX)
        self.click(RegistrationLocators.NEWSLETTER_CHECKBOX)
        self.type(RegistrationLocators.FIRST_NAME_INPUT, 'Test')
        self.type(RegistrationLocators.LAST_NAME_INPUT, 'Goraved')
        self.type(RegistrationLocators.ADDRESS_INPUT, "street")
        self.type(RegistrationLocators.CITY_INPUT, "test")
        self.select_option(RegistrationLocators.STATE_SELECT, "1")
        self.type(RegistrationLocators.POSTCODE_INPUT, "11111")
        self.type(RegistrationLocators.OTHER_INPUT, "123")
        self.type(RegistrationLocators.PHONE_INPUT, "123")
        self.click(RegistrationLocators.ALIAS_BTN)
        self.click(RegistrationLocators.SUBMIT_ACCOUNT_BTN)
