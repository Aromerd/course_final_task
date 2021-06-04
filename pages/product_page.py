from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.click_on_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_be_successful_alert_that_product_added_to_basket()
        self.product_name_should_be_equal_with_name_in_successful_add_to_basket_alert()
        self.product_price_should_be_equal_with_price_in_successful_basket_have_new_cost_alert()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME)

    def click_on_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_successful_alert_that_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET_ALERT), \
            "Successful alert that product added to basket is not presented"

    def successful_alert_that_product_added_to_basket_is_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET_ALERT),  \
            "Success message is presented, but should not be"

    def successful_alert_that_product_added_to_basket_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET_ALERT), \
            "Success message is presented, but should not be"

    def product_name_should_be_equal_with_name_in_successful_add_to_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET_ALERT_PRODUCT_NAME), \
            "Text in successful alert that product added to basket is not presented"
        alert_name = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET_ALERT_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_name, \
            f"Expected {product_name} but got {alert_name} from successful alert that product added to basket"

    def product_price_should_be_equal_with_price_in_successful_basket_have_new_cost_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT_ABOUT_NEW_COST_OF_BASKET), \
            "Successful alert that basket have new cost is not presented"
        alert_price = self.browser.find_element(*ProductPageLocators.NEW_COST_OF_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == alert_price, \
            f"Expected {product_price} but got {alert_price} from successful alert that basket have new cost"
