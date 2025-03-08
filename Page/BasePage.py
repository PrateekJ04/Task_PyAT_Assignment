import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    # These methods are used to perform actions on web elements and also handle dynamic loading part of web element
    def flashing_element(self,element):
        for i in range(1,6):
            # self.driver.execute_script("arguments[0].style.background='yellow'",element)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
            time.sleep(0.1)
            self.driver.execute_script("arguments[0].style.border='3px solid green'", element)
            # self.driver.execute_script("arguments[0].style.background='white',style.border='orange'", element)


    def click_on_element(self, by_locator):

        element=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(by_locator))
        self.flashing_element(element)
        element.click()



    def enter_text_into_element(self, by_locator,textdata):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        self.flashing_element(element)
        element.click()
        element.clear()
        element.send_keys(textdata)

    def get_element_text(self,by_locator):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        self.flashing_element(element)
        return element.text

    def perf_action_move_to_element(self,driver,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action=ActionChains(self.driver)
        action.move_to_element(element)
        self.flashing_element(element)

    def perf_action_double_click(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action=ActionChains(self.driver)
        action.double_click(element).perform()

    def perf_select_from_dropdown(self,by_locator,textdata):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        select=Select(element)
        select.select_by_visible_text(textdata)

    def check_element_isenabled(self,by_locator):
        element= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.flashing_element(element)
        return bool(element)

    def get_title_on_page(self,title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title





