import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    """
    Base pase for all the pages.
    """

    # Web pages constants (not used in tests, except HOMEPAGE)
    HOME_PAGE: str = "http://localhost:8000/parabank/"
    FORGOT_LOGIN_PAGE: str = "http://localhost:8000/parabank/lookup.htm"
    REGISTER_PAGE: str = "http://localhost:8000/parabank/register.htm"
    OPEN_ACCOUNT_PAGE: str = "http://localhost:8000/parabank/openaccount.htm"
    ACCOUNT_OVERVIEW_PAGE: str = "http://localhost:8000/parabank/overview.htm"
    # There is an argument ?id= that contains the account number
    ACTIVITY_PAGE: str = "http://localhost:8000/parabank/activity.htm"
    # There is an argument ?id= that contains the transaction number
    TRANSACTION_PAGE: str = "http://localhost:8000/parabank/transaction.htm"
    TRANSFER_FUNDS_PAGE: str = "http://localhost:8000/parabank/transfer.htm"
    BILL_PAY_PAGE: str = "http://localhost:8000/parabank/billpay.htm"
    FIND_TRANS_PAGE: str = "http://localhost:8000/parabank/findtrans.htm"
    UPDATE_INFO_PAGE: str = "http://localhost:8000/parabank/updateprofile.htm"
    REQUEST_LOAN_PAGE: str = "http://localhost:8000/parabank/requestloan.htm"
    ADMIN_PAGE_PAGE: str = "http://localhost:8000/parabank/admin.htm"
    CONTACT_FORM_PAGE: str = "http://localhost:8000/parabank/contact.htm"


    def verify_element_presence(self, locator: tuple, timeout: int = 5) -> WebElement:
        """
        Verifies the webelement presence on the page.
        :param locator: The locator describing the webelement to be checked. Tuple containing the By
                        strategy and locator.
        :param timeout: The timeout for the explicit waiting. The default value is 5.
        :return: webelement
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.presence_of_element_located(locator))

    def verify_elements_presence(self, locator: tuple, timeout: int = 5) -> list[WebElement]:
        """
        Verifies the webelements presence on the page.
        :param locator: The locator describing the webelements to be checked. Tuple containing the By
                        strategy and locator.
        :param timeout: The timeout for the explicit waiting. The default value is 5.
        :return: webelement
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.presence_of_all_elements_located(locator))

    def verify_element_clickable(self, locator: tuple, timeout: int = 5) -> WebElement:
        """
        Verifies if the webelement is clickable.
        :param locator: The locator describing the webelement to be checked. Tuple containing the By
                        strategy and locator.
        :param timeout: The timeout for the explicit waiting. The default value is 5.
        :return: webelement
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.element_to_be_clickable(locator))

    def verify_element_visibility(self, element: WebElement, timeout: int = 5) -> WebElement:
        """
        Verifies if the webelement is visible.
        :param element: Webelement to be checked.
        :param timeout: The timeout for the explicit waiting. The default value is 5.
        :return: webelement
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.visibility_of(element))

    def verify_text_present_in_element(self, locator: tuple, text: str, timeout: int = 5) -> bool:
        """
        Verifies if the text is present in the webelement.
        :param locator: The locator describing the webelement to be checked. Tuple containing the By
                        strategy and locator.
        :param text: Text to be located in webelement.
        :param timeout: The timeout for the explicit waiting. The default value is 5.
        :return:
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.text_to_be_present_in_element(locator, text))

    def verify_title_contains(self, text: str, timeout: int = 5) -> bool:
        """
        Verifies if the text is present in the page title.
        :param text: Text to be located in page title.
        :param timeout: The timeout for the explicit waiting. The default value is 5.
        :return:
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.title_contains(text))

    def verify_element_selected(self, element: WebElement, timeout: int = 10) -> bool:
        """
        Verifies if the webelement is selected.
        :param element: Webelement to be checked.
        :param timeout: The timeout of the explicit waiting. The default value is 10.
        :return:
        """
        self._wait: WebDriverWait = WebDriverWait(self._driver, timeout)
        return self._wait.until(EC.element_to_be_selected(element))

    def get_list_values(self, dropdown_list: WebElement) -> list:
        """
        Returns the list of elements from the static dropdown (webelement).
        :param dropdown_list: Webelement that references the static dropdown.
        :return: List of elements of the dropdown.
        """
        self._values = []
        for element in dropdown_list.find_elements(By.TAG_NAME, "option"):
            self._values.append(element.text)
        return self._values

    def get_elements_texts(self, elements: list[WebElement]) -> list:
        """
        Returns the list of webelement texts from the list of webelements.
        :param elements: List of webelements
        :return: List of text strings
        """
        self._values = []
        for element in elements:
            self._values.append(element.text)
        return self._values

    def get_elements_numbers(self, elements: list[WebElement]) -> list:
        """
        Returns the list of webelement texts converted to float from the list of webelements.
        :param elements: List of webelements
        :return: List of text strings
        """
        self._values = []
        for element in elements:
            self._values.append(float(re.sub(r"[^0-9.]", "", element.text)))
        return self._values

    def select_value_from_dropdown_text(self, element: WebElement, text: str) -> None:
        """
        Selects the value from the list (webelement) using the text.
        :param element: Webelement that references the static dropdown.
        :param text: The text value to be selected.
        :return:
        """
        dropdown: Select = Select(element)
        dropdown.select_by_visible_text(text)

    def select_value_from_dropdown_index(self, element: WebElement, index: int) -> None:
        """
        Selects the value from the list (webelement) using the index value.
        :param element: Webelement that references the static dropdown.
        :param index: The index value to be selected.
        :return:
        """
        dropdown: Select = Select(element)
        dropdown.select_by_index(index)

    def get_page_title(self) -> str:
        """
        Returns the page title.
        :return:
        """
        return self._driver.title