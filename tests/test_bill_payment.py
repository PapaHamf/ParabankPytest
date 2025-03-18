import time

import pytest
import allure
import random

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from utils.myfaker import MyFaker
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage


class TestOpenAccount(BaseClass):

    @allure.title("Logging in/out the user")
    @pytest.fixture(scope = "function")
    def login_logout(self):
        """
        Logins the user in the app and logs him out after the test.
        :return: List containing the dict w/ the home page object and user data.
        """
        with allure.step("Step 1: Logging in"):
            log = self.get_logger()
            self.driver.get(BasePage.HOME_PAGE)
            # Get the user data from Excel file
            user_data = random.choice(ExcelData.get_excel_data("dataset_customer.xlsx"))
            user_name = user_data["username"]
            password = user_data["password"]
            log.info("Logging the user.")
            # Create the home page object
            home_page = HomePage(self.driver)
            log.info(f"User name: {user_name}")
            home_page.get_username().send_keys(user_name)
            log.info(f"Password: {password}")
            home_page.get_password().send_keys(password)
            log.info("Clicking the login button.")
            side_menu = home_page.get_login_button()
        yield side_menu, user_data
        # Log out the user
        with allure.step("Step 2: Logging out"):
            log.info(f"Logging out the user {user_name}.")
            side_menu.get_log_out_link().click()
            self.driver.delete_all_cookies()

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for bill payment")
    @allure.sub_suite("Positive bill payment tests")
    @allure.tag("Bill Payment", "New payment", "Positive")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 86")
    @allure.description("This test attempts to pay the bill for the utility company.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_bill_payment_postive(self, login_logout):
        """
        Tests the bill payment for the utility company.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Bill Pay link.")
        bill_pay = login_logout[0].get_bill_pay_page()
        # Getting the faker-generated data
        payment_data = MyFaker.bill_data_all_fields(company = "PGNiG")[0]
        data_collection = ExcelData("Bill Payment", "New payment")
        company_name = payment_data["payee"]
        log.info(f"Entering the payee name: {company_name}")
        data_collection.add_data("payee", company_name)
        bill_pay.get_payee_name().send_keys(company_name)
        address = payment_data["payeeaddress"]
        log.info(f"Entering the payee address: {address}")
        data_collection.add_data("payeeaddress", address)
        bill_pay.get_payee_street().send_keys(address)
        city = payment_data["city"]
        log.info(f"Entering the payee city: {city}")
        data_collection.add_data("city", city)
        bill_pay.get_payee_city().send_keys(city)
        state = payment_data["state"]
        log.info(f"Entering the state: {state}")
        data_collection.add_data("state", state)
        bill_pay.get_payee_state().send_keys(state)
        post_code = payment_data["postcode"]
        log.info(f"Entering the post code: {post_code}")
        data_collection.add_data("postcode", post_code)
        bill_pay.get_payee_post_code().send_keys(post_code)
        phone_number = payment_data["phonenumber"]
        log.info(f"Entering the phone number: {phone_number}")
        data_collection.add_data("phonenumber", phone_number)
        bill_pay.get_payee_phonenumber().send_keys(phone_number)
        account_number = payment_data["account"]
        log.info(f"Entering the account number: {account_number}")
        data_collection.add_data("account", account_number)
        bill_pay.get_payee_account_number().send_keys(account_number)
        verify_account = payment_data["verifyaccount"]
        log.info(f"Entering the verify account number: {verify_account}")
        data_collection.add_data("verifyaccount", verify_account)
        bill_pay.get_payee_verify_account().send_keys(verify_account)
        amount = payment_data["amount"]
        log.info(f"Entering the amount: {amount}")
        data_collection.add_data("amount", amount)
        bill_pay.get_payment_amount().send_keys(amount)
        # Select random account from the available list
        account_list = bill_pay.get_list_values(bill_pay.get_source_account())
        acc_no = random.choice(account_list)
        log.info(f"Selecting the account number: {acc_no}")
        data_collection.add_data("sourceaccount", acc_no)
        bill_pay.select_value_from_dropdown_text(bill_pay.get_source_account(), acc_no)
        log.info("Clicking the payment button.")
        bill_pay.get_payment_button().click()
        data_collection.save_data()
        assert bill_pay.get_payment_success_title().text == bill_pay.BILL_PAYMENT_SUCCESS_MSG

