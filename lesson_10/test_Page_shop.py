"""
Этот модуль содержит тестовые примеры для веб-сайта SauceDemo shopping с использованием Selenium и pytest. Интегрированы отчеты Allure для получения подробных результатов тестирования.
"""

import pytest
from selenium import webdriver
from Page_shop import ShopPage # Assuming ShopPage is in Page_shop.py
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
   Приспособление для создания экземпляра ShopPage.

    Аргументы:
        driver (selenium.webdriver): The webdriver instance.

    Возвращается:
        ShopPage: The ShopPage instance.
    """
    return ShopPage(driver)


@allure.feature("Покупки")
@allure.severity("critical")
@allure.title("Комплексный контрольный тест")
@allure.description("Этот тест проверяет весь процесс оформления заказа, включая добавление нескольких товаров в корзину.")
def test_saucedemo_checkout(page):
    """
    Test-кейс для проверки сквозного процесса оформления заказа с несколькими товарами.
    """
    with allure.step("Откройте страницу магазина"):
        page.open()

    with allure.step("Авторизоваться"):
        page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        page.add_to_cart(page.backpack_button, page.tshirt_button, page.onesie_button)

    with allure.step("Переходите к оформлению заказа"):
        page.proceed_to_checkout()

    with allure.step("Заполните информацию о оформлении заказа"):
        page.fill_checkout_info("Ivan", "Ivanov", "17634")

    with allure.step("Проверить общее количество"):
        total = page.get_total()
        allure.attach(f"Total: {total}", name="Total Amount", attachment_type=allure.attachment_type.TEXT)
        assert total == "Total: $58.29" # This assertion might need updating if prices change on the site
