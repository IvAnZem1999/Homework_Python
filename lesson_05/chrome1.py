from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    add_button = driver.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    sleep(3)
    delete_button = driver.find_elements( 
         By.XPATH, '//button[text()="Delete"]')
print(len(delete_button))



