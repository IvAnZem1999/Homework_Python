import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
element_1 = driver.find_element(By.ID, "user-name")
element_1.send_keys("standard_user")
element_2 = driver.find_element(By.ID, "password")
element_2.send_keys("secret_sauce")
element_3 = driver.find_element(By.ID, "login-button").click()
element_4 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
element_5 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
element_6 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
element_7 = driver.find_element(By.ID, "shopping_cart_container").click()
element_8 = driver.find_element(By.ID, "checkout").click()
name = driver.find_element(By.ID, "first-name")
name.send_keys("Ivan")
sername = driver.find_element(By.ID, "last-name")
sername.send_keys("Ivanov")
code = driver.find_element(By.ID, "postal-code")
code.send_keys("17634")
element_9 = driver.find_element(By.ID, "continue").click()
element_10 = driver.find_element(By.CSS_SELECTOR, "[data-test=total-label]").text
print(element_10)
assert element_10 == "Total: $58.29"