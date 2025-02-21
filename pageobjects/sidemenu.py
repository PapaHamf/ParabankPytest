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
    LEFT_PANEL: tuple = (By.ID, "leftPanel")
    LEFT_PANEL_HEADER: tuple = (By.CLASS_NAME, "smallText")
    OPEN_ACCOUNT_LINK: tuple = (By.PARTIAL_LINK_TEXT, "Open New")
    ACCOUNTS_OVERVIEW_LINK: tuple = (By.PARTIAL_LINK_TEXT, "Accounts")
    TRANSFER_FUNDS_LINK: tuple = (By.PARTIAL_LINK_TEXT, "Transfer")
    BILL_PAY_LINK: tuple = (By.LINK_TEXT, "Bill Pay")
    FIND_TRANSACTIONS_LINK: tuple = (By.PARTIAL_LINK_TEXT, "Find")
    UPDATE_INFO_LINK: tuple = (By.PARTIAL_LINK_TEXT, "Update Contact")
    REQUEST_LOAN_LINK: tuple = (By.LINK_TEXT, "Request Loan")
    LOG_OUT_LINK: tuple = (By.LINK_TEXT, "Log Out")

    def __init__(self, driver):
        self._driver = driver

    def get_left_panel_header(self) -> WebElement:
        """
        Returns the left panel header text.
        :return: webelement
        """
        return self._driver.find_element(*SideMenu.LEFT_PANEL_HEADER)

    def get_open_account_page(self) -> OpenAccountPage:
        """
        Returns the open account page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.OPEN_ACCOUNT_LINK).click()
        return OpenAccountPage(self._driver)

    def get_accounts_overview_page(self) -> AccountOverview:
        """
        Returns the accounts overview page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.ACCOUNTS_OVERVIEW_LINK).click()
        return AccountOverview(self._driver)

    def get_transfer_funds_page(self) -> TransferPage:
        """
        Returns the transfer funds page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.TRANSFER_FUNDS_LINK).click()
        return TransferPage(self._driver)

    def get_bill_pay_page(self) -> BillPayPage:
        """
        Returns the bill pay page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.BILL_PAY_LINK).click()
        return BillPayPage(self._driver)

    def get_find_transactions_page(self) -> FindTransactionPage:
        """
        Returns the find transactions page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.FIND_TRANSACTIONS_LINK).click()
        return FindTransactionPage(self._driver)

    def get_update_info_page(self) -> UpdateProfilePage:
        """
        Returns the update profile information page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.UPDATE_INFO_LINK).click()
        return UpdateProfilePage(self._driver)

    def get_request_loan_page(self) -> RequestLoanPage:
        """
        Returns the request loan page object.
        :return: page object
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        l_panel.find_element(*SideMenu.REQUEST_LOAN_LINK).click()
        return RequestLoanPage(self._driver)

    def get_log_out_link(self) -> WebElement:
        """
        Returns the log out link.
        :return: webelement
        """
        l_panel = self._driver.find_element(*SideMenu.LEFT_PANEL)
        return l_panel.find_element(*SideMenu.LOG_OUT_LINK)
