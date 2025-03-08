from unittest import expectedFailure

import allure
import allure_pytest
import pytest

from Page.LoginPage import LoginPage
from Tests.basetest import BaseTest


class Test_Login(BaseTest):
    @allure.severity("Critical")
    @allure.title("TC01-Verify log in with valid email and password")
    @allure.description("Check if login is successful with valid credentials")
    @pytest.mark.positive
    def test_valid_Login(self, setup_and_teardown):
        login=LoginPage(driver=setup_and_teardown)
        login.do_login_user(self.user,self.password)
        title_of_page=self.driver.title
        exp_res=login.check_success_msg()
        assert title_of_page.__contains__("My Account")
        assert exp_res.__contains__("Hello")
        login.click_on_logout()



    @allure.title("TC02-Verify log in with invalid email and password")
    @allure.description("Check if login is not successful with invalid credentials")
    @pytest.mark.negative
    def test_invalid_Login01(self, setup_and_teardown):
        login = LoginPage(driver=setup_and_teardown)
        login.do_login_user("testpython@test.com", "Pass@123")
        expected_error = login.check_error_msg_invalid_pass_un()
        assert expected_error.__contains__("A user could not be found")


    @allure.title("TC03-Verify log in with valid email and blank password")
    @allure.description("Check if login is not successful with invalid credentials")
    @pytest.mark.negative
    def test_invalid_Login02(self, setup_and_teardown):
        login = LoginPage(driver=setup_and_teardown)
        login.do_login_user("testpython@test.com", "")
        expected_error = login.check_error_msg_empty_pass()
        assert expected_error.__contains__("Password")

    @allure.title("TC04-Verify log in with empty email and password")
    @allure.description("Check if login is not successful with invalid credentials")
    @pytest.mark.negative
    def test_invalid_Login03(self, setup_and_teardown):
        login = LoginPage(driver=setup_and_teardown)
        login.do_login_user("testpython@test.com", "TestCode@123")
        expected_error = login.check_error_msg_invalid_pass_un()
        assert expected_error.__contains__("A user could not be found")

    @allure.title("TC05-Verify forgot password link[Lost your password?]")
    @allure.description("Check whether the page is navigating and getting password reset message on UI")
    @pytest.mark.positive
    def test_lost_password_link_Login(self, setup_and_teardown):
        resetpass=LoginPage(driver=setup_and_teardown)
        resetpass.do_forgot_pass(self.user)
        exp_res=resetpass.get_reset_pass_text()
        assert exp_res.__contains__("Password reset email has been sent")
