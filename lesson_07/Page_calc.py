from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self.delay_field = (By.ID, "delay")
        self.button_7 = (By.XPATH, '//span[text()= "7"]')
        self.button_plus = (By.XPATH, '//span[text()= "+"]')
        self.button_8 = (By.XPATH, '//span[text()= "8"]')
        self.button_equals = (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
        self.screen = (By.CSS_SELECTOR, "div[class='screen']")

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def set_delay(self, delay):
        delay_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.delay_field))
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button(self, locator):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        button.click()

    def get_screen_text(self):
        screen_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.screen))
        return screen_element.text

    def wait_for_result(self, expected_result):
        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element(self.screen, expected_result))