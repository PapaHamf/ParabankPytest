from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class RegisterPage():
    """
    Class that holds the locators of the Register page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    first_name: tuple = (By.ID, "customer.firstName")
    last_name: tuple = (By.ID, "customer.lastName")
    address_street: tuple = (By.ID, "customer.address.street")
    address_city: tuple = (By.ID, "customer.address.city")
    address_state: tuple = (By.ID, "customer.address.state")
    address_post_code: tuple = (By.ID, "customer.address.zipCode")
    phone_number: tuple = (By.ID, "customer.phoneNumber")
    social_security_number: tuple = (By.ID, "customer.ssn")
    username: tuple = (By.ID, "customer.username")
    password: tuple = (By.ID, "customer.password")
    confirm_password: tuple = (By.ID, "repeatedPassword")
    register_button: tuple = (By.CSS_SELECTOR, "input[value='Register']")

    # Declaring the errors labels
    # All of the errors contain the phrase "is required."
    first_name_error: tuple = (By.ID, "customer.firstName.errors")
    last_name_error: tuple = (By.ID, "customer.lastName.errors")
    address_street_error: tuple = (By.ID, "customer.address.street.errors")
    address_city_error: tuple = (By.ID, "customer.address.city.errors")
    address_state_error: tuple = (By.ID, "customer.address.state.errors")
    address_post_code_error: tuple = (By.ID, "customer.address.zipCode.errors")
    phone_number_error: tuple = (By.ID, "customer.phoneNumber.errors")
    social_security_number_error: tuple = (By.ID, "customer.ssn.errors")
    # The possible errors:
    # 1. Username is required.
    # 2. This username already exists.
    username_error: tuple = (By.ID, "customer.username.errors")
    password_error: tuple = (By.ID, "customer.password.errors")
    confirm_password_error: tuple = (By.ID, "repeatedPassword.errors")

    # Successful registration
    # This locator should contain the text "Welcome"
    successful_registration: tuple = (By.CSS_SELECTOR, "h1.title")
    # This locator should contain the text "Your account was created successfully."
    # successful_registration: tuple = (By.CSS_SELECTOR, "div#rightPanel p")

    def __init__(self, driver):
        self._driver = driver

    def get_first_name(self) -> WebElement:
        """
        Returns the first name field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.first_name)

    def get_last_name(self) -> WebElement:
        """
        Returns the last name field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.last_name)

    def get_address_street(self) -> WebElement:
        """
        Returns the address street name & number field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_street)

    def get_address_city(self) -> WebElement:
        """
        Returns the address city field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_city)

    def get_address_state(self) -> WebElement:
        """
        Returns the address state field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_state)

    def get_address_post_code(self) -> WebElement:
        """
        Returns the address post code field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_post_code)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.phone_number)

    def get_social_security_number(self) -> WebElement:
        """
        Returns the social security number field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.social_security_number)

    def get_username(self) -> WebElement:
        """
        Returns the user name field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.username)

    def get_password(self) -> WebElement:
        """
        Returns the password field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.password)

    def get_confirm_password(self) -> WebElement:
        """
        Returns the confirm password field.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.confirm_password)

    def get_register_button(self) -> WebElement:
        """
        Returns the register button.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.register_button)

    def get_first_name_error(self) -> WebElement:
        """
        Returns the first name field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.first_name_error)

    def get_last_name_error(self) -> WebElement:
        """
        Returns the last name field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.last_name_error)

    def get_address_street_error(self) -> WebElement:
        """
        Returns the address street name & number field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_street_error)

    def get_address_city_error(self) -> WebElement:
        """
        Returns the address city field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_city_error)

    def get_address_state_error(self) -> WebElement:
        """
        Returns the address state field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_state_error)

    def get_address_post_code_error(self) -> WebElement:
        """
        Returns the address post code field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.address_post_code_error)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone_number field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.phone_number_error)

    def get_social_security_number_error(self) -> WebElement:
        """
        Returns the social security number field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.social_security_number_error)

    def get_username_error(self) -> WebElement:
        """
        Returns the user name field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.username_error)

    def get_password_error(self) -> WebElement:
        """
        Returns the password field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.password_error)

    def get_confirm_password_error(self) -> WebElement:
        """
        Returns the confirm password field error text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.confirm_password_error)

    def get_successful_registration(self) -> WebElement:
        """
        Returns the successful registration text.
        :return: webelement
        """
        return self._driver.find_element(*RegisterPage.successful_registration)

