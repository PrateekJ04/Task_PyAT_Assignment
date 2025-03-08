import pytest
import allure
from faker import Faker

from Page.AddressPage import AddressPage
from Page.LoginPage import LoginPage
from Tests.basetest import BaseTest
faker=Faker()

class Test_Address(BaseTest):
    @allure.severity("Critical")
    @allure.title("TC01-Verify that billing address is getting saved with all details")
    @allure.description("Check if billing address is gettig saved with all details")
    @pytest.mark.positive
    def test_address_all_details_billing(self, setup_and_teardown):
        address_page=AddressPage(setup_and_teardown)
        address_page.add_billing_address(self.user,self.password,faker.first_name(),faker.last_name(),faker.company(),faker.email(),faker.random_int(10000000000,99999999999),faker.color_name(),faker.name(),"Mumbai",faker.random_int(100000,9999999))
        assert address_page.get_success_res_text().__contains__("successfully")
        address_page.click_on_logout()

    @allure.severity("Critical")
    @allure.title("TC02-Verify that shipping address is getting saved with all details")
    @allure.description("Check if shipping address is gettig saved with all details")
    @pytest.mark.positive
    def test_address_all_details_shipping(self, setup_and_teardown):
        address_page1 = AddressPage(setup_and_teardown)
        address_page1.add_shipping_address(self.user, self.password, faker.first_name(), faker.last_name(),
                                         faker.company(),street_s=faker.color_name(), apt_s=faker.name(), city_s="Ahmedabad", zipcode_s=faker.random_int(100000, 9999999))
        assert address_page1.get_success_res_text_s().__contains__("successfully")
        address_page1.click_on_logout()