import pytest
from selenium import webdriver
from Page_shop import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    return ShopPage(driver)

def test_saucedemo_checkout(page):
    page.open()
    page.login("standard_user", "secret_sauce")
    page.add_to_cart(page.backpack_button, page.tshirt_button, page.onesie_button)
    page.proceed_to_checkout()
    page.fill_checkout_info("Ivan", "Ivanov", "17634")
    total = page.get_total()
    assert total == "Total: $58.29"

