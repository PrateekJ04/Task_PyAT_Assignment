import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Page.BasePage import BasePage
from Page.LoginPage import LoginPage


class AddressPage(BasePage):
    # Locators for Address Page
    #Note: Locators name ending with "_man" are mandatory fields
    addresses_link=(By.LINK_TEXT,"Addresses")
    billing_add_edit=(By.XPATH,"//h3[text()='Billing Address']/following-sibling::a")
    first_name_man=(By.XPATH,".//input[@id='billing_first_name']")
    last_name_man=(By.XPATH,".//input[@id='billing_last_name']")
    cmpny_name=(By.XPATH,".//input[@id='billing_company']")
    email_add_man=(By.XPATH,".//input[@id='billing_email']")
    phone_man=(By.XPATH,".//input[@id='billing_phone']")
    country_input_man=(By.XPATH,".//div/div[@class='select2-search']/input[@type='text']")
    country_man=(By.XPATH,"//label[text()='Country ']/following-sibling::div")
    select_contry=(By.XPATH,"//ul/li/div")
    address_street_man=(By.XPATH,".//input[@placeholder='Street address']")
    address_apt_man=(By.XPATH,".//input[contains(@placeholder,'Apartment')]")
    city_man=(By.XPATH,".//input[@id='billing_city']")
    state_sel_man=(By.XPATH,".//p[@id='billing_state_field']/select")
    zip_man=(By.XPATH,".//input[@id='billing_postcode']")
    save_address_btn=(By.XPATH,"//p/input[@value='Save Address']")
    success_response=(By.XPATH,"//div[@class='woocommerce-message']")
    logout = (By.XPATH, "//a[text()='Logout']")
#=====================Below are the locators for shipping address=================="""
    shipping_add_edit = (By.XPATH, "//h3[text()='Shipping Address']/following-sibling::a")
    first_name_man_s = (By.XPATH, ".//input[@id='shipping_first_name']")
    last_name_man_s = (By.XPATH, ".//input[@id='shipping_last_name']")
    cmpny_name_s = (By.XPATH, ".//input[@id='shipping_company']")
    email_add_man_s = (By.XPATH, ".//input[@id='shipping_email']")
    phone_man_s = (By.XPATH, ".//input[@id='shipping_phone']")
    address_street_man_s = (By.XPATH, ".//input[@name='shipping_address_1']")
    address_apt_man_s = (By.XPATH, ".//input[@name='shipping_address_2']")
    city_man_s = (By.XPATH, ".//input[@id='shipping_city']")
    zip_man_s = (By.XPATH, ".//input[@id='shipping_postcode']")
    save_address_btn_s = (By.XPATH, "//p/input[@value='Save Address']")
    success_response_s = (By.XPATH, "//div[@class='woocommerce-message']")
    # """============================================================================"""
    def click_address_link(self):
        return self.click_on_element(self.addresses_link)
    def click_on_billing_add_edit(self):
        return self.click_on_element(self.billing_add_edit)
    def enter_first_name(self, firstname):
        return self.enter_text_into_element(self.first_name_man,firstname)
    def enter_last_name(self, lastname):
        return self.enter_text_into_element(self.last_name_man,lastname)
    def enter_company_name(self, compname):
        return self.enter_text_into_element(self.cmpny_name,compname)
    def enter_email(self, email):
        return self.enter_text_into_element(self.email_add_man,email)
    def enter_phone(self, phone):
        return self.enter_text_into_element(self.phone_man,phone)
    def enter_country_name(self, country):
        self.click_on_element(self.country_man)
        self.enter_text_into_element(self.country_input_man,country)
        self.click_on_element(self.select_contry)
        return self.click_on_element(self.select_contry)
    def enter_addressline1(self,street):
        self.driver.execute_script("window.scrollTo(0,350)")
        return self.enter_text_into_element(self.address_street_man,street)
    def enter_addressline2(self, apt):
        return self.enter_text_into_element(self.address_apt_man, apt)
    def enter_city(self, city):
        return self.enter_text_into_element(self.city_man, city)
    def enter_state(self,state):
        self.click_on_element(self.state_sel_man)
        return self.perf_select_from_dropdown(self.state_sel_man,state)
    def enter_zip(self,zipcode):
        return self.enter_text_into_element(self.zip_man,zipcode)
    def click_save_address(self):
        return self.click_on_element(self.save_address_btn)
    def get_success_res_text(self):
        return self.get_element_text(self.success_response)
    def click_on_logout(self):
        return self.click_on_element(self.logout)

    # =====================Below are the methods for shipping address=================="""
    def click_on_shipping_add_edit(self):
        return self.click_on_element(self.shipping_add_edit)
    def enter_first_name_s(self, firstname_s):
        return self.enter_text_into_element(self.first_name_man_s,firstname_s)
    def enter_last_name_s(self, lastname_s):
        return self.enter_text_into_element(self.last_name_man_s,lastname_s)
    def enter_company_name_s(self, compname_s):
        return self.enter_text_into_element(self.cmpny_name_s,compname_s)
    def enter_addressline1_s(self,street_s):
        self.driver.execute_script("window.scrollTo(0,350)")
        return self.enter_text_into_element(self.address_street_man_s,street_s)
    def enter_addressline2_s(self, apt_s):
        return self.enter_text_into_element(self.address_apt_man_s, apt_s)
    def enter_city_s(self, city_s):
        return self.enter_text_into_element(self.city_man_s, city_s)
    def enter_zip_s(self,zipcode_s):
        return self.enter_text_into_element(self.zip_man_s,zipcode_s)
    def click_save_address_s(self):
        return self.click_on_element(self.save_address_btn_s)
    def get_success_res_text_s(self):
        return self.get_element_text(self.success_response_s)
    # """================================================================================"""
    def add_billing_address(self, l_email, l_pass, firstname, lastname, companyname, emailad, phone,
                            street, apt, city,zipcode):
        try:
            login=LoginPage(self.driver)
            login.do_login_user(l_email,l_pass)
            self.driver.implicitly_wait(5)
            self.click_address_link()
            self.driver.implicitly_wait(5)
            self.click_on_billing_add_edit()
            self.driver.implicitly_wait(1)
            self.enter_first_name(firstname)
            self.enter_last_name(lastname)
            self.enter_company_name(companyname)
            self.enter_email(emailad)
            self.enter_phone(phone)
            self.driver.implicitly_wait(5)
            self.enter_addressline1(street)
            self.enter_addressline2(apt)
            self.enter_city(city)
            self.enter_zip(zipcode)
            self.click_save_address()
        except Exception as e:
            print(e)
        finally:
            print(f"add_billing_address is executed")


        #=============================================================================================
        #Below code is for shipping address

    def add_shipping_address(self, l_email_s, l_pass_s, firstname_s, lastname_s, companyname_s,
                                street_s, apt_s, city_s, zipcode_s):
        try:
            login = LoginPage(self.driver)
            login.do_login_user(l_email_s, l_pass_s)
            self.driver.implicitly_wait(5)
            self.click_address_link()
            self.driver.implicitly_wait(5)
            self.click_on_shipping_add_edit()
            self.driver.implicitly_wait(1)
            self.enter_first_name_s(firstname_s)
            self.enter_last_name_s(lastname_s)
            self.enter_company_name_s(companyname_s)
            self.driver.implicitly_wait(3)
            self.enter_addressline1_s(street_s)
            self.enter_addressline2_s(apt_s)
            self.enter_city_s(city_s)
            self.enter_zip_s(zipcode_s)
            self.click_save_address_s()
        except Exception as e:
            print(e)
        finally:
            print(f"add_shipping_address is executed")






