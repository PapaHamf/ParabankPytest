from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.forgotloginpage import ForgotLoginPage
from pageobjects.registerpage import RegisterPage
from pageobjects.sitemappage import SiteMap
from pageobjects.aboutuspage import AboutUs
from pageobjects.adminpage import AdminPage
from pageobjects.contactpage import ContactPage
from pageobjects.basepage import BasePage
from pageobjects.sidemenu import SideMenu

class HomePage(BasePage):
    """
    Class that holds the locators of the Home page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    USERNAME: tuple = (By.NAME, "username")
    PASSWORD: tuple = (By.NAME, "password")
    LOGIN_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Log In']")
    FORGOT_LOGIN: tuple = (By.PARTIAL_LINK_TEXT, "Forgot login")
    REGISTER_LINK: tuple = (By.LINK_TEXT, "Register")
    SITE_MAP_LINK: tuple = (By.LINK_TEXT, "Site Map")
    HOME_PAGE_LINK: tuple = (By.LINK_TEXT, "Home")
    ABOUT_US_LINK: tuple = (By.LINK_TEXT, "About Us")
    ADMIN_PAGE_LINK: tuple = (By.LINK_TEXT, "Admin Page")

    # Declaring the images locators
    LOGO: tuple = (By.CLASS_NAME, "logo")
    HEADER_IMAGE: tuple = (By.ID, "headerPanel")
    # Testing the mouse hover -  driver.find_element().value_of_css_property()
    # value property background images/home-hover.gif
    HOME_PAGE_ICON: tuple = (By.CLASS_NAME, "home")
    ABOUT_US_ICON: tuple = (By.CLASS_NAME, "aboutus")
    CONTACT_ICON: tuple = (By.CLASS_NAME, "contact")

    # Declaring error labels
    LOGIN_ERROR: tuple = (By.TAG_NAME, "h1")
    # Possible values:
    # 1. Please enter a username and password.
    # 2. The username and password could not be verified.
    ERROR_MSG: tuple = (By.CLASS_NAME, "error")

    # Declaring the success and error messages
    VALID_PAGE_TITLE_NEGATIVE = "ParaBank | Error"
    VALID_PAGE_TITLE_POSITIVE = "ParaBank | Accounts Overview"
    ERROR_HEADER = "Error!"
    MISSING_USER_PASSWORD_MSG = "Please enter a username and password."
    NOT_VERIFIED_USER_PASSWORD_MSG = "The username and password could not be verified."

    def __init__(self, driver):
        self._driver = driver

    def get_username(self) -> WebElement:
        """
        Returns the username field.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.USERNAME)

    def get_password(self) -> WebElement:
        """
        Returns the password field.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.PASSWORD)

    def get_login_button(self) -> SideMenu:
        """
        Returns the login button.
        :return: webelement
        """
        self.verify_element_clickable(HomePage.LOGIN_BUTTON).click()
        return SideMenu(self._driver)

    def get_forgot_login(self) -> ForgotLoginPage:
        """
        Returns the forgot login page object.
        :return: page object
        """
        self.verify_element_clickable(HomePage.FORGOT_LOGIN).click()
        return ForgotLoginPage(self._driver)

    def get_register_link(self) -> RegisterPage:
        """
        Returns the register page object.
        :return: page object
        """
        self.verify_element_clickable(HomePage.REGISTER_LINK).click()
        return RegisterPage(self._driver)

    def get_site_map_link(self) -> SiteMap:
        """
        Returns the site map page object.
        :return: page object
        """
        self.verify_element_clickable(HomePage.SITE_MAP_LINK).click()
        return SiteMap(self._driver)

    def get_about_us_link(self) -> AboutUs:
        """
        Returns the about us page object.
        :return: page object
        """
        self.verify_element_clickable(HomePage.ABOUT_US_LINK).click()
        return AboutUs(self._driver)

    def get_admin_page_link(self) -> AdminPage:
        """
        Returns the administration page object.
        :return: page object
        """
        self.verify_element_clickable(HomePage.ADMIN_PAGE_LINK).click()
        return AdminPage(self._driver)

    def get_logo(self) -> WebElement:
        """
        Returns the header logo image.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.LOGO)

    def get_header_image(self) -> WebElement:
        """
        Returns the header image.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.HEADER_IMAGE)

    def get_home_page_icon(self) -> WebElement:
        """
        Returns the home page icon.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.HOME_PAGE_ICON)

    def get_about_us_icon(self) -> AboutUs:
        """
        Returns the about us icon.
        :return: webelement
        """
        self.verify_element_clickable(HomePage.ABOUT_US_ICON).click()
        return AboutUs(self._driver)

    def get_contact_icon(self) -> ContactPage:
        """
        Returns the contact us page object.
        :return: page object
        """
        self.verify_element_clickable(HomePage.CONTACT_ICON).click()
        return ContactPage(self._driver)

    def get_login_error(self) -> WebElement:
        """
        Returns the login error title.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.LOGIN_ERROR)

    def get_error_msg(self) -> WebElement:
        """
        Returns the error message text.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.ERROR_MSG)

    def get_page_title(self) -> str:
        """
        Returns the page title.
        :return:
        """
        return self._driver.title

