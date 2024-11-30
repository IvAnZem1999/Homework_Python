import pytest
from selenium import webdriver
from Page_calc import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    return CalculatorPage(driver)


def test_slow_calculator(page):
    page.open()
    page.set_delay("45")
    page.click_button(page.button_7)
    page.click_button(page.button_plus)
    page.click_button(page.button_8)
    page.click_button(page.button_equals)
    page.wait_for_result("15")
    assert "15" == page.get_screen_text()

