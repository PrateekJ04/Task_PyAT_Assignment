import allure
import allure_pytest
import pytest
from faker import Faker
from Page.LoginPage import LoginPage
from Page.RegisterPage import RegisterPage
from Tests.basetest import BaseTest

import random


class Test_Registration(BaseTest):
    @allure.severity("Critical")
    @allure.title("TC01-Verify registration with valid email and valid password")
    @allure.description("Check if registration is successful with valid details")
    @pytest.mark.positive
    def test_valid_Registration(self, setup_and_teardown):
        register = RegisterPage(driver=setup_and_teardown)
        newly_generated_int=str(random.randint(1,300))
        gen_email=f"patprateek{newly_generated_int}@yopmail.com"
        with open ("users.txt","a") as file:
            file.write(gen_email)
        register.do_register_user(gen_email, "TestCode@123")
        title_of_page = self.driver.title
        exp_res = register.check_success_msg()
        assert title_of_page.__contains__("My Account")
        assert exp_res.__contains__("Hello")
        register.click_on_logout()

    @allure.title("TC02-Verify registration with same user")
    @allure.description("Check if registration is not successful with same details")
    @pytest.mark.negative
    def test_invalid_Register01(self, setup_and_teardown):
        register = RegisterPage(driver=setup_and_teardown)
        register.do_register_user(f"patprateek@yopmail.com", "TestCode@123")
        title_of_page = self.driver.title
        exp_res = register.check_error_msg_same_user()
        assert title_of_page.__contains__("My Account")
        assert exp_res.__contains__("already registered")



    @allure.title("TC03-Verify registration with empty email and password")
    @allure.description("Check if registration is not successful with invalid details")
    @pytest.mark.negative
    def test_invalid_Register03(self, setup_and_teardown):
        register = RegisterPage(driver=setup_and_teardown)
        register.do_register_user(f"", "")
        title_of_page = self.driver.title
        exp_res = register.check_error_msg_blank_details()
        assert title_of_page.__contains__("My Account")
        assert exp_res.__contains__("provide a valid email")

