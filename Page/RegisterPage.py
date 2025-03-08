from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class RegisterPage(BasePage):
    """1.Navigate to Page from Home Page for Registration of User
           2.Enter the Registration details such as valid Email id and password to register"""
    #Locators for registration on page
    my_account=(By.LINK_TEXT,"My Account")
    reg_email=(By.CSS_SELECTOR,"#reg_email")
    reg_password=(By.CSS_SELECTOR,"#reg_password")
    register_btn=(By.XPATH,"//input[@value='Register']")
    success_response=(By.XPATH,"//p[contains(text(),'Hello')]")
    error_response=(By.XPATH,".//li[contains(text(),'already registered')]")# This is for same user tries to register again
    empty_error_response=(By.XPATH,"//li[contains(text(),'provide a valid email')]")# This is for blank details
    empty_pass_error_response=(By.XPATH,".//li[contains(text(),'enter an account password')]")
    logout=(By.XPATH,"//a[text()='Logout']")

    def click_on_my_account(self):
        return self.click_on_element(self.my_account)
    def enter_reg_email(self,r_email):
        return self.enter_text_into_element(self.reg_email,r_email)
    def enter_reg_pass(self,r_pass):
        return self.enter_text_into_element(self.reg_password,r_pass)
    def click_on_reg_btn(self):
        return self.click_on_element(self.register_btn)
    def check_success_msg(self):
        return self.get_element_text(self.success_response)
    def check_error_msg_same_user(self):
        return self.get_element_text(self.error_response)
    def check_error_msg_blank_details(self):
        return self.get_element_text(self.empty_error_response)
    def check_error_msg_empty_pass(self):
        return self.get_element_text(self.empty_pass_error_response)
    def click_on_logout(self):
        return self.click_on_element(self.logout)

    def do_register_user(self, r_email,r_pass):
        self.driver.implicitly_wait(5)
        self.click_on_my_account()
        self.enter_reg_email(r_email)
        self.enter_reg_pass(r_pass)
        self.click_on_reg_btn()

