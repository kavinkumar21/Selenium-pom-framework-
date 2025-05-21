from library.wrapper import Wrapper
from data.ex_reader import login
locators = login()
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.wrap_obj=Wrapper(self.driver)
    def enter_username(self):
        self.wrap_obj.send_value(locators['Login_user_name'],'Admin')
    def enter_password(self):
        self.wrap_obj.send_value(locators['Login_password'],'admin123')
    def click_login(self):
        self.wrap_obj.click_on_element(locators['Login_button'])



