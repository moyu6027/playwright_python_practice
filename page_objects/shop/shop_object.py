from page_objects.base_page import BasePage
from page_objects.shop.shop_locators import ShopLocators


class ShopPage(BasePage):
    def open_site(self):
        self.go_to_url('http://automationpractice.com/index.php')

    def open_t_shirt_category(self):
        self.click(ShopLocators.T_SHIRT_CATEGORY_BTN)

    def add_item_to_cart_and_proceed(self):
        self.hover(ShopLocators.ITEM_NAME_LBL)
        self.click(ShopLocators.ITEM_NAME_LBL)
        self.click(ShopLocators.ADD_TO_CART_BTN)
        self.click(ShopLocators.PROCEED_TO_CHECKOUT_BTN)

    def go_to_the_second_cart_step(self):
        self.click(ShopLocators.SECOND_CART_STEP_BTN)

    def finish_order_after_registration(self):
        self.click('#center_column > form > p > button')
        self.click(ShopLocators.TERMS_CHECKBOX)
        self.click('#form > p > button')
        self.click(ShopLocators.PAY_WITH_BANK_BTN)
        self.click(ShopLocators.CONFIRM_ORDER_BTN)

    def open_profile_order_page(self):
        self.click(ShopLocators.PROFILE_BTN)
        self.click(ShopLocators.ORDERS_BTN)

    def is_order_present(self):
        return self.is_element_present(ShopLocators.ORDER_ROW)
