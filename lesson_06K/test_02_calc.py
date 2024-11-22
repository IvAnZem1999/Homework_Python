import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()
sleep(5)
element_1 = driver.find_element(By.ID, "delay")
element_1.clear()
element_1.send_keys("45")
element_2 = driver.find_element(By.XPATH, '//span[text()= "7"]').click()
element_3 = driver.find_element(By.XPATH, '//span[text()= "+"]').click()
element_4 = driver.find_element(By.XPATH, '//span[text()= "8"]').click()
element_5 = driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()
waiter = WebDriverWait(driver, 50)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='screen']"), "15"))
assert "15" in driver.find_element(By.CSS_SELECTOR, "div[class='screen']").text