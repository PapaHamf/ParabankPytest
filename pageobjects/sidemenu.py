from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.openaccountpage import OpenAccountPage
from pageobjects.accountoverviewpage import AccountOverview
from pageobjects.transferpage import TransferPage
from pageobjects.billpaypage import BillPayPage
from pageobjects.findtransactionspage import FindTransactionPage
from pageobjects.updateprofilepage import UpdateProfilePage
from pageobjects.requestloanpage import RequestLoanPage

class SideMenu():
    """
    Class that holds the locators of the Side menu and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects
    left_panel: tuple = (By.ID, "leftPanel")
    left_panel_header: tuple = (By.CLASS_NAME, "smallText")
    open_account_link: tuple = (By.PARTIAL_LINK_TEXT, "Open New")
    accounts_overview_link: tuple = (By.PARTIAL_LINK_TEXT, "Accounts")
    transfer_funds_link: tuple = (By.PARTIAL_LINK_TEXT, "Transfer")
    bill_pay_link: tuple = (By.LINK_TEXT, "Bill Pay")
    find_transactions_link: tuple = (By.PARTIAL_LINK_TEXT, "Find")
    update_info_link: tuple = (By.PARTIAL_LINK_TEXT, "Update Contact")
    request_loan_link: tuple = (By.LINK_TEXT, "Request Loan")
    log_out_link: tuple = (By.LINK_TEXT, "Log Out")

    def __init__(self, driver):
        self._driver = driver

    def get_left_panel_header(self) -> WebElement:
        """
        Returns the left panel header text.
        :return: webelement
        """
        return self._driver.find_element(*SideMenu.left_panel_header)

    def get_open_account_page(self) -> OpenAccountPage:
        """
        Returns the open account page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.open_account_link).click()
        return OpenAccountPage(self._driver)

    def get_accounts_overview_page(self) -> AccountOverview:
        """
        Returns the accounts overview page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.accounts_overview_link).click()
        return AccountOverview(self._driver)

    def get_transfer_funds_page(self) -> TransferPage:
        """
        Returns the transfer funds page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.transfer_funds_link).click()
        return TransferPage(self._driver)

    def get_bill_pay_page(self) -> BillPayPage:
        """
        Returns the bill pay page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.bill_pay_link).click()
        return BillPayPage(self._driver)

    def get_find_transactions_page(self) -> FindTransactionPage:
        """
        Returns the find transactions page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.find_transactions_link).click()
        return FindTransactionPage(self._driver)

    def get_update_info_page(self) -> UpdateProfilePage:
        """
        Returns the update profile information page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.update_info_link).click()
        return UpdateProfilePage(self._driver)

    def get_request_loan_page(self) -> RequestLoanPage:
        """
        Returns the request loan page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        l_panel.find_element(*SideMenu.request_loan_link).click()
        return RequestLoanPage(self._driver)

    def get_log_out_link(self) -> WebElement:
        """
        Returns the log out link.
        :return: webelement
        """
        l_panel = self._driver.find_element(*SideMenu.left_panel)
        return l_panel.find_element(*SideMenu.log_out_link)
