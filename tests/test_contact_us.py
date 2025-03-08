import pytest
import allure

from utils.baseclass import BaseClass
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage

class TestContactUs(BaseClass):

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for contact us page")
    @allure.sub_suite("Home page header tests")
    @allure.tag("Home page", "Header", "Logo", "Visible")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 61")
    @allure.description("This test verifies if the header logo is displayed properly.")
    @pytest.mark.displayed
    @pytest.mark.skip
    def test_header_logo_displayed(self):
        """
        Tests if the home page header logo is visible.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)