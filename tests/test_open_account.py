import pytest
import allure
import random

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
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
    def test_open_account_postive(self, login_logout):
        """
        Tests the account opening for the customer.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Open New Account link.")
        open_account = login_logout[0].get_open_account_page()
        log.info("Selecting the CHECKING item from the account type list.")
        open_account.select_value_from_dropdown_text(open_account.get_account_type(), "CHECKING")
        log.info("Selecting the existing account to transfer funds (deposit) into new account.")
        # Every customer from the dataset has 4 accounts
        random_index = random.randint(0, 3)
        open_account.select_value_from_dropdown_index(open_account.get_source_accounts(), random_index)
        log.info("Clicking the Open new account button.")
        open_account.get_open_account_button().click()
        with allure.step("Step 1: Verify the account opened message"):
            log.info("Verifying if the account was opened correctly.")
            assert open_account.OPEN_SUCCESS_MSG == open_account.get_success_title().text
        with allure.step("Step 2: Verify the new account link"):
            log.info("Verifying the new account link works correctly.")
            activity_page = open_account.get_new_account_id()
            assert activity_page.VALID_PAGE_TITLE_POSITIVE == activity_page.get_page_title()

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
        log.info("Clicking the Open New Account link.")
        open_account = side_menu.get_open_account_page()
        log.info("Selecting the CHECKING item from the account type list.")
        open_account.select_value_from_dropdown_text(open_account.get_account_type(), "CHECKING")
        log.info("Selecting the existing account to transfer funds (deposit) into new account.")
        open_account.select_value_from_dropdown_text(open_account.get_source_accounts(), "1002")
        log.info("Clicking the Open new account button.")
        open_account.get_open_account_button().click()
        error_title = open_account.get_error_title().text
        log.info(f"Logging out the user {user_name}.")
        side_menu.get_log_out_link().click()
        self.driver.delete_all_cookies()
        assert open_account.OPEN_ERROR_MSG == error_title

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
        with allure.step("Step 1: Open the account"):
            open_account = login_logout[0].get_open_account_page()
            log.info("Selecting the CHECKING item from the account type list.")
            open_account.select_value_from_dropdown_text(open_account.get_account_type(), "CHECKING")
            log.info("Selecting the existing account to transfer funds (deposit) into new account.")
            account_number = random.choice(open_account.get_source_accounts_text())
            open_account.select_value_from_dropdown_text(open_account.get_source_accounts(), account_number)
            log.info("Clicking the Open new account button.")
            open_account.get_open_account_button().click()
        with allure.step("Step 2: Verify if the deposit was charged"):
            accounts_overview = login_logout[0].get_accounts_overview_page()
            activity_page = accounts_overview.select_account_number(account_number)


