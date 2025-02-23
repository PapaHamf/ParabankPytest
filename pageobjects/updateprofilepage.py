from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class UpdateProfilePage(BasePage):
    """
    Class that holds the locators of the Update profile page and methods to get its webelements.
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
    UPDATE_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Update Profile']")

    # Declaring the errors labels
    FIRST_NAME_ERROR: tuple = (By.ID, "firstName-error")
    LAST_NAME_ERROR: tuple = (By.ID, "lastName-error")
    ADDRESS_STREET_ERROR: tuple = (By.ID, "street-error")
    ADDRESS_CITY_ERROR: tuple = (By.ID, "city-error")
    ADDRESS_STATE_ERROR: tuple = (By.ID, "state-error")
    ADDRESS_POST_CODE_ERROR: tuple = (By.ID, "zipCode-error")
    # Does not exist
    PHONE_NUMBER_ERROR: tuple = (By.ID, "phoneNumber-error")

    # Successful update
    # Returns the div block, that should contain "Profile Updated" in h1 tag
    SUCCESSFUL_UPDATE_MSG: tuple = (By.ID, "updateProfileResult")

    def __init__(self, driver):
        self._driver = driver
        
    def get_first_name(self) -> WebElement:
        """
        Returns the first name field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.FIRST_NAME)

    def get_last_name(self) -> WebElement:
        """
        Returns the last name field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.LAST_NAME)

    def get_address_street(self) -> WebElement:
        """
        Returns the address street name & number field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_STREET)

    def get_address_city(self) -> WebElement:
        """
        Returns the address city field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_CITY)

    def get_address_state(self) -> WebElement:
        """
        Returns the address state field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_STATE)

    def get_address_post_code(self) -> WebElement:
        """
        Returns the address post code field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_POST_CODE)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.PHONE_NUMBER)
    
    def get_update_button(self) -> WebElement:
        """
       Returns the update profile button.
       :return: webelement
       """
        return self._driver.find_element(*UpdateProfilePage.UPDATE_BUTTON)
    
    def get_first_name_error(self) -> WebElement:
        """
        Returns the first name field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.FIRST_NAME_ERROR)

    def get_last_name_error(self) -> WebElement:
        """
        Returns the last name field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.LAST_NAME_ERROR)

    def get_address_street_error(self) -> WebElement:
        """
        Returns the address street name & number field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_STREET_ERROR)

    def get_address_city_error(self) -> WebElement:
        """
        Returns the address city field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_CITY_ERROR)

    def get_address_state_error(self) -> WebElement:
        """
        Returns the address state field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_STATE_ERROR)

    def get_address_post_code_error(self) -> WebElement:
        """
        Returns the address post code field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.ADDRESS_POST_CODE_ERROR)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone_number field error text.
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.PHONE_NUMBER_ERROR)

    def get_successful_update(self) -> WebElement:
        """
        Returns the successful update profile text (div block w/ h1 title).
        :return: webelement
        """
        return self._driver.find_element(*UpdateProfilePage.SUCCESSFUL_UPDATE_MSG)