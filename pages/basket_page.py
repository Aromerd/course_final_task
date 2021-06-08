from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_that_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items is presented, but should not be"

    def check_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message form that basket is empty not presented"
        text_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert text_message, "Message that basket is empty, has not any text"
