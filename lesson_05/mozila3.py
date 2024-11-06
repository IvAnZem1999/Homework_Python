from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
input_1 = driver.find_element(By.ID, 'username')
input_1.send_keys("tomsmith")
input_2 = driver.find_element(By.ID, 'password')
input_2.send_keys("SuperSecretPassword!")
input_3 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()