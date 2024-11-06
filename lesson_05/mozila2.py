from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
search_box = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
search_box.send_keys(1000)
sleep(2)
search_box.clear()
sleep(2)
search_box.send_keys(999)