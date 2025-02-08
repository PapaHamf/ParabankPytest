from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class UpdateProfilePage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    first_name: tuple = (By.ID, "customer.firstName")
    last_name: tuple = (By.ID, "customer.lastName")
    address_street: tuple = (By.ID, "customer.address.street")
    address_city: tuple = (By.ID, "customer.address.city")
    address_state: tuple = (By.ID, "customer.address.state")
    address_post_code: tuple = (By.ID, "customer.address.zipCode")
    phone_number: tuple = (By.ID, "customer.phoneNumber")
    update_button: tuple = (By.CSS_SELECTOR, "input[value='Update Profile']")

    # Declaring the errors labels
    first_name_error: tuple = (By.ID, "firstName-error")
    last_name_error: tuple = (By.ID, "lastName-error")
    address_street_error: tuple = (By.ID, "street-error")
    address_city_error: tuple = (By.ID, "city-error")
    address_state_error: tuple = (By.ID, "state-error")
    address_post_code_error: tuple = (By.ID, "zipCode-error")
    # Does not exist
    phone_number_error: tuple = (By.ID, "phoneNumber-error")

    # Successful update
    # Returns the div block, that should contain "Profile Updated" in h1 tag
    successful_update_msg: tuple = (By.ID, "updateProfileResult")

    def __init__(self, driver):
        self._driver = driver
        
    def get_first_name(self) -> WebElement:
        """
        Returns the first name field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.first_name)

    def get_last_name(self) -> WebElement:
        """
        Returns the last name field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.last_name)

    def get_address_street(self) -> WebElement:
        """
        Returns the address street name & number field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_street)

    def get_address_city(self) -> WebElement:
        """
        Returns the address city field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_city)

    def get_address_state(self) -> WebElement:
        """
        Returns the address state field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_state)

    def get_address_post_code(self) -> WebElement:
        """
        Returns the address post code field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_post_code)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.phone_number)
    
    def get_update_button(self) -> WebElement:
        """
       Returns the update profile button.
       :return: webelement
       """
        return self._driver.find_element(*UpdateProfilePage.update_button)
    
    def get_first_name_error(self) -> WebElement:
        """
        Returns the first name field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.first_name_error)

    def get_last_name_error(self) -> WebElement:
        """
        Returns the last name field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.last_name_error)

    def get_address_street_error(self) -> WebElement:
        """
        Returns the address street name & number field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_street_error)

    def get_address_city_error(self) -> WebElement:
        """
        Returns the address city field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_city_error)

    def get_address_state_error(self) -> WebElement:
        """
        Returns the address state field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_state_error)

    def get_address_post_code_error(self) -> WebElement:
        """
        Returns the address post code field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.address_post_code_error)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone_number field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.phone_number_error)

    def get_successful_update(self) -> WebElement:
        """
        Returns the successful update profile text (div block w/ h1 title).
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.successful_update_msg)