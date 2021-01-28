import os

import allure
import pytest
from allure_commons._allure import step

from page_objects.registation.registration_object import RegistrationPage
from page_objects.shop.shop_object import ShopPage


@allure.story('Shop')
class TestShop:
    @staticmethod
    @allure.title('Order T-Shirt')
    def test_order_t_shirt(page):
        shop_page = ShopPage(page)
        registration_page = RegistrationPage(page)
        with step('Open site'):
            shop_page.open_site()
        with step('Open T-Shirt category'):
            shop_page.open_t_shirt_category()
        with step('Add item to cart and proceed'):
            shop_page.add_item_to_cart_and_proceed()
        with step("Go to the second cart step"):
            shop_page.go_to_the_second_cart_step()
        with step('Register new account'):
            registration_page.register_account()
        with step('Finish order after registration'):
            shop_page.finish_order_after_registration()
        with step('Open profile orders page'):
            shop_page.open_profile_order_page()
        with step('Check at least 1 order present'):
            assert shop_page.is_order_present(), 'Order missed'

    @staticmethod
    @allure.title('Negative to check attachments')
    @pytest.mark.skipif(os.getenv('GITHUB_RUN') is not None, reason='GitHub actions')
    def test_negative(page):
        shop_page = ShopPage(page)
        with step('Open site'):
            shop_page.open_site()
        with step('Fail test'):
            assert False
