from time import sleep
from library.wrapper import Wrapper
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ActionChain:
    def __init__(self, driver):
        self.driver = driver
        self.ac_ob = ActionChains(self.driver)
        self.wait = WebDriverWait(driver,5)
        self.wrapper = Wrapper(self.driver)
    def mouse_hover(self, locator):
        element = self.wrapper.find_element(locator)
        self.ac_ob.move_to_element(element).perform()
        sleep(2)
    def mouse_click(self,locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        value = self.wrapper.find_element(locator)
        self.ac_ob.move_to_element(value).click().perform()

    def mouse_scroll(self,locator):
        element = self.wrapper.find_element(locator)
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.ac_ob.scroll_to_element(element).perform()
        sleep(5)

    def back_space(self,locator,e_id):
        self.mouse_click(locator)
        self.ac_ob.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(e_id).perform()


    # def mouse_click(self,locator):
    #     # for _ in range(2):
    #     #     try:
    #             # self.wait.until(expected_conditions.visibility_of_element_located(locator))
    #             self.wait.until(expected_conditions.element_to_be_clickable(locator))
    #             value = self.wrapper.find_element(locator)
    #             # if value:
    #             self.ac_ob.move_to_element(value).click().perform()
    #         # except StaleElementReferenceException:
    #         #     continue