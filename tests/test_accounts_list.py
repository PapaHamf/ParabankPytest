import pytest
import allure
import random
import re

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from utils.hysqlconnector import HyperSQLConnector
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage
from pageobjects.sidemenu import SideMenu

class TestContactUs(BaseClass):
    side_menu: SideMenu

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
    @allure.suite("Tests for customer accounts overview")
    @allure.sub_suite("Accounts list tests")
    @allure.tag("Accounts Overview", "Accounts list", "Account numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 73")
    @allure.description("This test verifies if the accounts overview list is sorted according to the"
                        " account numbers.")
    @pytest.mark.functional
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_account_overview_accounts_list(self, login_logout):
        """
        Tests if the accounts overview list is sorted properly.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Accounts Overview link.")
        account_overview = login_logout[0].get_accounts_overview_page()
        log.info("Fetching the account numbers list.")
        acc_nos = account_overview.get_account_numbers_text()
        sorted_acc_nos = sorted(acc_nos)
        log.info("Verifying if the accounts are sorted properly.")
        assert acc_nos == sorted_acc_nos

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for customer accounts overview")
    @allure.sub_suite("Accounts list tests")
    @allure.tag("Accounts Overview", "Accounts list", "Account balances")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 74")
    @allure.description("This test verifies if the account balances total is calculated properly.")
    @pytest.mark.functional
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_account_overview_balances_total(self, login_logout):
        """
        Tests if the account balances total is correct.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Accounts Overview link.")
        account_overview = login_logout[0].get_accounts_overview_page()
        log.info("Fetching the account balances numbers list.")
        acc_balances = account_overview.get_account_balances_numbers()
        my_total = sum(acc_balances)
        log.info("Fetching the total amount.")
        web_total = float(re.sub(r"[^0-9.]", "", account_overview.get_total_amount().text))
        log.info("Verifying if the account balances total is correct.")
        assert my_total == web_total

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for customer accounts overview")
    @allure.sub_suite("Accounts list tests")
    @allure.tag("Accounts Overview", "Accounts list", "Account balances", "Database")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 75")
    @allure.description("This test verifies if the account balances displayed on the page are the"
                        " same as in database.")
    @pytest.mark.functional
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_account_overview_balances_database(self, login_logout):
        """
        Tests if the accounts balances displayed are the same as in database.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Accounts Overview link.")
        account_overview = login_logout[0].get_accounts_overview_page()
        user_data = login_logout[1]
        log.info("Fetching the account balances numbers list.")
        acc_balances = account_overview.get_account_balances_numbers()
        log.info("Fetching the data from the database.")
        db_handle = HyperSQLConnector()
        db_handle.get_cursor()
        db_data = db_handle.get_data_from_db(f"SELECT balance FROM account "
                                             f"WHERE customer_id = '{user_data["id"]}'")
        if len(db_data) > 0:
            db_data = [element[0] for element in db_data]
        log.info("Verifying if the account balances total is correct.")
        assert db_data == acc_balances
