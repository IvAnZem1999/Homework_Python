"""
Этот модуль содержит модель для веб-страницы с вычислением и связанные с ней тестовые примеры с использованием Selenium и pytest. Интегрированы отчеты Allure для получения подробных результатов тестирования.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalculatorPage:
    """
    Page Object Model для веб-страницы slow calculator по адресу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
 Этот класс обрабатывает взаимодействия с элементами калькулятора.
    """
    def __init__(self, driver):
        """
       Инициализирует объект CalculatorPage.

 Аргументы:
 driver (selenium.webdriver):Selenium webdriver.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self.delay_field = (By.ID, "delay")
        self.button_7 = (By.XPATH, '//span[text()= "7"]')
        self.button_plus = (By.XPATH, '//span[text()= "+"]')
        self.button_8 = (By.XPATH, '//span[text()= "8"]')
        self.button_equals = (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
        self.screen = (By.CSS_SELECTOR, "div[class='screen']")

    def open(self):
        """
        Открывает URL-адрес калькулятора в браузере и разворачивает окно до максимума.

 Возвращается:
            None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def set_delay(self, delay: int):
        """
        Задает значение задержки в калькуляторе.

 Аргументы:
 задержка (int): задаваемое значение задержки.

 Возвращается:
            None
        """
        delay_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.delay_field))
        delay_element.clear()
        delay_element.send_keys(str(delay)) # Ensure delay is sent as a string

    def click_button(self, locator: tuple):
        """
        Нажимает кнопку на калькуляторе.

 Аргументы:
 локатор (tuple): tuple, содержащий строку стратегии и локатора.

 Возвращается:
            None
        """
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        button.click()

    def get_screen_text(self) -> str:
        """
        Возвращает текст, отображаемый на экране калькулятора.

 Возвращается:
 str: Текст с экрана калькулятора.
        """
        screen_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.screen))
        return screen_element.text

    def wait_for_result(self, expected_result: str):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

 Аргументы:
 ожидаемый результат (str): ожидаемый результат, которого нужно дождаться.

 Возвращается:
            None
        """
        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element(self.screen, expected_result))


import pytest
from selenium import webdriver
import allure

@pytest.fixture
def driver():
    """
    Приспособление для создания экземпляра Chrome webdriver.

 Возвращается:
        selenium.webdriver: The webdriver instance.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    """
    Приспособление для создания экземпляра CalculatorPage.

    Аргументы:
        driver (selenium.webdriver): The webdriver instance.

    Возвращается:
        CalculatorPage: The CalculatorPage instance.
    """
    return CalculatorPage(driver)


@allure.feature("Calculator")
@allure.severity("critical")
@allure.title("Test calculator addition")
@allure.description("This test verifies the addition functionality of the slow calculator.")
def test_calculator_addition(page):
    """
    Тестовый пример для проверки функциональности добавления.
    """
    with allure.step("Open the calculator page"):
        page.open()

    with allure.step("Set delay to 0"):
        page.set_delay(0)

    with allure.step("Perform calculation 7 + 8"):
        page.click_button(page.button_7)
        page.click_button(page.button_plus)
        page.click_button(page.button_8)
        page.click_button(page.button_equals)

    with allure.step("Wait for result and verify"):
        page.wait_for_result("15")
        assert page.get_screen_text() == "15"