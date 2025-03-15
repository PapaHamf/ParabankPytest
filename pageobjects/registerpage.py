from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage
from pageobjects.sidemenu import SideMenu

class RegisterPage(BasePage):
    """
    Class that holds the locators of the Register page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    FIRST_NAME: tuple = (By.ID, "customer.firstName")
    LAST_NAME: tuple = (By.ID, "customer.lastName")
    ADDRESS_STREET: tuple = (By.ID, "customer.address.street")
    ADDRESS_CITY: tuple = (By.ID, "customer.address.city")
    ADDRESS_STATE: tuple = (By.ID, "customer.address.state")
    ADDRESS_POST_CODE: tuple = (By.ID, "customer.address.zipCode")
    PHONE_NUMBER: tuple = (By.ID, "customer.phoneNumber")
    SOCIAL_SECURITY_NUMBER: tuple = (By.ID, "customer.ssn")
    USERNAME: tuple = (By.ID, "customer.username")
    PASSWORD: tuple = (By.ID, "customer.password")
    CONFIRM_PASSWORD: tuple = (By.ID, "repeatedPassword")
    REGISTER_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Register']")

    # Declaring the errors labels
    # All of the errors contain the phrase "is required."
    ERROR_LABEL: tuple = (By.CLASS_NAME, "error")
    FIRST_NAME_ERROR: tuple = (By.ID, "customer.firstName.errors")
    LAST_NAME_ERROR: tuple = (By.ID, "customer.lastName.errors")
    ADDRESS_STREET_ERROR: tuple = (By.ID, "customer.address.street.errors")
    ADDRESS_CITY_ERROR: tuple = (By.ID, "customer.address.city.errors")
    ADDRESS_STATE_ERROR: tuple = (By.ID, "customer.address.state.errors")
    ADDRESS_POST_CODE_ERROR: tuple = (By.ID, "customer.address.zipCode.errors")
    PHONE_NUMBER_ERROR: tuple = (By.ID, "customer.phoneNumber.errors")
    SOCIAL_SECURITY_NUMBER_ERROR: tuple = (By.ID, "customer.ssn.errors")
    # The possible errors:
    # 1. Username is required.
    # 2. This username already exists.
    USERNAME_ERROR: tuple = (By.ID, "customer.username.errors")
    PASSWORD_ERROR: tuple = (By.ID, "customer.password.errors")
    CONFIRM_PASSWORD_ERROR: tuple = (By.ID, "repeatedPassword.errors")

    # Successful registration
    # This locator should contain the text "Welcome"
    SUCCESSFUL_REGISTRATION: tuple = (By.CSS_SELECTOR, "h1.title")
    # This locator should contain the text "Your account was created successfully."
    SUCCESSFUL_REGISTRATION_FULL_MSG: tuple = (By.CSS_SELECTOR, "div#rightPanel p")

    # Declaring the success & errors messages
    ERROR_REQUIRED_MSG = " is required."
    ERROR_INVALID_MSG = " is invalid."
    USERNAME_EXISTS_MSG = "This username already exists."
    PASSWORDS_DO_NOT_MATCH = "Passwords did not match."
    REGISTRATION_SUCCESS_MSG = "Welcome"
    REGISTRATION_SUCCESS_FULL_MSG = "Your account was created successfully."
    BAD_REQUEST_TITLE = "HTTP Status 400"
    VALID_PAGE_TITLE_NEGATIVE = "ParaBank | Register for Free Online Account Access"
    VALID_PAGE_TITLE_POSITIVE = "ParaBank | Customer Created"
    # Full text "An internal error has occurred and has been logged."
    GENERAL_ERROR_MSG = "internal error"

    def __init__(self, driver):
        self._driver = driver

    def get_first_name(self) -> WebElement:
        """
        Returns the first name field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.FIRST_NAME)

    def get_last_name(self) -> WebElement:
        """
        Returns the last name field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.LAST_NAME)

    def get_address_street(self) -> WebElement:
        """
        Returns the address street name & number field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_STREET)

    def get_address_city(self) -> WebElement:
        """
        Returns the address city field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_CITY)

    def get_address_state(self) -> WebElement:
        """
        Returns the address state field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_STATE)

    def get_address_post_code(self) -> WebElement:
        """
        Returns the address post code field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_POST_CODE)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.PHONE_NUMBER)

    def get_social_security_number(self) -> WebElement:
        """
        Returns the social security number field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.SOCIAL_SECURITY_NUMBER)

    def get_username(self) -> WebElement:
        """
        Returns the user name field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.USERNAME)

    def get_password(self) -> WebElement:
        """
        Returns the password field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.PASSWORD)

    def get_confirm_password(self) -> WebElement:
        """
        Returns the confirm password field.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.CONFIRM_PASSWORD)

    def get_register_button(self) -> SideMenu:
        """
        Returns the register button.
        :return: webelement
        """
        self.verify_element_presence(RegisterPage.REGISTER_BUTTON).click()
        return SideMenu(self._driver)

    def get_errors(self) -> list[str]:
        """
        Returns all of the errors from the page.
        :return:
        """
        return [element.text for element in self._driver.find_elements(*RegisterPage.ERROR_LABEL)]

    def get_first_name_error(self) -> WebElement:
        """
        Returns the first name field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.FIRST_NAME_ERROR)

    def get_last_name_error(self) -> WebElement:
        """
        Returns the last name field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.LAST_NAME_ERROR)

    def get_address_street_error(self) -> WebElement:
        """
        Returns the address street name & number field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_STREET_ERROR)

    def get_address_city_error(self) -> WebElement:
        """
        Returns the address city field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_CITY_ERROR)

    def get_address_state_error(self) -> WebElement:
        """
        Returns the address state field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_STATE_ERROR)

    def get_address_post_code_error(self) -> WebElement:
        """
        Returns the address post code field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.ADDRESS_POST_CODE_ERROR)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone_number field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.PHONE_NUMBER_ERROR)

    def get_social_security_number_error(self) -> WebElement:
        """
        Returns the social security number field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.SOCIAL_SECURITY_NUMBER_ERROR)

    def get_username_error(self) -> WebElement:
        """
        Returns the user name field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.USERNAME_ERROR)

    def get_password_error(self) -> WebElement:
        """
        Returns the password field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.PASSWORD_ERROR)

    def get_confirm_password_error(self) -> WebElement:
        """
        Returns the confirm password field error text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.CONFIRM_PASSWORD_ERROR)

    def get_successful_registration(self) -> WebElement:
        """
        Returns the successful registration text.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.SUCCESSFUL_REGISTRATION)

    def get_successful_registration_full(self) -> WebElement:
        """
        Returns the successful registration full message.
        :return: webelement
        """
        return self.verify_element_presence(RegisterPage.SUCCESSFUL_REGISTRATION_FULL_MSG)

    def get_bad_request_title(self) -> bool:
        """
        Verifies if the page title contains the "bad request" text.
        :return: bool
        """
        return self.verify_title_contains(RegisterPage.BAD_REQUEST_TITLE)
