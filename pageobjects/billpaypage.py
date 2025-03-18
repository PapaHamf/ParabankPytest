from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class BillPayPage(BasePage):
    """
    Class that holds the locators of the Bill Pay page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    PAYEE_NAME: tuple = (By.NAME, "payee.name")
    PAYEE_STREET: tuple = (By.NAME, "payee.address.street")
    PAYEE_CITY: tuple = (By.NAME, "payee.address.city")
    PAYEE_STATE: tuple = (By.NAME, "payee.address.state")
    PAYEE_POST_CODE: tuple = (By.NAME, "payee.address.zipCode")
    PAYEE_PHONENUMBER: tuple = (By.NAME, "payee.phoneNumber")
    PAYEE_ACCOUNT_NUMBER: tuple = (By.NAME, "payee.accountNumber")
    PAYEE_VERIFY_ACCOUNT: tuple = (By.NAME, "verifyAccount")
    PAYMENT_AMOUNT: tuple = (By.NAME, "amount")
    SOURCE_ACCOUNT: tuple = (By.NAME, "fromAccountId")
    PAYMENT_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Send Payment']")

    # Declaring the error labels
    PAYEE_NAME_ERROR: tuple = (By.ID, "validationModel-name")
    PAYEE_STREET_ERROR: tuple = (By.ID, "validationModel-street")
    PAYEE_CITY_ERROR: tuple = (By.ID, "validationModel-city")
    PAYEE_STATE_ERROR: tuple = (By.ID, "validationModel-state")
    PAYEE_POST_CODE_ERROR: tuple = (By.ID, "validationModel-zipCode")
    PAYEE_PHONENUMBER_ERROR: tuple = (By.ID, "validationModel-phoneNumber")
    PAYEE_ACCOUNT_NUMBER_EMPTY_ERROR: tuple = (By.ID, "validationModel-account-empty")
    PAYEE_ACCOUNT_NUMBER_INVALID_ERROR: tuple = (By.ID, "validationModel-account-invalid")
    PAYEE_VERIFY_ACCOUNT_EMPTY_ERROR: tuple = (By.ID, "validationModel-verifyAccount-empty")
    PAYEE_VERIFY_ACCOUNT_INVALID_ERROR: tuple = (By.ID, "validationModel-verifyAccount-invalid")
    PAYEE_VERIFY_ACCOUNT_MISMATCH_ERROR: tuple = (By.ID, "validationModel-verifyAccount-mismatch")
    PAYEE_AMOUNT_EMPTY_ERROR: tuple = (By.ID, "validationModel-amount-empty")
    PAYEE_AMOUNT_INVALID_ERROR: tuple = (By.ID, "validationModel-amount-invalid")
    PAYMENT_ERROR: tuple = (By.ID, "billpayError")

    # Success message
    PAYMENT_SUCCESS: tuple = (By.ID, "billpayResult")
    PAYMENT_SUCCESS_TITLE: tuple = (By.CLASS_NAME, "title")
    SUCCESS_PAYEE_NAME: tuple = (By.ID, "payeeName")
    SUCCESS_AMOUNT: tuple = (By.ID, "amount")

    # Declaring success and error messages
    BILL_PAYMENT_SUCCESS_MSG = "Bill Payment Complete"
    BILL_PAYMENT_ERROR_TITLE = "Error!"
    BILL_PAYMENT_ERROR_MSG = "An internal error has occurred and has been logged."

    def __init__(self, driver):
        self._driver = driver

    def get_payee_name(self) -> WebElement:
        """
        Returns the payee name field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_NAME)

    def get_payee_street(self) -> WebElement:
        """
        Returns the payee address street name & number field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_STREET)

    def get_payee_city(self) -> WebElement:
        """
        Returns the payee address city field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_CITY)

    def get_payee_state(self) -> WebElement:
        """
        Returns the payee address state field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_STATE)

    def get_payee_post_code(self) -> WebElement:
        """
        Returns the payee address post code field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_POST_CODE)

    def get_payee_phonenumber(self) -> WebElement:
        """
        Returns the payee phone number field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_PHONENUMBER)

    def get_payee_account_number(self) -> WebElement:
        """
        Returns the payee account_number field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_ACCOUNT_NUMBER)

    def get_payee_verify_account(self) -> WebElement:
        """
        Returns the payee verify account number field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_VERIFY_ACCOUNT)

    def get_payment_amount(self) -> WebElement:
        """
        Returns the payment amount field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYMENT_AMOUNT)

    def get_source_account(self) -> WebElement:
        """
        Returns the source account field.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.SOURCE_ACCOUNT)

    def get_payment_button(self) -> WebElement:
        """
        Returns the payment button.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYMENT_BUTTON)

    def get_payment_success(self) -> WebElement:
        """
        Returns the payment success message block.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYMENT_SUCCESS)

    def get_payment_success_title(self) -> WebElement:
        """
        Returns the payment success message title.
        :return: webelement
        """
        return self.get_payment_success().find_element(*BillPayPage.PAYMENT_SUCCESS_TITLE)

    def get_success_amount(self) -> WebElement:
        """
        Returns the payment success amount.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.SUCCESS_AMOUNT)

    def get_success_payee_name(self) -> WebElement:
        """
        Returns the payment success amount.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.SUCCESS_PAYEE_NAME)

    def get_payee_name_error(self) -> WebElement:
        """
        Returns the payee name field error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_NAME_ERROR)

    def get_payee_street_error(self) -> WebElement:
        """
        Returns the payee street name and number field error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_STREET_ERROR)

    def get_payee_city_error(self) -> WebElement:
        """
        Returns the payee city field error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_CITY_ERROR)

    def get_payee_state_error(self) -> WebElement:
        """
        Returns the payee state field error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_STATE_ERROR)

    def get_payee_post_code_error(self) -> WebElement:
        """
        Returns the payee post code field error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_POST_CODE_ERROR)

    def get_payee_phonenumber_error(self) -> WebElement:
        """
        Returns the payee phone number field error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_PHONENUMBER_ERROR)

    def get_account_number_empty_error(self) -> WebElement:
        """
        Returns the account number field empty error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_ACCOUNT_NUMBER_EMPTY_ERROR)

    def get_account_number_invalid_error(self) -> WebElement:
        """
        Returns the account number field invalid error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_ACCOUNT_NUMBER_INVALID_ERROR)

    def get_verify_account_empty_error(self) -> WebElement:
        """
        Returns the verify account number field empty error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_VERIFY_ACCOUNT_EMPTY_ERROR)

    def get_verify_account_invalid_error(self) -> WebElement:
        """
        Returns the verify account number field invalid error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_VERIFY_ACCOUNT_INVALID_ERROR)

    def get_verify_account_mismatch_error(self) -> WebElement:
        """
        Returns the verify account number field mismatch error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_VERIFY_ACCOUNT_MISMATCH_ERROR)

    def get_payee_amount_empty_error(self) -> WebElement:
        """
        Returns the amount field empty error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_AMOUNT_EMPTY_ERROR)

    def get_payee_amount_invalid_error(self) -> WebElement:
        """
        Returns the amount field invalid error text.
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYEE_AMOUNT_INVALID_ERROR)

    def get_payment_error(self) -> WebElement:
        """
        Returns the payment error text (internal).
        :return: webelement
        """
        return self.verify_element_presence(BillPayPage.PAYMENT_ERROR)

