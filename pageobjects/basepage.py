import pytest
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from pageobjects.homepage import HomePage
from pageobjects.sidemenu import SideMenu

@pytest.mark.usefixtures("setup")
class BasePage():
    """
    Base pase for all of the pages.
    """

    # Web pages constants (not used in tests, except HOMEPAGE)
    HOMEPAGE: str = "http://localhost:8000/parabank/"
    FORGOT_LOGIN: str = "http://localhost:8000/parabank/lookup.htm"
    REGISTER: str = "http://localhost:8000/parabank/register.htm"
    OPEN_ACCOUNT: str = "http://localhost:8000/parabank/openaccount.htm"
    ACCOUNT_OVERVIEW: str = "http://localhost:8000/parabank/overview.htm"
    # There is an argument ?id= that contains the account number
    ACTIVITY: str = "http://localhost:8000/parabank/activity.htm"
    # There is an argument ?id= that contains the transaction number
    TRANSACTION: str = "http://localhost:8000/parabank/transaction.htm"
    TRANSFER_FUNDS: str = "http://localhost:8000/parabank/transfer.htm"
    BILL_PAY: str = "http://localhost:8000/parabank/billpay.htm"
    FIND_TRANS: str = "http://localhost:8000/parabank/findtrans.htm"
    UPDATE_INFO: str = "http://localhost:8000/parabank/updateprofile.htm"
    REQUEST_LOAN: str = "http://localhost:8000/parabank/requestloan.htm"
    ADMIN_PAGE: str = "http://localhost:8000/parabank/admin.htm"
    CONTACT_FORM: str = "http://localhost:8000/parabank/contact.htm"

    @pytest.fixture(scope = "function")
    def login_logout(self) -> list:
        """
        Logins the user in the app and logs him out after the test.
        :return: List containing the dict w/ the user data and the logger object.
        """
        log = BaseClass.get_logger()
        self.driver.get(self.HOMEPAGE)
        # Get the user data from Excel file
        user_data = random.choice(ExcelData.get_excel_data("test_usernames.xlsx"))
        user_name = user_data["username"]
        password = user_data["password"]
        log.info("Logging the user.")
        # Create the home page object
        home_page = HomePage(self.driver)
        log.info(f"User name: {user_name}")
        home_page.get_username().send_keys(user_name)
        log.info(f"Password: {password}")
        home_page.get_password().send_keys(password)
        log.info("Clicking the login button.")
        home_page.get_login_button().click()
        yield [home_page, user_data, log]
        # Log out the user
        side_menu = SideMenu(self.driver)
        log.info(f"Logging out the user {user_name}.")
        side_menu.get_log_out_link().click()
        self.driver.delete_all_cookies()

    def verify_element_presence(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
        Verifies the webelement presence on the page.
        :param locator: The locator describing the webelement to be checked. Tuple containing the By
        strategy and locator.
        :param timeout: The timeout for the explicit waiting. The default value is 10.
        :return: webelement
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(*locator))

    def verify_element_clickable(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
        Verifies if the webelement is clickable.
        :param locator: The locator describing the webelement to be checked. Tuple containing the By
        strategy and locator.
        :param timeout: The timeout for the explicit waiting. The default value is 10.
        :return: webelement
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(*locator))

    def verify_element_visibility(self, element: WebElement, timeout: int = 10) -> WebElement:
        """
        Verifies if the webelement is visible.
        :param element: Webelement to be checked.
        :param timeout: The timeout of the explicit waiting. The default value is 10.
        :return: webelement
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of(element))

    def verify_text_present_in_element(self, locator: tuple, text: str, timeout: int = 10) -> bool:
        """
        Verifies if the text is present in the webelement.
        :param locator: The locator describing the webelement to be checked. Tuple containing the By
        strategy and locator.
        :param text: Text to be located in given webelement.
        :param timeout: The timeout of the explicit waiting. The default value is 10.
        :return:
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(locator, text))

    def verify_title_contains(self, text: str, timeout: int = 10) -> bool:
        """
        Verifies if the text is present in the page title.
        :param text: Text to be located in page title.
        :param timeout: The timeout of the explicit waiting. The default value is 10.
        :return:
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.title_contains(text))

    def verify_element_selected(self, element: WebElement, timeout: int = 10):
        """
        Verifies if the webelement is selected.
        :param element: Webelement to be checked.
        :param timeout: The timeout of the explicit waiting. The default value is 10.
        :return:
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_selected(element))

    def get_list_values(self, dropdown_list: WebElement) -> list:
        """
        Returns the list of elements from the passed static dropdown (webelement).
        :param element: Webelement that references the static dropdown.
        :return: List of elements of the dropdown.
        """
        values = []
        for element in dropdown_list.find_elements(By.TAG_NAME, "option"):
            values.append(element.text)
        return values

    def select_value_from_dropdown_text(self, element: WebElement, text: str) -> None:
        """
        Selects the value from the passed list (webelement) using the text.
        :param element: Webelement that references the static dropdown.
        :param text: The text value to be selected.
        :return: None
        """
        dropdown: Select = Select(element)
        dropdown.select_by_visible_text(text)

    def select_value_from_dropdown_index(self, element: WebElement, index: int) -> None:
        """
        Selects the value from the passed list (webelement) using the index value.
        :param element: Webelement that references the static dropdown.
        :param index: The index value to be selected.
        :return: None
        """
        dropdown: Select = Select(element)
        dropdown.select_by_index(index)