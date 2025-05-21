from time import sleep

from data.ex_reader import emp
from library.action_chains import ActionChain
from pom.pim import get
from library.wrapper import Wrapper

locators = emp()
class EmpList(ActionChain):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.wrapper = Wrapper(self.driver)
    def emp_list(self):
        self.wrapper.click_on_element(locators['open_list'])

    def view_emp(self):
        f = get('f')
        l = get('l')
        for i,j in zip(f,l):
            new = locators['sel_column'][1].format(i, j)
            replace = (locators['sel_column'][0], new)
            sleep(2)
            t_pages = len(self.wrapper.find_elements(locators['emp_pages']))
            for no in range(t_pages):
                pages = self.wrapper.find_elements(locators['emp_pages'])
                pages[no].click()
                sleep(2)
                try:
                    self.mouse_scroll(replace)
                    print('Name Verified')
                    break
                except Exception as e:
                    print('Name not found in this page ', e)
                    continue




