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
from pageobjects.updateprofilepage import UpdateProfilePage
from pageobjects.accountoverviewpage import AccountOverview
from pageobjects.activitypage import ActivityPage
from pageobjects.adminpage import AdminPage

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
        # Check if the 20% down payment from the settings is respected (turn into TC)
        down_payment = loan_amount * 0.10
        log.info(f"Down payment: {down_payment}")
        request_loan_page.get_down_payment_amount().send_keys(down_payment)
        log.info("Clicking the apply button.")
        request_loan_page.get_apply_button().click()
        print(request_loan_page.get_loan_status().text)
        activity_page = request_loan_page.get_loan_accout_id()
        time.sleep(3)

    @pytest.mark.skip
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
        log.info("Clicking the transfer button.")
        transfer_funds_page.get_transfer_button().click()
        # Is not displayed on the console?
        print(transfer_funds_page.get_transfer_complete().text)
        # Another test case, check if the numbers on the transfer complete match w/ the selected from the list.
        print(transfer_funds_page.get_amount_result().text)
        time.sleep(3)

    @pytest.mark.skip
    def test_update_profile_page(self):
        """
        Tests the update profile page.
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
        log.info("Test case no 7")
        log.info("Testing the update profile page.")
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        log.info("Opening the update profile page.")
        self.driver.get(BaseClass.UPDATE_INFO)
        update_profile_page = UpdateProfilePage(self.driver)
        first_name = faker.first_name()
        log.info(f"First name: {first_name}")
        update_profile_page.get_first_name().clear()
        update_profile_page.get_first_name().send_keys(first_name)
        last_name = faker.last_name()
        log.info(f"Last name: {last_name}")
        update_profile_page.get_last_name().clear()
        update_profile_page.get_last_name().send_keys(last_name)
        address = faker.street_address()
        log.info(f"Address: {address}")
        update_profile_page.get_address_street().clear()
        update_profile_page.get_address_street().send_keys(address)
        city = faker.city()
        log.info(f"City: {city}")
        update_profile_page.get_address_city().clear()
        update_profile_page.get_address_city().send_keys(city)
        state = faker.administrative_unit()
        log.info(f"State: {state}")
        update_profile_page.get_address_state().clear()
        update_profile_page.get_address_state().send_keys(state)
        post_code = faker.postalcode()
        log.info(f"Post code: {post_code}")
        update_profile_page.get_address_post_code().clear()
        update_profile_page.get_address_post_code().send_keys(post_code)
        phone_number = faker.phone_number()
        log.info(f"Phone number: {phone_number}")
        update_profile_page.get_phone_number().clear()
        update_profile_page.get_phone_number().send_keys(phone_number)
        log.info("Clicking the update profile button.")
        update_profile_page.get_update_button().click()
        print(update_profile_page.get_successful_update().text)
        time.sleep(3)

    @pytest.mark.skip
    def test_account_overview_page(self):
        """
        Tests the account overview page.
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
        log.info("Test case no 8")
        log.info("Testing the update profile page.")
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        log.info("Opening the update profile page.")
        self.driver.get(BaseClass.ACCOUNT_OVERVIEW)
        account_overview_page = AccountOverview(self.driver)
        log.info("Getting the account numbers list.")
        account_nos_list = account_overview_page.get_account_numbers()
        acc_nos = []
        for account in account_nos_list:
            acc_nos.append(account.text)
        log.info("Getting the account balances list.")
        account_balances_list = account_overview_page.get_account_balances()
        acc_bal = []
        for balance in account_balances_list:
            acc_bal.append(balance.text)
        log.info("Getting the account available amounts list.")
        account_available_amounts_list = account_overview_page.get_available_amounts()
        acc_amt = []
        for amount in account_available_amounts_list:
            acc_amt.append(amount.text)
        print("\nTotal: ")
        print(account_overview_page.get_total_amount().text)
        print(f"\nBalance: {account_overview_page.get_account_balance(random.choice(acc_nos)).text}")
        time.sleep(1)

    @pytest.mark.skip
    def test_activity_page(self):
        """
        Tests the activity page.
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
        log.info("Test case no 9")
        log.info("Testing the update profile page.")
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        log.info("Opening the update profile page.")
        self.driver.get(BaseClass.ACCOUNT_OVERVIEW)
        account_overview_page = AccountOverview(self.driver)
        log.info("Getting the account numbers list.")
        account_nos_list = account_overview_page.get_account_numbers()
        acc_nos = []
        for account in account_nos_list:
            acc_nos.append(account.text)
        account_no = random.choice(acc_nos)
        log.info(f"Opening the activity page for the account no: {account_no}")
        # self.driver.get(BaseClass.ACTIVITY + f"?id={account_no}")
        self.driver.get(BaseClass.ACTIVITY + f"?id=13566")
        activity_page = ActivityPage(self.driver)
        print(activity_page.get_account_number().text)
        print(activity_page.get_account_type().text)
        print(activity_page.get_account_balance().text)
        print(activity_page.get_available_amount().text)
        # log.info("Selecting the activity period: January")
        # self.select_value_from_dropdown_text(activity_page.get_activity_period(), "January")
        # log.info("Selecting the activity type: Debit")
        # self.select_value_from_dropdown_text(activity_page.get_activity_type(), "Credit")
        # log.info("Clicking the Go button.")
        # activity_page.get_activity_button().click()
        # log.info("Displaying the transactions")
        # transaction_names = activity_page.get_transaction_dates()
        # for transaction in transaction_names:
        #     print(transaction.text)
        trans = activity_page.get_transaction_link_by_text("Down Payment")
        trans_id = trans.get_attribute("href").split("=")[1]
        log.info(f"Retrieving the debit value for transaction {trans_id}")
        print(activity_page.get_transaction_debit_by_name("Down Payment").text)
        log.info(f"Retrieving the credit value for transaction {trans_id}")
        print(activity_page.get_transaction_credit_by_name("Down Payment").text)
        log.info(f"Clicking the transaction link w/ id: {trans_id}")
        activity_page.get_transaction_link_by_text("Down Payment").click()
        time.sleep(5)

    def test_admin_page(self):
        """
        Tests the admin page.
        :return:
        """
        # Does not require the log in process.
        log = self.get_logger()
        log.info("Test case no 10")
        log.info("Testing the admin page.")
        self.driver.get(BaseClass.ADMIN_PAGE)
        admin_page = AdminPage(self.driver)
        admin_page.get_clean_database()
        log.info("Filling in the initial balance field. Value: 50000")
        admin_page.get_initial_balance().clear()
        admin_page.get_initial_balance().send_keys("50000")
        log.info("Filling in the minimum balance field. Value: 5000")
        admin_page.get_minimum_balance().clear()
        admin_page.get_minimum_balance().send_keys("5000")
        log.info("Selecting the SOAP access mode.")
        admin_page.get_access_mode_soap().click()
        log.info("Selecting the rest JSON access mode.")
        admin_page.get_access_mode_restJSON().click()
        log.info("Selecting the JDBC access mode.")
        admin_page.get_access_mode_JDBC().click()
        log.info("Selecting the loan provider, index value 3")
        self.select_value_from_dropdown_index(admin_page.get_loan_provider(), 0)
        log.info("Selecting the loan processor, index value 3")
        self.select_value_from_dropdown_index(admin_page.get_loan_processor(), 0)
        admin_page.get_loan_threshold().clear()
        admin_page.get_loan_threshold().send_keys("30")
        time.sleep(5)

