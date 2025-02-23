from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class ForgotLoginPage(BasePage):
    """
    Class that holds the locators of the Forgot login page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    FIRST_NAME: tuple = (By.ID, "firstName")
    LAST_NAME: tuple = (By.ID, "lastName")
    ADDRESS_STREET: tuple = (By.ID, "address.street")
    ADDRESS_CITY: tuple = (By.ID, "address.city")
    ADDRESS_STATE: tuple = (By.ID, "address.state")
    ADDRESS_POST_CODE: tuple = (By.ID, "address.zipCode")
    SOCIAL_SECURITY_NUMBER: tuple = (By.ID, "ssn")
    FIND_LOGIN_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Find My Login Info']")

    # Declaring the errors
    FIRST_NAME_ERROR: tuple = (By.ID, "firstName.errors")
    LAST_NAME_ERROR: tuple = (By.ID, "lastName.errors")
    ADDRESS_STREET_ERROR: tuple = (By.ID, "address.street.errors")
    ADDRESS_CITY_ERROR: tuple = (By.ID, "address.city.errors")
    ADDRESS_STATE_ERROR: tuple = (By.ID, "address.state.errors")
    ADDRESS_POST_CODE_ERROR: tuple = (By.ID, "address.zipCode.errors")
    PHONE_NUMBER_ERROR: tuple = (By.ID, "phoneNumber.errors")
    SOCIAL_SECURITY_NUMBER_ERROR: tuple = (By.ID, "ssn.errors")
    LOOKUP_ERROR: tuple = (By.CLASS_NAME, "error")

    def __init__(self, driver):
        self._driver = driver

    def get_first_name(self) -> WebElement:
        """
        Returns the first name field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.FIRST_NAME)

    def get_last_name(self) -> WebElement:
        """
        Returns the last name field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.LAST_NAME)

    def get_address_street(self) -> WebElement:
        """
        Returns the address street name & number field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_STREET)

    def get_address_city(self) -> WebElement:
        """
        Returns the address city field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_CITY)

    def get_address_state(self) -> WebElement:
        """
        Returns the address state field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_STATE)

    def get_address_post_code(self) -> WebElement:
        """
        Returns the address post code field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_POST_CODE)

    def get_social_security_number(self) -> WebElement:
        """
        Returns the social security number field.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.SOCIAL_SECURITY_NUMBER)

    def get_find_login_button(self) -> WebElement:
        """
        Returns the find login button.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.FIND_LOGIN_BUTTON)

    def get_first_name_error(self) -> WebElement:
        """
        Returns the first name field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.FIRST_NAME_ERROR)

    def get_last_name_error(self) -> WebElement:
        """
        Returns the last name field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.LAST_NAME_ERROR)

    def get_address_street_error(self) -> WebElement:
        """
        Returns the address street name & number field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_STREET_ERROR)

    def get_address_city_error(self) -> WebElement:
        """
        Returns the address city field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_CITY_ERROR)

    def get_address_state_error(self) -> WebElement:
        """
        Returns the address state field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_STATE_ERROR)

    def get_address_post_code_error(self) -> WebElement:
        """
        Returns the address post code field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.ADDRESS_POST_CODE_ERROR)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone number field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.PHONE_NUMBER_ERROR)

    def get_social_security_number_error(self) -> WebElement:
        """
        Returns the social security number field error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.SOCIAL_SECURITY_NUMBER_ERROR)

    def get_lookup_error(self) -> WebElement:
        """
        Returns the lookup error text.
        :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.LOOKUP_ERROR)



