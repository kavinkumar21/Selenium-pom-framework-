from time import sleep
from data.ex_reader import logout
from library.wrapper import Wrapper

locators = logout()
class Logout:
    def __init__(self, driver):
        self.driver=driver
        self.wrapper = Wrapper(self.driver)
    def click_dashboard(self):
        self.wrapper.click_on_element(locators['Click_dash_board'])

    def click_profile(self):
        self.wrapper.click_on_element(locators['Click_drop_down'])

    def click_logout(self):
        self.wrapper.click_on_element(locators['Click_logout'])

