from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.activitypage import ActivityPage
from pageobjects.basepage import BasePage

class RequestLoanPage(BasePage):
    """
    Class that holds the locators of the Request Loan page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    LOAN_AMOUNT: tuple = (By.ID, "amount")
    DOWN_PAYMENT_AMOUNT: tuple = (By.ID, "downPayment")
    ACCOUNT_NUMBER: tuple = (By.ID, "fromAccountId")
    APPLY_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Apply Now']")
    # Loan status
    # Possible values: Approved, Denied
    LOAN_STATUS: tuple = (By.ID, "loanStatus")
    LOAN_ACCOUNT_ID: tuple = (By.ID, "newAccountId")
    # Div blocks w/ loan messages (either approved or denied)
    LOAN_APPROVED_MSG: tuple = (By.ID, "loanRequestApproved")
    LOAN_DENIED_MSG: tuple = (By.ID, "loanRequestDenied")

    # Declaring the error labels
    # There's no field verification
    LOAN_REQUEST_ERROR: tuple = (By.ID, "requestLoanError")

    def __init__(self, driver):
        self._driver = driver

    def get_loan_amount(self) -> WebElement:
        """
        Returns the loan amount field.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.LOAN_AMOUNT)

    def get_down_payment_amount(self) -> WebElement:
        """
        Returns the down payment amount field.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.DOWN_PAYMENT_AMOUNT)

    def get_account_number(self) -> WebElement:
        """
        Returns the account number field.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.ACCOUNT_NUMBER)

    def get_apply_button(self) -> WebElement:
        """
        Returns the apply for the loan button.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.APPLY_BUTTON)

    def get_loan_status(self) -> WebElement:
        """
        Returns the loan status.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.LOAN_STATUS)

    def get_loan_accout_id(self) -> ActivityPage:
        """
        Returns the loan account identifier link.
        :return: page object
        """
        self._driver.find_element(*RequestLoanPage.LOAN_ACCOUNT_ID).click()
        return ActivityPage(self._driver)

    def get_loan_approved_msg(self) -> WebElement:
        """
        Returns the loan approved messsage.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.LOAN_APPROVED_MSG)

    def get_loan_denied_msg(self) -> WebElement:
        """
        Returns the loan denied messsage.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.LOAN_DENIED_MSG)

    def get_loan_request_error(self) -> WebElement:
        """
        Returns the loan request error text.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.LOAN_REQUEST_ERROR)

