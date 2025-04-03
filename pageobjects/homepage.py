from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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
    FOOTER: tuple = (By.ID, "footerPanel")

    # Declaring the images locators
    LOGO: tuple = (By.CLASS_NAME, "logo")
    HEADER_IMAGE: tuple = (By.ID, "headerPanel")
    ICON_A: tuple = (By.TAG_NAME, "a")
    HOME_PAGE_ICON: tuple = (By.CLASS_NAME, "home")
    ABOUT_US_ICON: tuple = (By.CLASS_NAME, "aboutus")
    CONTACT_ICON: tuple = (By.CLASS_NAME, "contact")

    # Declaring error labels
    LOGIN_ERROR: tuple = (By.TAG_NAME, "h1")
    ERROR_MSG: tuple = (By.CLASS_NAME, "error")

    # Declaring the success and error texts
    VALID_PAGE_TITLE_NEGATIVE = "ParaBank | Error"
    VALID_PAGE_TITLE_POSITIVE = "ParaBank | Accounts Overview"
    HOME_PAGE_TITLE = "ParaBank | Welcome | Online Banking"
    ABOUT_US_TITLE = "ParaBank | About Us"
    CONTACT_US_TITLE = "ParaBank | Customer Care"
    ERROR_HEADER = "Error!"
    MISSING_USER_PASSWORD_MSG = "Please enter a username and password."
    NOT_VERIFIED_USER_PASSWORD_MSG = "The username and password could not be verified."
    HOME_HOVER = "home-hover.gif"
    ABOUT_US_HOVER = "aboutus-hover.gif"
    CONTACT_US_HOVER = "contact-hover.gif"
    HEADER_IMAGE_FILE = "header-main.jpg"

    # JavaScript codes
    JS_IMAGE_LOAD_END = 'var resourceList = window.performance.getEntriesByType("resource");' \
                        'for (i = 0; i < resourceList.length; i++) { if (resourceList[i].name.includes("' \
                        + HEADER_IMAGE_FILE + '")) { return resourceList[i].responseEnd; } }'
    JS_SITE_DOM_LOAD_END = 'return window.performance.getEntriesByType("navigation")[0].domContentLoadedEventEnd;'
    # Returns the complete Navigation Timing interface; not used for now
    JS_NAVIGATION_ALL = 'return window.performance.getEntriesByType("navigation")[0];'

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
        Returns the side menu page object.
        :return: page object
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

    def get_footer(self) -> WebElement:
        """
        Returns the footer div element.
        :return:
        """
        return self.verify_element_presence(HomePage.FOOTER)

    def click_footer_links(self, link_name: str) -> None:
        """
        Clicks the link in the footer of the page identified by the link text.
        :param link_name: Link text
        :return:
        """
        self.get_footer().find_element(By.LINK_TEXT, link_name).click()

    def get_logo(self) -> WebElement:
        """
        Returns the header logo image.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.LOGO)

    def verify_logo_visibility(self) -> WebElement:
        """
        Verifies if the header logo image is visible on the page.
        :return:
        """
        return self.verify_element_visibility(self.get_logo())

    def verify_logo_clickable(self) -> WebElement:
        """
        Verifies if the header logo image is clickable.
        :return:
        """
        return self.verify_element_clickable(HomePage.LOGO)

    def get_header_image(self) -> WebElement:
        """
        Returns the header image.
        :return: webelement
        """
        return self.verify_element_presence(HomePage.HEADER_IMAGE)

    def get_header_image_load_timings(self) -> tuple:
        """
        Returns the header image response end time and the DOM load event end time.
        :return: Tuple containing the time values.
        """
        self._image_load_end = self._driver.execute_script(HomePage.JS_IMAGE_LOAD_END)
        self._site_dom_load_end = self._driver.execute_script(HomePage.JS_SITE_DOM_LOAD_END)
        return self._image_load_end, self._site_dom_load_end

    def get_home_page_icon(self) -> WebElement:
        """
        Returns the home page icon.
        :return: webelement
        """
        return self.verify_element_clickable(HomePage.HOME_PAGE_ICON)

    def hover_over_home_page_icon(self) -> str:
        """
        Returns the value of CSS property "background" of the home page icon.
        :return:
        """
        self._action = ActionChains(self._driver)
        self._action.move_to_element(self.get_home_page_icon()).perform()
        return self.get_home_page_icon().find_element(*HomePage.ICON_A).value_of_css_property("background-image")

    def get_about_us_icon(self) -> AboutUs:
        """
        Returns the about us page object.
        :return: webelement
        """
        self.verify_element_clickable(HomePage.ABOUT_US_ICON).click()
        return AboutUs(self._driver)

    def hover_over_about_us_icon(self) -> str:
        """
        Returns the value of CSS property "background" of the about us icon.
        :return:
        """
        self._action = ActionChains(self._driver)
        self._action.move_to_element(self.verify_element_presence(HomePage.ABOUT_US_ICON)).perform()
        return self.verify_element_presence(HomePage.ABOUT_US_ICON). \
                find_element(*HomePage.ICON_A).value_of_css_property("background-image")

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

