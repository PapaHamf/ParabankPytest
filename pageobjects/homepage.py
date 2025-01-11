from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class HomePage():
    driver: Chrome

    # Declaring the page objects
    username: tuple = (By.NAME, "username")
    password: tuple = (By.NAME, "password")
    login_button: tuple = (By.CSS_SELECTOR, "input[value='Log In']")
    forgot_login: tuple = (By.PARTIAL_LINK_TEXT, "Forgot login")
    register_link: tuple = (By.LINK_TEXT, "Register")

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


