"""
Этот модуль содержит модель страницы для веб-формы и связанные с ней тестовые примеры с использованием Selenium и pytest. Модель показывает взаимодействие с элементами формы, улучшая читаемость кода и удобство сопровождения. Интегрированы отчеты Allure для получения подробных результатов тестирования.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class FormPage:
    """
    Page Object Model для веб-формы по адресу https://bonigarcia.dev/selenium-webdriver-java/data-types.html. Этот класс обрабатывает взаимодействия с элементами формы.
    """
    def __init__(self, driver):
        """
        Инициализирует объект FormPage.

 Аргументы:
            driver (selenium.webdriver): The Selenium webdriver instance.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

        # Locators for form elements
        self.first_name_field = (By.NAME, "first-name")
        self.last_name_field = (By.NAME, "last-name")
        self.address_field = (By.NAME, "address")
        self.zip_code_field = (By.NAME, "zip-code")
        self.city_field = (By.NAME, "city")
        self.country_field = (By.NAME, "country")
        self.email_field = (By.NAME, "e-mail")
        self.phone_field = (By.NAME, "phone")
        self.job_position_field = (By.NAME, "job-position")
        self.company_field = (By.NAME, "company")
        self.submit_button = (By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")
        self.zip_code_element = (By.ID, "zip-code") 
        self.first_name_element = (By.ID, "first-name") 
        self.last_name_element = (By.ID, "last-name") 
        self.address_element = (By.ID, "address")    
        self.email_element = (By.ID, "e-mail")      
        self.phone_element = (By.ID, "phone")      
        self.city_element = (By.ID, "city")        


    def open(self):
        """
        Открывает URL-адрес формы в браузере и разворачивает окно до максимума.

 Возвращается:
            None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def fill_form(self, first_name: str, last_name: str, address: str, zip_code: str, city: str, country: str, email: str, phone: str, job_position: str, company: str):
        """
        Заполняет веб-форму предоставленными данными.

        Аргументы:
            first_name (str): The first name.
            last_name (str): The last name.
            address (str): The address.
            zip_code (str): The zip code.
            city (str): The city.
            country (str): The country.
            email (str): The email address.
            phone (str): The phone number.
            job_position (str): The job position.
            company (str): The company name.

        Возвращается:
            None
        """
        self.set_field_value(self.first_name_field, first_name)
        self.set_field_value(self.last_name_field, last_name)
        self.set_field_value(self.address_field, address)
        self.set_field_value(self.zip_code_field, zip_code)
        self.set_field_value(self.city_field, city)
        self.set_field_value(self.country_field, country)
        self.set_field_value(self.email_field, email)
        self.set_field_value(self.phone_field, phone)
        self.set_field_value(self.job_position_field, job_position)
        self.set_field_value(self.company_field, company)

    def submit(self):
        """
        Отправляет форму.

        Возвращается:
            None
        """
        self.driver.find_element(*self.submit_button).click()

    def set_field_value(self, locator: tuple, value: str):
        """
        Задает значение поля формы.

        Аргументы:
            locator (tuple): A tuple containing the By strategy and locator string.
            value (str): The value to set.

        Возвращается:
            None
        """
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_element_attribute(self, locator: tuple, attribute: str) -> str:
        """
        Возвращает значение атрибута из элемента формы.

        Аргументы:
            locator (tuple): A tuple containing the By strategy and locator string.
            attribute (str): The attribute name.

        Возвращается:
            str: Значение атрибута. Возвращает пустую строку, если элемент или атрибут не найден.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element.get_attribute(attribute)
        except:
            return ""


import pytest
from selenium import webdriver

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
    Приспособление для создания экземпляра FormPage.

    Аргументы:
        driver (selenium.webdriver): The webdriver instance.

    Возвращается:
        FormPage: The FormPage instance.
    """
    return FormPage(driver)


@allure.feature("Подача формы")
@allure.severity("critical")
@allure.title("Отправка тестовой формы")
@allure.description("Этот тест проверяет правильность отправки формы и правильность заполнения поля почтового индекса.")
def test_data_form_submission(page):
    """
    Тестовый пример для проверки отправки и валидации формы.
    """
    with allure.step("Откройте страницу формы"):
        page.open()

    with allure.step("Заполните форму"):
        page.fill_form("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "test@skypro.com", "+7985899998787", "QA", "SkyPro")

    with allure.step("Отправьте форму"):
        page.submit()

    with allure.step("Ошибка проверки почтового индекса"):
        zip_code_class = page.get_element_attribute(page.zip_code_element, "class")
        allure.attach(f"Zip Code class: {zip_code_class}", name="Zip Code Class", attachment_type=allure.attachment_type.TEXT)
        assert 'alert-danger' in zip_code_class

    with allure.step("Проверьте успешность заполнения других полей"):
        assert 'success' in page.get_element_attribute(page.first_name_element, "class")
        assert 'success' in page.get_element_attribute(page.last_name_element, "class")
        assert 'success' in page.get_element_attribute(page.address_element, "class")
        assert 'success' in page.get_element_attribute(page.email_element, "class")
        assert 'success' in page.get_element_attribute(page.phone_element, "class")
        assert 'success' in page.get_element_attribute(page.city_element, "class")