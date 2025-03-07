import pytest
import random
import allure

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage

class TestHomePage(BaseClass):

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for home page elements")
    @allure.sub_suite("Home page header tests")
    @allure.tag("Home page", "Header", "Logo", "Visible")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 56")
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
        with allure.step("Step 1: Verify if the logo is visible"):
            log.info("Verifying if the logo is visible on the page.")
            assert home_page.verify_logo_visibility()

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for home page elements")
    @allure.sub_suite("Home page header tests")
    @allure.tag("Home page", "Header", "Logo", "Clickable")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 57")
    @allure.description("This test verifies if the header logo is clickable.")
    @pytest.mark.clickable
    @pytest.mark.skip
    def test_header_logo_clickable(self):
        """
        Tests if the home page header logo is clickable.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        with allure.step("Step 1: Verify if the logo is clickable"):
            log.info("Verifying if the logo is clickable on the page.")
            assert home_page.verify_logo_clickable()

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for home page elements")
    @allure.sub_suite("Home page header tests")
    @allure.tag("Home page", "Header", "Icons", "Working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 58")
    @allure.description("This test verifies if the icons on the home page are clickable and working.")
    @pytest.mark.clickable
    @pytest.mark.skip
    def test_header_icons_working(self):
        """
        Tests if the home page header icons are clickable and working.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        with allure.step("Step 1: Verify if the Home icon is clickable"):
            log.info("Verifying if the Home icon is clickable.")
            assert home_page.get_home_page_icon()
        with allure.step("Step 2: Verify if the About us icon is working"):
            log.info("Verifying if the About us icon is working.")
            home_page.get_about_us_icon()
            assert home_page.get_page_title() == home_page.ABOUT_US_TITLE
            self.driver.back()
        with allure.step("Step 3: Verify if the Contact us icon is working"):
            log.info("Verifying if the Contact us icon is working.")
            home_page.get_contact_icon()
            assert home_page.get_page_title() == home_page.CONTACT_US_TITLE
            self.driver.back()

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for home page elements")
    @allure.sub_suite("Home page header tests")
    @allure.tag("Home page", "Header", "Icons", "Hover over")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 59")
    @allure.description("This test verifies if the Home icon image changes properly on the hover over.")
    @pytest.mark.displayed
    def test_header_icons_hover_over(self):
        """
        Tests if the home page header Home icon changes properly on the hover over.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        with allure.step("Step 1: Verify if the Home icon image changes"):
            log.info("Verifying if the Home icon image changes properly on the hover over.")
            assert home_page.hover_over_home_page_icon() == "test"

