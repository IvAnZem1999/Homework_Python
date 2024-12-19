"""
Этот модуль содержит модель страницы для веб-сайта магазина и связанные с ней тестовые примеры с использованием Selenium и pytest. Интегрированы отчеты Allure для получения подробных результатов тестирования.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class ShopPage:
    """
    Page Object Model для веб-сайта покупок по адресу https://www.saucedemo.com/. Этот класс обрабатывает взаимодействия с элементами веб-сайта.
    """
    def __init__(self, driver):
        """
        Инициализирует объект ShopPage.

        Аргументы:
            driver (selenium.webdriver): The Selenium webdriver instance.
        """
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
        """
        Открывает URL-адрес магазина в браузере и разворачивает окно до максимума.

        Возвращается:
            None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login(self, username: str, password: str):
        """
        Войдите в магазин с указанными учетными данными.

        Аргументы:
            username (str): The username.
            password (str): The password.

        Возвращается:
            None
        """
        self.set_field_value(self.username_field, username)
        self.set_field_value(self.password_field, password)
        self.click_button(self.login_button)

    def add_to_cart(self, *items: tuple):
        """
        Добавляет указанные товары в корзину.

        Аргументы:
            *элементы (tuple): переменное количество tuples представляющих локаторы товаров.

        Возвращается:
            None
        """
        for item in items:
            self.click_button(item)

    def proceed_to_checkout(self):
        """
       Приступает к оформлению заказа.

        Возвращается:
            None
        """
        self.click_button(self.cart_button)
        self.click_button(self.checkout_button)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет информацию для оформления заказа.

        Аргументы:
            first_name (str): The first name.
            last_name (str): The last name.
            postal_code (str): The postal code.

        Возвращается:
            None
        """
        self.set_field_value(self.first_name_field, first_name)
        self.set_field_value(self.last_name_field, last_name)
        self.set_field_value(self.postal_code_field, postal_code)
        self.click_button(self.continue_button)

    def get_total(self) -> str:
        """
        Получает общую сумму со страницы.

        Возвращается:
            str: Общая сумма.
        """
        total_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.total_label))
        return total_element.text


    def set_field_value(self, locator: tuple, value: str):
        """
        Задает значение поля формы.

        Аргументы:
            locator (tuple): A tuple содержащий строку стратегии By и локатора.
            value (str): Значение, которое нужно установить.

        Возвращается:
            None
        """
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def click_button(self, locator: tuple):
        """
        Нажимает на кнопку.

        Аргументы:
            locator (tuple): A tuple содержащий строку со стратегией и локатором.

        Возвращается:
            None
        """
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        button.click()



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
    Приспособление для создания экземпляра ShopPage.

    Аргументы:
        driver (selenium.webdriver): The webdriver instance.

    Возвращается:
        ShopPage: The ShopPage instance.
    """
    return ShopPage(driver)


@allure.feature("Покупки")
@allure.severity("critical")
@allure.title("Комплексный тест на совершение покупок")
@allure.description("Этот тест проверяет весь процесс совершения покупок - от входа в систему до оформления заказа.")
def test_e2e_shopping(page):
    """
    Тестовый пример для проверки сквозного потока покупок.
    """
    with allure.step("Откройте страницу магазина"):
        page.open()

    with allure.step("Авторизоваться"):
        page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        page.add_to_cart(page.backpack_button, page.tshirt_button)

    with allure.step("Переходите к оформлению заказа"):
        page.proceed_to_checkout()

    with allure.step("Заполните информацию о оформлении заказа"):
        page.fill_checkout_info("John", "Doe", "12345")

    with allure.step("Проверить общее количество"):
        total = page.get_total()
        allure.attach(f"Total: {total}", name="Total Amount", attachment_type=allure.attachment_type.TEXT)
        assert "Total: $32.39" == total #Adjust assertion if total price changes