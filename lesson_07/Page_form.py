from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

        self.first_name_field = (By.NAME, "first-name")
        self.last_name_field = (By.NAME, "last-name")
        self.address_field = (By.NAME, "address")
        self.zip_code_field = (By.NAME, "zip-code")
        self.city_field = (By.NAME, "city")
        self.country_field = (By.NAME, "country")
        self.email_field = (By.NAME, "e-mail")
        self.phone_field = (By.NAME, "phone")
        self.job_position_field = (By.NAME, "job-position")
        self.company_field = (By.NAME, "company")
        self.submit_button = (By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")
        self.zip_code_element = (By.ID, "zip-code") 
        self.first_name_element = (By.ID, "first-name") 
        self.last_name_element = (By.ID, "last-name") 
        self.address_element = (By.ID, "address")    
        self.email_element = (By.ID, "e-mail")      
        self.phone_element = (By.ID, "phone")      
        self.city_element = (By.ID, "city")        


    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def fill_form(self, first_name, last_name, address, zip_code, city, country, email, phone, job_position, company):
        self.set_field_value(self.first_name_field, first_name)
        self.set_field_value(self.last_name_field, last_name)
        self.set_field_value(self.address_field, address)
        self.set_field_value(self.zip_code_field, zip_code)
        self.set_field_value(self.city_field, city)
        self.set_field_value(self.country_field, country)
        self.set_field_value(self.email_field, email)
        self.set_field_value(self.phone_field, phone)
        self.set_field_value(self.job_position_field, job_position)
        self.set_field_value(self.company_field, company)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def set_field_value(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_element_attribute(self, locator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)