import pytest
from selenium import webdriver
from Page_form import FormPage 

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    return FormPage(driver)

def test_data_form_submission(page):
    page.open()
    page.fill_form("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "test@skypro.com", "+7985899998787", "QA", "SkyPro")
    page.submit()

    assert 'alert-danger' in page.get_element_attribute(page.zip_code_element, "class")
    assert 'success' in page.get_element_attribute(page.first_name_element, "class")
    assert 'success' in page.get_element_attribute(page.last_name_element, "class")
    assert 'success' in page.get_element_attribute(page.address_element, "class")
    assert 'success' in page.get_element_attribute(page.email_element, "class")
    assert 'success' in page.get_element_attribute(page.phone_element, "class")
    assert 'success' in page.get_element_attribute(page.city_element, "class")