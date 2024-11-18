from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
element = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(element)