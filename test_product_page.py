from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.add_to_basket_from_product_page
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fake-mail.org"
        password = "123qwe78qwe"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
        page = ProductPage(browser, link)
        page.open()
        page.successful_alert_that_product_added_to_basket_is_not_presented()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.successful_alert_that_product_added_to_basket_is_not_presented()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page.check_that_basket_is_empty()
    page.check_message_that_basket_is_empty()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.successful_alert_that_product_added_to_basket_is_disappeared()


def test_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    page.should_be_add_to_basket_button()
    page.should_be_product_name()
    page.click_on_add_to_basket_button()

    page.solve_quiz_and_get_code()
    page.should_be_successful_alert_that_product_added_to_basket()
    page.product_name_should_be_equal_with_name_in_successful_add_to_basket_alert()
    page.product_price_should_be_equal_with_price_in_successful_basket_have_new_cost_alert()
