from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.XPATH, '//article[@class="product_page"]//p[@class="price_color"]')
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]//div[@class="alertinner "]//strong')
    PRODUCT_PRICE_IN_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[3]//div[@class="alertinner "]//strong')
