import time

import pytest
import random
import allure

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage

class TestLogin(BaseClass):

    # Declaring the SQL injection strings
    SQL_INJECT_ALL = "' OR 1=1#"
    SQL_INJECT_CUSTOMER = "' UNION SELECT username, password FROM customer#"

    @allure.title("Logging in/out the user")
    @pytest.fixture(scope = "function")
    def login_logout(self) -> list:
        """
        Logins the user in the app and logs him out after the test.
        :return: List containing the dict w/ the home page object and user data.
        """
        with allure.step("Step 1: Logging in"):
            self._log = self.get_logger()
            self.driver.get(BasePage.HOMEPAGE)
            # Get the user data from Excel file
            user_data = random.choice(ExcelData.get_excel_data("test_usernames.xlsx"))
            user_name = user_data["username"]
            password = user_data["password"]
            self._log.info("Logging the user.")
            # Create the home page object
            home_page = HomePage(self.driver)
            self._log.info(f"User name: {user_name}")
            home_page.get_username().send_keys(user_name)
            self._log.info(f"Password: {password}")
            home_page.get_password().send_keys(password)
            self._log.info("Clicking the login button.")
            side_menu = home_page.get_login_button()
        yield [side_menu, user_data]
        # Log out the user
        with allure.step("Step 2: Logging out"):
            self._log.info(f"Logging out the user {user_name}.")
            side_menu.get_log_out_link().click()
            self.driver.delete_all_cookies()

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Negative logging in")
    @allure.tag("Negative", "Smoke", "Logging in", "Empty fields")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 48")
    @allure.description("This test attempts to log in the customer with empty Username and Password field.")
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_logging_negative_no_username(self):
        """
        Tests the customer logging in w/ empty username and password field.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        log.info(f"Testing the customer log in with empty Username and Password field.")
        log.info("Logging in the user.")
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the logging in"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.MISSING_USER_PASSWORD_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Negative logging in")
    @allure.tag("Negative", "Smoke", "Logging in", "Empty field")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 49")
    @allure.description("This test attempts to log in the customer with empty Username field.")
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_logging_negative_no_username(self):
        """
        Tests the customer logging in w/ empty username field.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Customer log in", "Empty username")
        log.info(f"Testing the customer log in with empty Username field.")
        customer_data = random.choice(ExcelData.get_excel_data("dataset_customer.xlsx"))
        log.info("Logging in the user.")
        user_name = ""
        data_collection.add_data("username", user_name)
        password = customer_data["password"]
        log.info(f"Entering the password {password}")
        data_collection.add_data("password", password)
        home_page.get_password().send_keys(password)
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the logging in"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.MISSING_USER_PASSWORD_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Negative logging in")
    @allure.tag("Negative", "Smoke", "Logging in", "Empty field")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 50")
    @allure.description("This test attempts to log in the customer with empty Password field.")
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_logging_negative_no_password(self):
        """
        Tests the customer logging in w/ empty password field.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Customer log in", "Empty password")
        log.info(f"Testing the customer log in with empty Password field.")
        customer_data = random.choice(ExcelData.get_excel_data("dataset_customer.xlsx"))
        log.info("Logging in the user.")
        user_name = customer_data["username"]
        log.info(f"Entering the username {user_name}.")
        data_collection.add_data("username", user_name)
        home_page.get_username().send_keys(user_name)
        password = ""
        data_collection.add_data("password", password)
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the logging in"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.MISSING_USER_PASSWORD_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Negative logging in")
    @allure.tag("Negative", "Smoke", "Logging in", "Wrong username")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 51")
    @allure.description("This test attempts to log in the customer with wrong username.")
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_logging_negative_wrong_username(self):
        """
        Tests the customer logging in w/ wrong username.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Customer log in", "Wrong username")
        log.info(f"Testing the customer log in with wrong username.")
        customer_data = random.choice(ExcelData.get_excel_data("dataset_customer.xlsx"))
        log.info("Logging in the user.")
        user_name = customer_data["username"] + str(int(random.randint(0, 1000)))
        log.info(f"Entering the username {user_name}.")
        data_collection.add_data("username", user_name)
        home_page.get_username().send_keys(user_name)
        password = customer_data["password"]
        log.info(f"Entering the password {password}")
        data_collection.add_data("password", password)
        home_page.get_password().send_keys(password)
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the logging in"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.NOT_VERIFIED_USER_PASSWORD_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Negative logging in")
    @allure.tag("Negative", "Smoke", "Logging in", "Wrong password")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 52")
    @allure.description("This test attempts to log in the customer with wrong password.")
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_logging_negative_wrong_password(self):
        """
        Tests the customer logging in w/ wrong password.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Customer log in", "Wrong password")
        log.info(f"Testing the customer log in with wrong password.")
        customer_data = random.choice(ExcelData.get_excel_data("dataset_customer.xlsx"))
        log.info("Logging in the user.")
        user_name = customer_data["username"]
        log.info(f"Entering the username {user_name}.")
        data_collection.add_data("username", user_name)
        home_page.get_username().send_keys(user_name)
        password = customer_data["password"] + str(int(random.randint(0, 1000)))
        log.info(f"Entering the password {password}")
        data_collection.add_data("password", password)
        home_page.get_password().send_keys(password)
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the logging in"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.NOT_VERIFIED_USER_PASSWORD_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Positive logging in")
    @allure.tag("Positive", "Smoke", "Logging in", "Correct credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 53")
    @allure.description("This test attempts to log in the customer with correct username and password.")
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_logging_positive_correct_credentials(self, get_excel_data_customer_logins):
        """
        Tests the customer logging in w/ correct username and password.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Customer log in", "Correct credentials")
        log.info(f"Testing the customer log in with correct username and password.")
        log.info("Logging in the user.")
        user_name = get_excel_data_customer_logins["username"]
        log.info(f"Entering the username {user_name}.")
        data_collection.add_data("username", user_name)
        home_page.get_username().send_keys(user_name)
        password = get_excel_data_customer_logins["password"]
        log.info(f"Entering the password {password}")
        data_collection.add_data("password", password)
        home_page.get_password().send_keys(password)
        log.info("Clicking the log in button.")
        side_menu = home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_POSITIVE
        with (allure.step("Step 2: Verify if the user is logged in")):
            log.info("Verifying if the user is logged in.")
            logged_msg = side_menu.get_successful_login().text
            log.info(f"Logging out the user {get_excel_data_customer_logins["username"]}.")
            side_menu.get_log_out_link().click()
            self.driver.delete_all_cookies()
            assert logged_msg == side_menu.SUCCESSFULL_LOGIN_MSG + get_excel_data_customer_logins["firstname"] \
                                                    + " " + get_excel_data_customer_logins["lastname"]

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Security tests")
    @allure.tag("Security", "Smoke", "Logging in", "SQL Injection")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 54")
    @allure.description("This test attempts to do the SQL injection attack displaying the whole table.")
    @pytest.mark.smoke
    def test_logging_security_sql_inject_all(self):
        """
        Tests the customer logging in w/ SQL inject attack string.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        log.info(f"Testing the customer log in with SQL injection strings.")
        log.info("Logging in the user.")
        log.info(f"Entering the username {TestLogin.SQL_INJECT_ALL}.")
        home_page.get_username().send_keys(TestLogin.SQL_INJECT_ALL)
        password = "SQL inject"
        log.info(f"Entering the password {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the table data is not displayed"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.NOT_VERIFIED_USER_PASSWORD_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Customer logging in")
    @allure.sub_suite("Security tests")
    @allure.tag("Security", "Smoke", "Logging in", "SQL Injection")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 55")
    @allure.description("This test attempts to do the SQL injection attack displaying the usernames & passwords.")
    @pytest.mark.smoke
    def test_logging_security_sql_inject_up(self):
        """
        Tests the customer logging in w/ SQL inject attack string.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        log.info(f"Testing the customer log in with SQL injection strings.")
        log.info("Logging in the user.")
        log.info(f"Entering the username {TestLogin.SQL_INJECT_CUSTOMER}.")
        home_page.get_username().send_keys(TestLogin.SQL_INJECT_CUSTOMER)
        password = "SQL inject"
        log.info(f"Entering the password {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the log in button.")
        home_page.get_login_button()
        with allure.step("Step 1: Verify the page title"):
            log.info("Verifying the proper page title.")
            assert home_page.get_page_title() == home_page.VALID_PAGE_TITLE_NEGATIVE
        with allure.step("Step 2: Verify the table data is not displayed"):
            log.info("Verifying the error header.")
            assert home_page.get_login_error().text == home_page.ERROR_HEADER
            log.info("Verifying the error message.")
            assert home_page.get_error_msg().text == home_page.NOT_VERIFIED_USER_PASSWORD_MSG
