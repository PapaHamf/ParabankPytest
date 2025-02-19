from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.forgotloginpage import ForgotLoginPage
from pageobjects.registerpage import RegisterPage
from pageobjects.sitemap import SiteMap
from pageobjects.aboutus import AboutUs
from pageobjects.adminpage import AdminPage
from pageobjects.contactpage import ContactPage

class HomePage():
    """
    Class that holds the locators of the Home page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    username: tuple = (By.NAME, "username")
    password: tuple = (By.NAME, "password")
    login_button: tuple = (By.CSS_SELECTOR, "input[value='Log In']")
    forgot_login: tuple = (By.PARTIAL_LINK_TEXT, "Forgot login")
    register_link: tuple = (By.LINK_TEXT, "Register")
    site_map_link: tuple = (By.LINK_TEXT, "Site Map")
    home_page_link: tuple = (By.LINK_TEXT, "Home")
    about_us_link: tuple = (By.LINK_TEXT, "About Us")
    admin_page_link: tuple = (By.LINK_TEXT, "Admin Page")

    # Declaring the images locators
    logo: tuple = (By.CLASS_NAME, "logo")
    header_image: tuple = (By.ID, "headerPanel")
    # Testing the mouse hover -  driver.find_element().value_of_css_property()
    # value property background images/home-hover.gif
    home_page_icon: tuple = (By.CLASS_NAME, "home")
    about_us_icon: tuple = (By.CLASS_NAME, "aboutus")
    contact_icon: tuple = (By.CLASS_NAME, "contact")

    # Declaring error labels
    login_error: tuple = (By.TAG_NAME, "h1")
    # Possible values:
    # 1. Please enter a username and password.
    # 2. The username and password could not be verified.
    error_msg: tuple = (By.CLASS_NAME, "error")

    def __init__(self, driver):
        self._driver = driver

    def get_username(self) -> WebElement:
        """
        Returns the username field.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.username)

    def get_password(self) -> WebElement:
        """
        Returns the password field.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.password)

    def get_login_button(self) -> WebElement:
        """
        Returns the login button.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.login_button)

    def get_forgot_login(self) -> ForgotLoginPage:
        """
        Returns the forgot login page object.
        :return: page object
        """
        self._driver.find_element(*HomePage.forgot_login).click()
        return ForgotLoginPage(self._driver)

    def get_register_link(self) -> RegisterPage:
        """
        Returns the register page object.
        :return: page object
        """
        self._driver.find_element(*HomePage.register_link).click()
        return RegisterPage(self._driver)

    def get_site_map_link(self) -> SiteMap:
        """
        Returns the site map page object.
        :return: page object
        """
        self._driver.find_element(*HomePage.site_map_link).click()
        return SiteMap(self._driver)

    def get_about_us_link(self) -> AboutUs:
        """
        Returns the about us page object.
        :return: page object
        """
        self._driver.find_element(*HomePage.about_us_link).click()
        return AboutUs(self._driver)

    def get_admin_page_link(self) -> AdminPage:
        """
        Returns the administration page object.
        :return: page object
        """
        self._driver.find_element(*HomePage.admin_page_link).click()
        return AdminPage(self._driver)

    def get_logo(self) -> WebElement:
        """
        Returns the header logo image.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.logo)

    def get_header_image(self) -> WebElement:
        """
        Returns the header image.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.header_image)

    def get_home_page_icon(self) -> WebElement:
        """
        Returns the home page icon.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.home_page_icon)

    def get_about_us_icon(self) -> AboutUs:
        """
        Returns the about us icon.
        :return: webelement
        """
        self._driver.find_element(*HomePage.about_us_icon).click()
        return AboutUs(self._driver)

    def get_contact_icon(self) -> ContactPage:
        """
        Returns the contact us page object.
        :return: page object
        """
        self._driver.find_element(*HomePage.contact_icon).click()
        return ContactPage(self._driver)

    def get_login_error(self) -> WebElement:
        """
        Returns the login error title.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.login_error)

    def get_error_msg(self) -> WebElement:
        """
        Returns the error message text.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.error_msg)


