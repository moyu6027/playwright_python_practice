import allure
from playwright._helper import TimeoutError as TError
from playwright._page import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click locator - {locator}')
    def click(self, locator: str):
        self.page.click(locator)

    @allure.step('Check checkbox locator - {locator}')
    def check(self, locator: str):
        self.page.check(locator)

    @allure.step('Uncheck checkbox locator - {locator}')
    def uncheck(self, locator: str):
        self.page.check(locator)

    @allure.step('Hover locator - {locator}')
    def hover(self, locator: str):
        self.page.hover(locator)

    @allure.step('Go to url - {url}')
    def go_to_url(self, url: str):
        self.page.goto(url)

    @allure.step('Type text - {text} into locator - {locator}')
    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    @allure.step('Select option - {option} in locator - {locator}')
    def select_option(self, locator: str, option: str):
        self.page.selectOption(locator, option)

    @allure.step('Is element - {locator} present')
    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.waitForSelector(locator)
            return True
        except TError:
            return False

    @allure.step('Is element - {locator} hidden')
    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.waitForSelector(locator, state='hidden')
            return True
        except TError:
            return False
