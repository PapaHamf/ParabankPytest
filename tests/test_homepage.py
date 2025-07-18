import pytest
import allure

from utils.baseclass import BaseClass
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
    @pytest.mark.functional
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
    @pytest.mark.functional
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
    @pytest.mark.functional
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
    @allure.description("This test verifies if the Home icon image changes properly on the mouse over.")
    @pytest.mark.functional
    def test_header_icons_hover_over(self):
        """
        Tests if the home page header Home icon changes properly on the mouse over.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        with allure.step("Step 1: Verify if the Home icon image changes"):
            log.info("Verifying if the Home icon image changes properly on the mouse over.")
            hover_over = home_page.hover_over_home_page_icon().lstrip('url("').rstrip('")').split("/")
            assert  hover_over[-1] == HomePage.HOME_HOVER

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for home page elements")
    @allure.sub_suite("Home page header tests")
    @allure.tag("Home page", "Header", "Image", "Loading time")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 60")
    @allure.description("This test verifies if the header image loads with other content or at the end.")
    @pytest.mark.functional
    def test_header_image_loading_time(self):
        """
        Tests if the home page header image loads with other content or at the end.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        with allure.step("Step 1: Fetch the loading times"):
            log.info("Fetching the loading times using the Performance Timing JS interface.")
            load_data = home_page.get_header_image_load_timings()
        with allure.step("Step 2: Verify if the header image loads w/ other content"):
            log.info("Verifying if the header image load time is similar to the DOM load end time.")
            # Increase the DOM load end time by 10%; if the diff is not higher than this,
            # we can consider this as loading at the same time
            assert load_data[0] < load_data[1] * 1.1

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for home page elements")
    @allure.sub_suite("Home page footer links tests")
    @allure.tag("Home page", "Footer" "Pages links")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @pytest.mark.functional
    def test_footer_links(self, get_csv_data_footer_links):
        """
        Tests if the home page footer links direct to the correct page.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        allure.dynamic.testcase(f"Test Case no {get_csv_data_footer_links["tc"]}")
        allure.dynamic.description(f"This test attempts to click the footer link {get_csv_data_footer_links["link"]}.")
        with allure.step("Step 1: Click the footer link"):
            log.info(f"Clicking the footer link {get_csv_data_footer_links["link"]}.")
            home_page.click_footer_links(get_csv_data_footer_links["link"])
        with allure.step("Step 2: Verify the page title"):
            log.info(f"Checking if the page title is {get_csv_data_footer_links["pagetitle"]}.")
            assert home_page.get_page_title() == get_csv_data_footer_links["pagetitle"]

