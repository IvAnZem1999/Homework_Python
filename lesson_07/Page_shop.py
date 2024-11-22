from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.ID, "shopping_cart_container")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, "[data-test=total-label]")


    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login(self, username, password):
        self.set_field_value(self.username_field, username)
        self.set_field_value(self.password_field, password)
        self.click_button(self.login_button)

    def add_to_cart(self, *items):
        for item in items:
            self.click_button(item)

    def proceed_to_checkout(self):
        self.click_button(self.cart_button)
        self.click_button(self.checkout_button)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.set_field_value(self.first_name_field, first_name)
        self.set_field_value(self.last_name_field, last_name)
        self.set_field_value(self.postal_code_field, postal_code)
        self.click_button(self.continue_button)

    def get_total(self):
        total_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.total_label))
        return total_element.text


    def set_field_value(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def click_button(self, locator):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        button.click()
