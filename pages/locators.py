from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")


class MainPageLocators:
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p[class='price_color']")
    SUCCESS_ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR, ".alertinner")
    SUCCESS_ADDED_TO_BASKET_ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner>strong")
    SUCCESS_ALERT_ABOUT_NEW_COST_OF_BASKET = (By.CSS_SELECTOR, ".alert-info")
    NEW_COST_OF_BASKET = (By.CSS_SELECTOR, ".alertinner>p>strong")
