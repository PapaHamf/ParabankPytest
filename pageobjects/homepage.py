from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class HomePage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    username: tuple = (By.NAME, "username")
    password: tuple = (By.NAME, "password")
    login_button: tuple = (By.CSS_SELECTOR, "input[value='Log In']")
    forgot_login: tuple = (By.PARTIAL_LINK_TEXT, "Forgot login")
    register_link: tuple = (By.LINK_TEXT, "Register")

    # Declaring error labels
    login_error: tuple = (By.TAG_NAME, "h1")
    # Possible values:
    # 1. Please enter a username and password.
    # 2. The username and password could not be verified.
    error_msg: tuple = (By.CLASS_NAME, "error")

    def __init__(self, driver):
        self._driver = driver

    def get_username(self):
        """
        Returns the username field.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.username)

    def get_password(self):
        """
        Returns the password field.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.password)

    def get_login_button(self):
        """
        Returns the login button.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.login_button)

    def get_forgot_login(self):
        """
        Returns the forgot login name link.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.forgot_login)

    def get_register_link(self):
        """
        Returns the register link.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.register_link)

    def get_login_error(self):
        """
        Returns the login error title.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.login_error)

    def get_error_msg(self):
        """
        Returns the error message text.
        :return: webelement
        """
        return self._driver.find_element(*HomePage.error_msg)


