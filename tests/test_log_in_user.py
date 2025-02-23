import time
import pytest
import random
import allure

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from pageobjects.homepage import HomePage
from pageobjects.sidemenu import SideMenu
from pageobjects.basepage import BasePage

class TestLogin(BaseClass):

    @pytest.fixture(scope = "function")
    def login_logout(self) -> list:
        """
        Logins the user in the app and logs him out after the test.
        :return: List containing the dict w/ the home page object and user data.
        """
        self._log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
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
        home_page.get_login_button().click()
        yield [home_page, user_data]
        # Log out the user
        side_menu = SideMenu(self.driver)
        self._log.info(f"Logging out the user {user_name}.")
        side_menu.get_log_out_link().click()
        self.driver.delete_all_cookies()

    @pytest.mark.smoke
    def test_aboutus(self):
        """
        Tests the about us page.
        :return:
        """
        self.driver.get(HomePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        about_us_page = home_page.get_about_us_link()
        print(about_us_page.get_page_header().text)
        if about_us_page.get_about_us_message("Demo Website"):
            print("Yes")
        print(about_us_page.check_page_header_visibility().text)