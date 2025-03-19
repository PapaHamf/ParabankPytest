import pytest
import allure
import random
import re

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
        src_acc_no = random.choice(account_list)
        log.info(f"Selecting the account number: {src_acc_no}")
        data_collection.add_data("sourceaccount", src_acc_no)
        bill_pay.select_value_from_dropdown_text(bill_pay.get_source_account(), src_acc_no)
        log.info("Clicking the payment button.")
        bill_pay.get_payment_button().click()
        data_collection.save_data()
        assert bill_pay.get_payment_success_title().text == bill_pay.BILL_PAYMENT_SUCCESS_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for bill payment")
    @allure.sub_suite("Negative bill payment tests")
    @allure.tag("Bill Payment", "New payment", "Negative")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 87")
    @allure.description("This test attempts to pay the bill to the random company with a negative amount.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_bill_payment_negative_amount(self, login_logout):
        """
        Tests the bill payment to the random company w/ negative amount.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Bill Pay link.")
        bill_pay = login_logout[0].get_bill_pay_page()
        # Getting the faker-generated data
        payment_data = MyFaker.bill_data_all_fields()[0]
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
        amount = "-0.01"
        log.info(f"Entering the amount: {amount}")
        data_collection.add_data("amount", amount)
        bill_pay.get_payment_amount().send_keys(amount)
        # Select random account from the available list
        account_list = bill_pay.get_list_values(bill_pay.get_source_account())
        src_acc_no = random.choice(account_list)
        log.info(f"Selecting the account number: {src_acc_no}")
        data_collection.add_data("sourceaccount", src_acc_no)
        data_collection.save_data()
        bill_pay.select_value_from_dropdown_text(bill_pay.get_source_account(), src_acc_no)
        log.info("Clicking the payment button.")
        bill_pay.get_payment_button().click()
        assert bill_pay.get_payee_amount_invalid_error().text == bill_pay.BILL_PAYMENT_INVALID_AMOUNT

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for bill payment")
    @allure.sub_suite("Positive bill payment tests")
    @allure.tag("Bill Payment", "New payment", "Positive", "Verify debit")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 88")
    @allure.description("This test attempts to pay the bill to the random company and verifies if the"
                        " source account is debited correctly.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_bill_payment_verify_debit(self, login_logout):
        """
        Tests the bill payment to the random company and verifies the debit on source account.
        :return:
        """
        log = self.get_logger()
        with allure.step("Step 1: Complete the bill payment"):
            log.info("Clicking the Bill Pay link.")
            bill_pay = login_logout[0].get_bill_pay_page()
            # Getting the faker-generated data
            payment_data = MyFaker.bill_data_all_fields()[0]
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
            amount = str(payment_data["amount"])
            log.info(f"Entering the amount: {amount}")
            data_collection.add_data("amount", amount)
            bill_pay.get_payment_amount().send_keys(amount)
            # Select random account from the available list
            account_list = bill_pay.get_list_values(bill_pay.get_source_account())
            src_acc_no = random.choice(account_list)
            log.info(f"Selecting the account number: {src_acc_no}")
            data_collection.add_data("sourceaccount", src_acc_no)
            bill_pay.select_value_from_dropdown_text(bill_pay.get_source_account(), src_acc_no)
            log.info("Clicking the payment button.")
            bill_pay.get_payment_button().click()
            data_collection.save_data()
        with allure.step("Step 2: Verify the bill payment success"):
            assert bill_pay.get_payment_success_title().text == bill_pay.BILL_PAYMENT_SUCCESS_MSG
        with allure.step("Step 3: Verify the debit on the source account"):
            log.info("Clicking the Accounts Overview link.")
            accounts_overview = login_logout[0].get_accounts_overview_page()
            log.info(f"Clicking the source account link.")
            activity_page = accounts_overview.select_account_number(src_acc_no)
            log.info("Selecting the Debit from the Type list.")
            activity_page.select_value_from_dropdown_text(activity_page.get_activity_type(), "Debit")
            log.info("Clicking the Go button.")
            activity_page.get_activity_button().click()
            transaction = activity_page.get_transaction_by_index(-1)
            log.info(f"Verifying if the transaction name is {activity_page.BILL_PAYMENT + company_name}")
            assert transaction[1] == activity_page.BILL_PAYMENT + company_name
            log.info(f"Verifying if the transaction amount is {amount}.")
            assert str(transaction[2]).split(".")[0] == amount

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for bill payment")
    @allure.sub_suite("Positive bill payment tests")
    @allure.tag("Bill Payment", "New payment", "Positive", "Verify account")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 89")
    @allure.description("This test attempts to pay the bill to the random company and verifies if the"
                        " source account and amount are displayed correctly.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_bill_payment_verify_payment(self, login_logout):
        """
        Tests the bill payment to the random company and verifies the source account and amount are correct.
        :return:
        """
        log = self.get_logger()
        with allure.step("Step 1: Complete the bill payment"):
            log.info("Clicking the Bill Pay link.")
            bill_pay = login_logout[0].get_bill_pay_page()
            # Getting the faker-generated data
            payment_data = MyFaker.bill_data_all_fields()[0]
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
            amount = str(payment_data["amount"])
            log.info(f"Entering the amount: {amount}")
            data_collection.add_data("amount", amount)
            bill_pay.get_payment_amount().send_keys(amount)
            # Select random account from the available list
            account_list = bill_pay.get_list_values(bill_pay.get_source_account())
            src_acc_no = random.choice(account_list)
            log.info(f"Selecting the account number: {src_acc_no}")
            data_collection.add_data("sourceaccount", src_acc_no)
            bill_pay.select_value_from_dropdown_text(bill_pay.get_source_account(), src_acc_no)
            log.info("Clicking the payment button.")
            bill_pay.get_payment_button().click()
            data_collection.save_data()
        with allure.step("Step 2: Verify the bill payment success"):
            assert bill_pay.get_payment_success_title().text == bill_pay.BILL_PAYMENT_SUCCESS_MSG
        with allure.step("Step 3: Verify the source account and amount"):
            log.info(f"Verifying if the account number is {src_acc_no}")
            assert bill_pay.get_success_account().text == src_acc_no
            log.info(f"Verifying if the payment amount is {amount}.")
            assert int(float(re.sub(r"[^0-9.]", "", bill_pay.get_success_amount().text))) == int(amount)