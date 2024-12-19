"""
Этот модуль содержит тестовые примеры для веб-формы с использованием Selenium и pytest. Интегрирована функция создания отчетов Allure для получения подробных результатов тестирования.
"""

import pytest
from selenium import webdriver
from Page_form import FormPage # Предполагая, что FormPage находится в Page_form.py
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
    Приспособление для создания экземпляра FormPage.

    Аргументы:
        driver (selenium.webdriver): The webdriver instance.

    Возвращается:
        FormPage: The FormPage instance.
    """
    return FormPage(driver)


@allure.feature("Подача формы")
@allure.severity("critical")
@allure.title("Отправка и валидация тестовой формы")
@allure.description("Этот тест проверяет отправку формы и правильность заполнения отдельных полей.")
def test_data_form_submission(page):
    """
    Тестовый пример для проверки отправки и валидации формы.
    """
    with allure.step("Откройте страницу формы"):
        page.open()

    with allure.step("Заполните форму действительными данными"):
        page.fill_form("Иван", "Петров", "Ленина, 55-3", "123456", "Москва", "Россия", "test@skypro.com", "+7985899998787", "QA", "SkyPro")

    with allure.step("Отправьте форму"):
        page.submit()

    with allure.step("Проверьте поле с почтовым индексом"):
        zip_code_class = page.get_element_attribute(page.zip_code_element, "class")
        allure.attach(f"Zip Code class: {zip_code_class}", name="Zip Code Class", attachment_type=allure.attachment_type.TEXT)
        assert 'success' in zip_code_class #Zip code field should be valid now.


    with allure.step("Проверьте другие поля"):
        assert 'success' in page.get_element_attribute(page.first_name_element, "class")
        assert 'success' in page.get_element_attribute(page.last_name_element, "class")
        assert 'success' in page.get_element_attribute(page.address_element, "class")
        assert 'success' in page.get_element_attribute(page.email_element, "class")
        assert 'success' in page.get_element_attribute(page.phone_element, "class")
        assert 'success' in page.get_element_attribute(page.city_element, "class")