import time

from selenium.webdriver.common.by import By

from Page.BasePage import BasePage
#Locators for Login

class LoginPage(BasePage):
    my_account = (By.LINK_TEXT, "My Account")
    login_email = (By.CSS_SELECTOR, "#username")
    login_password = (By.CSS_SELECTOR, "#password")
    login_btn = (By.XPATH, "//input[@value='Login']")
    success_response = (By.XPATH, "//div/p[contains(text(),'Hello')]")
    invalid_error_response=(By.XPATH,"//li[contains(text(),'A user could not be found with this email address')]")#This is for invalid username and password
    empty_error_response = (By.XPATH, "//li[contains(text(),'Username is required')]")  # This is for blank details
    empty_pass_error_response = (By.XPATH, "//li[contains(text(),'Password is required.')]")
    logout = (By.XPATH, "//a[text()='Logout']")
    lost_your_pass=(By.XPATH,"//a[text()='Lost your password?']")
    lost_pass_user=(By.CSS_SELECTOR,"#user_login")
    reset_pass_btn=(By.XPATH,"//input[@value='Reset Password']")
    pass_reset_success_response=(By.XPATH,"//div[contains(text(),'Password reset email has been sent.')]")


    def click_on_my_account(self):
        return self.click_on_element(self.my_account)

    def enter_login_email(self, l_email):
        return self.enter_text_into_element(self.login_email, l_email)

    def enter_login_pass(self, l_pass):
        return self.enter_text_into_element(self.login_password, l_pass)

    def click_on_login_btn(self):
        return self.click_on_element(self.login_btn)

    def check_success_msg(self):
        return self.get_element_text(self.success_response)

    def check_error_msg_blank_details(self):
        return self.get_element_text(self.empty_error_response)

    def check_error_msg_empty_pass(self):
        return self.get_element_text(self.empty_pass_error_response)
    def check_error_msg_invalid_pass_un(self):
        return self.get_element_text(self.invalid_error_response)

    def click_on_logout(self):
        return self.click_on_element(self.logout)
    def click_on_lost_pass(self):
        return self.click_on_element(self.lost_your_pass)
    def enter_lost_user_email(self,l_mail):
        return self.enter_text_into_element(self.lost_pass_user,l_mail)

    def click_on_reset_pass(self):
        return self.click_on_element(self.reset_pass_btn)

    def get_reset_pass_text(self):
        return self.get_element_text(self.pass_reset_success_response)



    #Below method is for log in
    def do_login_user(self, l_email, l_pass):
        try:
            self.driver.implicitly_wait(5)
            self.click_on_my_account()
            self.enter_login_email(l_email)
            self.enter_login_pass(l_pass)
            self.click_on_login_btn()
            self.driver.implicitly_wait(5)
        except Exception as e:
            print("In Log in method got exception",e)
        finally:
            print("Login is executed")


    # Below method is for forget password
    def do_forgot_pass(self,l_email):
        try:
            self.driver.implicitly_wait(5)
            self.click_on_my_account()
            self.driver.implicitly_wait(5)
            self.click_on_lost_pass()
            self.driver.implicitly_wait(5)
            self.enter_lost_user_email(l_email)
            self.click_on_reset_pass()
            self.driver.implicitly_wait(5)

        except Exception as e:
            print("In forgot Password method got exception",e)
        finally:
            print("Forgot Password is executed")









