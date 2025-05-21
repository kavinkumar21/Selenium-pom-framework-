from time import sleep
from random import randint
from library.action_chains import ActionChain
from library.wrapper import Wrapper
from data.ex_reader import pim
locators = pim()
f_n = []
l_n = []
class Pim(ActionChain):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wrapper = Wrapper(self.driver)

    def select_pim(self):
        self.mouse_hover(locators['Click_pim'])
        self.mouse_click(locators['Click_pim'])

    def add_emp(self):
        self.wrapper.click_on_element(locators['add_emp'])

    def f_name(self,f_name):
        self.wrapper.send_value(locators['first_name'],f_name)
        f_n.append(f_name)

    def l_name(self,l_name):
        self.wrapper.send_value(locators['last_name'],l_name)
        l_n.append(l_name)
    def e_id(self):
        value =randint(0000,9999)
        self.back_space(locators['emp_id'],value)
    def save(self):
        self.wrapper.click_on_element(locators['save_btn'])
        sleep(1)

    def add_more(self):
        self.wrapper.click_on_element(locators['add_m_emp'])
def get(v):
    if v == 'f':
        return f_n
    else:
        return l_n
