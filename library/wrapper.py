from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Wrapper:
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver,10)
    def find_element(self,logical_name):
        if isinstance(logical_name,tuple):
            return self.wait.until(expected_conditions.presence_of_element_located(logical_name))

    def find_elements(self,logical_name):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(logical_name))

    def click_on_element(self,logical_name):
        element = self.wait.until(expected_conditions.element_to_be_clickable(logical_name))
        element.click()

    def send_value(self,logical_name,data):
        element = (self.wait.until(expected_conditions.element_to_be_clickable(logical_name)))
        element.send_keys(data)


