import pytest
import allure
import random

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from utils.hysqlconnector import HyperSQLConnector
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
    @allure.suite("Tests for opening account")
    @allure.sub_suite("Positive account tests")
    @allure.tag("Opening account", "New account", "Positive")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 76")
    @allure.description("This test attempts to open a new checking account for the customer.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_open_account_positive(self, login_logout):
        """
        Tests the account opening for the customer.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Open New Account link.")
        open_account = login_logout[0].get_open_account_page()
        with allure.step("Step 1: Open the account"):
            log.info("Selecting the CHECKING item from the account type list.")
            open_account.select_value_from_dropdown_text(open_account.get_account_type(), "CHECKING")
            log.info("Selecting the existing account to transfer funds (deposit) into new account.")
            # Every customer from the dataset has 4 accounts
            random_index = random.randint(0, 3)
            open_account.select_value_from_dropdown_index(open_account.get_source_accounts(), random_index)
            log.info("Clicking the Open new account button.")
            open_account.get_open_account_button().click()
        with allure.step("Step 2: Verify the account opened message"):
            log.info("Verifying if the account was opened correctly.")
            assert open_account.get_success_title().text == open_account.OPEN_SUCCESS_MSG
        with allure.step("Step 3: Verify the new account link"):
            log.info("Verifying the new account link works correctly.")
            activity_page = open_account.get_new_account_id()
            assert activity_page.get_page_title() == activity_page.VALID_PAGE_TITLE_POSITIVE

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for opening account")
    @allure.sub_suite("Negative account tests")
    @allure.tag("Opening account", "New account", "Negative")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 77")
    @allure.description("This test attempts to open a new checking account for the customer using the "
                        "source account without sufficient funds for deposit.")
    @pytest.mark.smoke
    def test_open_account_insufficient_funds(self):
        """
        Tests the account opening for the customer w/ insufficient funds.
        :return:
        """
        log = self.get_logger()
        # Log in the user manually to select specific user (id 100)
        self.driver.get(BasePage.HOME_PAGE)
        with allure.step("Step 1: Log in the user"):
        # Get the user data from Excel file
            user_data = ExcelData.get_excel_data("dataset_customer.xlsx")[0]
            user_name = user_data["username"]
            password = user_data["password"]
            log.info("Logging the user.")
            home_page = HomePage(self.driver)
            log.info(f"User name: {user_name}")
            home_page.get_username().send_keys(user_name)
            log.info(f"Password: {password}")
            home_page.get_password().send_keys(password)
            log.info("Clicking the login button.")
            side_menu = home_page.get_login_button()
        with allure.step("Step 2: Open the account"):
            log.info("Clicking the Open New Account link.")
            open_account = side_menu.get_open_account_page()
            log.info("Selecting the CHECKING item from the account type list.")
            open_account.select_value_from_dropdown_text(open_account.get_account_type(), "CHECKING")
            log.info("Selecting the existing account to transfer funds (deposit) into new account.")
            open_account.select_value_from_dropdown_text(open_account.get_source_accounts(), "1002")
            log.info("Clicking the Open new account button.")
            open_account.get_open_account_button().click()
        with allure.step("Step 3: Verify the error message"):
            error_title = open_account.get_error_title().text
            log.info(f"Logging out the user {user_name}.")
            side_menu.get_log_out_link().click()
            self.driver.delete_all_cookies()
            assert error_title == open_account.OPEN_ERROR_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for opening account")
    @allure.sub_suite("Positive account tests")
    @allure.tag("Opening account", "New account", "Positive")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 78")
    @allure.description("This test verifies if the source account is correctly charged w/ the deposit.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_open_account_deposit(self, login_logout):
        """
        Tests if the source account is charged correctly.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Open New Account link.")
        open_account = login_logout[0].get_open_account_page()
        with allure.step("Step 1: Open the account"):
            log.info("Selecting the CHECKING item from the account type list.")
            open_account.select_value_from_dropdown_text(open_account.get_account_type(), "CHECKING")
            log.info("Selecting the existing account to transfer funds (deposit) into new account.")
            account_number = random.choice(open_account.get_source_accounts_text())
            open_account.select_value_from_dropdown_text(open_account.get_source_accounts(), account_number)
            log.info("Clicking the Open new account button.")
            open_account.get_open_account_button().click()
        with allure.step("Step 2: Verify if the deposit was charged"):
            log.info("Clicking the Accounts Overview link.")
            accounts_overview = login_logout[0].get_accounts_overview_page()
            log.info("Clicking the source account link.")
            activity_page = accounts_overview.select_account_number(account_number)
            log.info("Selecting the Debit from the Type list.")
            activity_page.select_value_from_dropdown_text(activity_page.get_activity_type(), "Debit")
            log.info("Clicking the Go button.")
            activity_page.get_activity_button().click()
            transaction = activity_page.get_transaction_by_index(-1)
            log.info(f"Verifying if the transaction name is {activity_page.FUNDS_SENT}")
            assert transaction[1] == activity_page.FUNDS_SENT
            log.info("Verifying if the transaction amount is 5000.")
            # Default deposit for the app is set to 5000
            assert transaction[2] == 5000

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for opening account")
    @allure.sub_suite("Positive account tests")
    @allure.tag("Opening account", "New account", "Positive", "Database")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 79")
    @allure.description("This test verifies if the account type is written properly to the database.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    def test_open_account_type_in_database(self, login_logout):
        """
        Tests if the account type is written properly to the database.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Open New Account link.")
        open_account = login_logout[0].get_open_account_page()
        with allure.step("Step 1: Open the account"):
            log.info("Selecting the SAVINGS item from the account type list.")
            open_account.select_value_from_dropdown_text(open_account.get_account_type(), "SAVINGS")
            log.info("Selecting the existing account to transfer funds (deposit) into new account.")
            # Every customer from the dataset has 4 accounts
            random_index = random.randint(0, 3)
            open_account.select_value_from_dropdown_index(open_account.get_source_accounts(), random_index)
            log.info("Clicking the Open new account button.")
            open_account.get_open_account_button().click()
        with allure.step("Step 2: Verify the account opened message"):
            log.info("Verifying if the account was opened correctly.")
            assert open_account.get_success_title().text == open_account.OPEN_SUCCESS_MSG
        with allure.step("Step 3: Verify if the account type is correct in DB"):
            log.info("Verifying if the account type was properly written to the database.")
            # Get the new account id
            new_account = open_account.get_new_account_id_text()
            log.info("Fetching the data from the database.")
            db_handle = HyperSQLConnector()
            db_handle.get_cursor()
            db_data = db_handle.get_data_from_db(f"SELECT type FROM account "
                                                 f"WHERE id = '{new_account}'")
            if len(db_data) > 0:
                db_type = db_data[0][0]
            log.info("Verifying if the account type is correct.")
            # SAVINGS account type should be 1
            assert db_type == 1


