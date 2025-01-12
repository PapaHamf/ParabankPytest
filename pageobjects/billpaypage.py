from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class TransferPage():
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

    def __init__(self, driver):
        self._driver = driver