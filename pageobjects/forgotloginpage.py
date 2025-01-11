from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class ForgotLoginPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    first_name: tuple = (By.ID, "firstName")
    last_name: tuple = (By.ID, "lastName")
    address_street: tuple = (By.ID, "address.street")
    address_city: tuple = (By.ID, "address.city")
    address_state: tuple = (By.ID, "address.state")
    address_post_code: tuple = (By.ID, "address.zipCode")
    social_security_number: tuple = (By.ID, "ssn")
    find_login_button: tuple = (By.CSS_SELECTOR, "input[value='Find My Login Info']")

    # Declaring the errors
    first_name_error: tuple = (By.ID, "firstName.errors")
    last_name_error: tuple = (By.ID, "lastName.errors")
    address_street_error: tuple = (By.ID, "address.street.errors")
    address_city_error: tuple = (By.ID, "address.city.errors")
    address_state_error: tuple = (By.ID, "address.state.errors")
    address_post_code_error: tuple = (By.ID, "address.zipCode.errors")
    phone_number_error: tuple = (By.ID, "phoneNumber.errors")
    social_security_number_error: tuple = (By.ID, "ssn.errors")

    def __init__(self, driver):
        self._driver = driver

    def get_first_name(self):
        """
            Returns the first name field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.first_name)

    def get_last_name(self):
        """
            Returns the last name field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.last_name)

    def get_address_street(self):
        """
            Returns the address street name & number field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_street)

    def get_address_city(self):
        """
            Returns the address city field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_city)

    def get_address_state(self):
        """
            Returns the address state field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_state)

    def get_address_post_code(self):
        """
            Returns the address post code field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_post_code)

    def get_social_security_number(self):
        """
            Returns the social security number field.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.social_security_number)

    def get_find_login_button(self):
        """
            Returns the find login button.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.find_login_button)

    def get_first_name_error(self):
        """
            Returns the first name field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.first_name_error)

    def get_last_name_error(self):
        """
            Returns the last name field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.last_name_error)

    def get_address_street_error(self):
        """
            Returns the address street name & number field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_street_error)

    def get_address_city_error(self):
        """
            Returns the address city field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_city_error)

    def get_address_state_error(self):
        """
            Returns the address state field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_state_error)

    def get_address_post_code_error(self):
        """
            Returns the address post code field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.address_post_code_error)

    def get_social_security_number_error(self):
        """
            Returns the social security number field error text.
            :return: webelement
        """
        return self._driver.find_element(*ForgotLoginPage.social_security_number_error)



