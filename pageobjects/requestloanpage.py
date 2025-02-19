from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.activitypage import ActivityPage

class RequestLoanPage():
    """
    Class that holds the locators of the Request Loan page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    loan_amount: tuple = (By.ID, "amount")
    down_payment_amount: tuple = (By.ID, "downPayment")
    account_number: tuple = (By.ID, "fromAccountId")
    apply_button: tuple = (By.CSS_SELECTOR, "input[value='Apply Now']")
    # Loan status
    # Possible values: Approved, Denied
    loan_status: tuple = (By.ID, "loanStatus")
    loan_account_id: tuple = (By.ID, "newAccountId")
    # Div blocks w/ loan messages (either approved or denied)
    loan_approved_msg: tuple = (By.ID, "loanRequestApproved")
    loan_denied_msg: tuple = (By.ID, "loanRequestDenied")

    # Declaring the error labels
    # There's no field verification
    loan_request_error: tuple = (By.ID, "requestLoanError")

    def __init__(self, driver):
        self._driver = driver

    def get_loan_amount(self) -> WebElement:
        """
        Returns the loan amount field.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.loan_amount)

    def get_down_payment_amount(self) -> WebElement:
        """
        Returns the down payment amount field.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.down_payment_amount)

    def get_account_number(self) -> WebElement:
        """
        Returns the account number field.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.account_number)

    def get_apply_button(self) -> WebElement:
        """
        Returns the apply for the loan button.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.apply_button)

    def get_loan_status(self) -> WebElement:
        """
        Returns the loan status.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.loan_status)

    def get_loan_accout_id(self) -> ActivityPage:
        """
        Returns the loan account identifier link.
        :return: page object
        """
        self._driver.find_element(*RequestLoanPage.loan_account_id).click()
        return ActivityPage(self._driver)

    def get_loan_approved_msg(self) -> WebElement:
        """
        Returns the loan approved messsage.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.loan_approved_msg)

    def get_loan_denied_msg(self) -> WebElement:
        """
        Returns the loan denied messsage.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.loan_denied_msg)

    def get_loan_request_error(self) -> WebElement:
        """
        Returns the loan request error text.
        :return: webelement
        """
        return self._driver.find_element(*RequestLoanPage.loan_request_error)

