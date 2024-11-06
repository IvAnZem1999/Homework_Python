from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
element_1 = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element_1.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
element_2 = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(element_2)
