import time
import pytest
import random

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from utils.baseclass import BaseClass
from pageobjects.homepage import HomePage
from pageobjects.forgotloginpage import ForgotLoginPage
from pageobjects.registerpage import RegisterPage
from pageobjects.openaccountpage import OpenAccountPage
from pageobjects.requestloanpage import RequestLoanPage
from pageobjects.transferpage import TransferPage

class TestHomePage(BaseClass):
    driver: Chrome

    @pytest.mark.skip
    def test_login(self):
        """
        Tests the login forms field.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BaseClass.HOMEPAGE)
        home_page = HomePage(self.driver)
        log.info("Test case no 1")
        log.info("Testing the user login form.")
        user_name = faker.user_name()
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        password = faker.password()
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        print(home_page.get_login_error().text)
        print(home_page.get_error_msg().text)
        # forgot_login = home_page.get_forgot_login()
        time.sleep(5)

    @pytest.mark.skip
    def test_forgot_login(self):
        """
        Tests the forgot login form fields.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BaseClass.FORGOT_LOGIN)
        forgot_login = ForgotLoginPage(self.driver)
        log.info("Test case no 2")
        log.info("Testing the forgot login form.")
        first_name = faker.first_name()
        log.info(f"First name: {first_name}")
        forgot_login.get_first_name().send_keys(first_name)
        last_name = faker.last_name()
        log.info(f"Last name: {last_name}")
        forgot_login.get_last_name().send_keys(last_name)
        address = faker.street_address()
        log.info(f"Address: {address}")
        forgot_login.get_address_street().send_keys(address)
        city = faker.city()
        log.info(f"City: {city}")
        forgot_login.get_address_city().send_keys(city)
        state = faker.administrative_unit()
        log.info(f"State: {state}")
        forgot_login.get_address_state().send_keys(state)
        post_code = faker.postalcode()
        log.info(f"Post code: {post_code}")
        forgot_login.get_address_post_code().send_keys(post_code)
        ssn = faker.ssn()
        log.info(f"SSN: {ssn}")
        forgot_login.get_social_security_number().send_keys(ssn)
        log.info("Clicking the find my login button.")
        forgot_login.get_find_login_button().click()
        print(forgot_login.get_lookup_error().text)
        time.sleep(5)

    @pytest.mark.skip
    def test_register_page(self):
        """
        Tests the register page form fields.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BaseClass.REGISTER)
        register_page = RegisterPage(self.driver)
        log.info("Test case no 3")
        log.info("Testing the register the user form.")
        first_name = faker.first_name()
        log.info(f"First name: {first_name}")
        register_page.get_first_name().send_keys(first_name)
        last_name = faker.last_name()
        log.info(f"Last name: {last_name}")
        register_page.get_last_name().send_keys(last_name)
        address = faker.street_address()
        log.info(f"Address: {address}")
        register_page.get_address_street().send_keys(address)
        city = faker.city()
        log.info(f"City: {city}")
        register_page.get_address_city().send_keys(city)
        state = faker.administrative_unit()
        log.info(f"State: {state}")
        register_page.get_address_state().send_keys(state)
        post_code = faker.postalcode()
        log.info(f"Post code: {post_code}")
        register_page.get_address_post_code().send_keys(post_code)
        phone_number = faker.phone_number()
        log.info(f"Phone number: {phone_number}")
        register_page.get_phone_number().send_keys(phone_number)
        ssn = faker.ssn()
        log.info(f"SSN: {ssn}")
        register_page.get_social_security_number().send_keys(ssn)
        user_name = faker.user_name()
        log.info(f"User name: {user_name}")
        register_page.get_username().send_keys(user_name)
        password = faker.password()
        log.info(f"Password: {password}")
        register_page.get_password().send_keys(password)
        log.info(f"Confirm password: {password}")
        register_page.get_confirm_password().send_keys(password)
        log.info("Clicking the register button.")
        register_page.get_register_button().click()
        print(register_page.get_successful_registration().text)
        time.sleep(5)

    @pytest.mark.skip
    def test_openaccount_page(self):
        """
        Tests the open account page fields.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BaseClass.HOMEPAGE)
        # Login data from the previous test case
        # Move the login to the base class?
        user_name = "ma_tre"
        password = "password"
        home_page = HomePage(self.driver)
        log.info("Test case no 4")
        log.info("Testing the open account page.")
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        log.info("Opening the Open account page.")
        self.driver.get(BaseClass.OPEN_ACCOUNT)
        open_account_page = OpenAccountPage(self.driver)
        log.info("Selecting the account type: SAVINGS")
        self.select_value_from_dropdown_text(open_account_page.get_account_type(), "SAVINGS")
        log.info("Selecting the account number.")
        # Move this to the utils?
        # Maybe add the get_source_account method to select one random account
        accounts_list = open_account_page.get_source_accounts()
        acc_nos = []
        for account in accounts_list.find_elements(By.TAG_NAME, "option"):
            acc_nos.append(account.text)
        # Select random account number
        acc_no = random.choice(acc_nos)
        log.info(f"Account number: {acc_no}")
        self.select_value_from_dropdown_text(accounts_list, acc_no)
        # Select random account number by index
        index = random.randint(0, len(acc_nos)+1)
        log.info(f"Selected list index: {index}")
        # self.select_value_from_dropdown_index(accounts_list, index)
        log.info("Opening the new account")
        open_account_page.get_open_account_button().click()
        print(open_account_page.get_account_opened_msg().text)
        activity_page = open_account_page.get_new_account_id()
        time.sleep(2)

    @pytest.mark.skip
    def test_request_loan_page(self):
        """
        Tests the request loan page.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BaseClass.HOMEPAGE)
        # Login data from the previous test case
        # Move the login to the base class?
        user_name = "ma_tre"
        password = "password"
        home_page = HomePage(self.driver)
        log.info("Test case no 5")
        log.info("Testing the request loan page.")
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        log.info("Opening the Request loan page.")
        self.driver.get(BaseClass.REQUEST_LOAN)
        request_loan_page = RequestLoanPage(self.driver)
        loan_amount = random.randint(0, 100000)
        log.info(f"Loan amount: {loan_amount}")
        request_loan_page.get_loan_amount().send_keys(loan_amount)
        down_payment = loan_amount * 0.10
        log.info(f"Down payment: {down_payment}")
        request_loan_page.get_down_payment_amount().send_keys(down_payment)
        log.info("Clicking the apply button.")
        request_loan_page.get_apply_button().click()
        print(request_loan_page.get_loan_status().text)
        activity_page = request_loan_page.get_loan_accout_id()
        time.sleep(3)

    def test_transfer_page(self):
        """
        Tests the transfer funds page.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BaseClass.HOMEPAGE)
        # Login data from the previous test case
        # Move the login to the base class?
        user_name = "ma_tre"
        password = "password"
        home_page = HomePage(self.driver)
        log.info("Test case no 6")
        log.info("Testing the request loan page.")
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        log.info("Opening the transfer funds page.")
        self.driver.get(BaseClass.TRANSFER_FUNDS)
        transfer_funds_page = TransferPage(self.driver)
        amount = random.randint(0, 10000)
        log.info(f"Amount: {amount}")
        transfer_funds_page.get_amount().send_keys(amount)
        source_accounts_list = transfer_funds_page.get_source_accounts()
        src_acc_nos = []
        for account in source_accounts_list.find_elements(By.TAG_NAME, "option"):
            src_acc_nos.append(account.text)
        # Possible test case, selecting source account should remove it from the target list
        # Do the pop on the list and assert it is the same as target
        src_acc_no = random.choice(src_acc_nos)
        log.info(f"Selecting the source account number: {src_acc_no}")
        self.select_value_from_dropdown_text(source_accounts_list, src_acc_no)
        target_accounts_list = transfer_funds_page.get_target_accounts()
        trg_acc_nos = []
        for account in target_accounts_list.find_elements(By.TAG_NAME, "option"):
            trg_acc_nos.append(account.text)
        trg_acc_nos.pop(trg_acc_nos.index(src_acc_no))
        trg_acc_no = random.choice(trg_acc_nos)
        log.info(f"Selecting the target account number: {trg_acc_no}")
        self.select_value_from_dropdown_text(target_accounts_list, trg_acc_no)
        transfer_funds_page.get_transfer_button().click()
        # Is not displayed on the console?
        print(transfer_funds_page.get_transfer_complete().text)
        # Another test case, check if the numbers on the transfer complete match w/ the selected from the list.
        print(transfer_funds_page.get_amount_result().text)
        time.sleep(3)



