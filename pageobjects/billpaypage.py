from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class BillPayPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    payee_name: tuple = (By.NAME, "payee.name")
    payee_street: tuple = (By.NAME, "payee.address.street")
    payee_city: tuple = (By.NAME, "payee.address.city")
    payee_state: tuple = (By.NAME, "payee.address.state")
    payee_post_code: tuple = (By.NAME, "payee.address.zipCode")
    payee_phonenumber: tuple = (By.NAME, "payee.phoneNumber")
    payee_account_number: tuple = (By.NAME, "payee.accountNumber")
    payee_verify_account: tuple = (By.NAME, "verifyAccount")
    payment_amount: tuple = (By.NAME, "amount")
    source_account: tuple = (By.NAME, "fromAccountId")
    payment_button: tuple = (By.CSS_SELECTOR, "input[value='Send Payment']")

    # Declaring the error labels
    payee_name_error: tuple = (By.ID, "validationModel-name")
    payee_street_error: tuple = (By.ID, "validationModel-street")
    payee_city_error: tuple = (By.ID, "validationModel-city")
    payee_state_error: tuple = (By.ID, "validationModel-state")
    payee_post_code_error: tuple = (By.ID, "validationModel-zipCode")
    payee_phonenumber_error: tuple = (By.ID, "validationModel-phoneNumber")
    payee_account_number_empty_error: tuple = (By.ID, "validationModel-account-empty")
    payee_account_number_invalid_error: tuple = (By.ID, "validationModel-account-invalid")
    payee_verify_account_empty_error: tuple = (By.ID, "validationModel-verifyAccount-empty")
    payee_verify_account_invalid_error: tuple = (By.ID, "validationModel-verifyAccount-invalid")
    payee_verify_account_mismatch_error: tuple = (By.ID, "validationModel-verifyAccount-mismatch")
    payee_amount_empty_error: tuple = (By.ID, "validationModel-amount-empty")
    payee_amount_invalid_error: tuple = (By.ID, "validationModel-amount-invalid")

    # Success message
    payment_success: tuple = (By.ID, "billpayResult")
    payment_success_title: tuple = (By.CLASS_NAME, "title")
    success_payee_name: tuple = (By.ID, "payeeName")
    success_amount: tuple = (By.ID, "amount")

    def __init__(self, driver):
        self._driver = driver

    def get_payee_name(self):
        """
        Returns the payee name field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_name)

    def get_payee_street(self):
        """
        Returns the payee address street name & number field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_street)

    def get_payee_city(self):
        """
        Returns the payee address city field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_city)

    def get_payee_state(self):
        """
        Returns the payee address state field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_state)

    def get_payee_post_code(self):
        """
        Returns the payee address post code field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_post_code)

    def get_payee_phonenumber(self):
        """
        Returns the payee phone number field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_phonenumber)

    def get_payee_account_number(self):
        """
        Returns the payee account_number field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_account_number)

    def get_payee_verify_account(self):
        """
        Returns the payee verify account number field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_verify_account)

    def get_payment_amount(self):
        """
        Returns the payment amount field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payment_amount)

    def get_source_account(self):
        """
        Returns the source account field.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.source_account)

    def get_payment_button(self):
        """
        Returns the payment button.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payment_button)

    def get_payment_success(self):
        """
        Returns the payment success message block.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payment_success)

    def get_payment_success_title(self):
        """
        Returns the payment success message title.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payment_success_title)

    def get_success_amount(self):
        """
        Returns the payment success amount.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.success_amount)

    def get_success_payee_name(self):
        """
        Returns the payment success amount.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.success_payee_name)

    def get_payee_name_error(self):
        """
        Returns the payee name field error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_name_error)

    def get_payee_street_error(self):
        """
        Returns the payee street name and number field error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_street_error)

    def get_payee_city_error(self):
        """
        Returns the payee city field error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_city_error)

    def get_payee_state_error(self):
        """
        Returns the payee state field error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_state_error)

    def get_payee_post_code_error(self):
        """
        Returns the payee post code field error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_post_code_error)

    def get_payee_phonenumber_error(self):
        """
        Returns the payee phone number field error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_phonenumber_error)

    def get_account_number_empty_error(self):
        """
        Returns the account number field empty error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_account_number_empty_error)

    def get_account_number_invalid_error(self):
        """
        Returns the account number field invalid error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_account_number_invalid_error)

    def get_verify_account_empty_error(self):
        """
        Returns the verify account number field empty error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_verify_account_empty_error)

    def get_verify_account_invalid_error(self):
        """
        Returns the verify account number field invalid error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_verify_account_invalid_error)

    def get_verify_account_mismatch_error(self):
        """
        Returns the verify account number field mismatch error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_verify_account_mismatch_error)

    def get_payee_amount_empty_error(self):
        """
        Returns the amount field empty error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_amount_empty_error)

    def get_payee_amount_invalid_error(self):
        """
        Returns the amount field invalid error text.
        :return: webelement
        """
        return self._driver.find_element(*BillPayPage.payee_amount_invalid_error)


