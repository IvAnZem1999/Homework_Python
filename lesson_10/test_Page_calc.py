"""
Этот модуль содержит тестовые примеры для работы с медленным калькулятором с использованием Selenium и pytest. Интегрированы отчеты Allure для получения подробных результатов тестирования.
"""

import pytest
from selenium import webdriver
from Page_calc import CalculatorPage #Предполагая, что CalculatorPage находится в Page_calc.py
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
    Приспособление для предоставления экземпляра CalculatorPage.

    Аргументы:
        driver (selenium.webdriver): The webdriver instance.

    Возвращается:
        CalculatorPage: The CalculatorPage instance.
    """
    return CalculatorPage(driver)


@allure.feature("Калькулятор")
@allure.severity("critical")
@allure.title("Протестируйте медленное добавление калькулятора")
@allure.description("Этот тест проверяет функциональность сложения в медленном калькуляторе с задержкой.")
def test_slow_calculator(page):
    """
    Тестовый пример для проверки функциональности добавления с задержкой.
    """
    with allure.step("Откройте страницу калькулятора"):
        page.open()

    with allure.step("Установите задержку на 45"):
        page.set_delay(45)
    with allure.step("Выполните расчет 7 + 8"):
        page.click_button(page.button_7)
        page.click_button(page.button_plus)
        page.click_button(page.button_8)
        page.click_button(page.button_equals)

    with allure.step("Дождитесь результата и проверьте"):
        page.wait_for_result("15")
        assert "15" == page.get_screen_text()