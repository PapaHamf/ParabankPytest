from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.aboutus import AboutUs
from pageobjects.adminpage import AdminPage
from pageobjects.openaccountpage import OpenAccountPage
from pageobjects.accountoverviewpage import AccountOverview
from pageobjects.transferpage import TransferPage
from pageobjects.billpaypage import BillPayPage
from pageobjects.findtransactionspage import FindTransactionPage
from pageobjects.updateprofilepage import UpdateProfilePage
from pageobjects.requestloanpage import RequestLoanPage

class SiteMap():
    """
    Class that holds the locators of the Site map page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (these need chaining)
    RIGHT_PANEL: tuple = (By.ID, "rightPanel")
    ABOUT_US_LINK: tuple = (By.LINK_TEXT, "About Us")
    SERVICES_LINK: tuple = (By.LINK_TEXT, "Services")
    ADMIN_PAGE_LINK: tuple = (By.LINK_TEXT, "Admin Page")

    # Declaring the account services page objects
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

    def get_about_us_link(self) -> AboutUs:
        """
        Returns the about us page object.
        :return: page object
        """
        r_panel = self._driver.find_element(*SiteMap.RIGHT_PANEL)
        r_panel.find_element(*SiteMap.ABOUT_US_LINK).click()
        return AboutUs(self._driver)

    def get_services_link(self) -> WebElement:
        """
        Returns the services link.
        :return: webelement
        """
        r_panel = self._driver.find_element(*SiteMap.RIGHT_PANEL)
        return r_panel.find_element(*SiteMap.SERVICES_LINK)

    def get_admin_page_link(self) -> AdminPage:
        """
        Returns the admin page object.
        :return: page object
        """
        r_panel = self._driver.find_element(*SiteMap.RIGHT_PANEL)
        r_panel.find_element(*SiteMap.ADMIN_PAGE_LINK).click()
        return AdminPage(self._driver)

    def get_open_account_link(self) -> OpenAccountPage:
        """
        Returns the open account page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.OPEN_ACCOUNT_LINK).click()
        return OpenAccountPage(self._driver)

    def get_accounts_overview_link(self) -> AccountOverview:
        """
        Returns the accounts overview page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.ACCOUNTS_OVERVIEW_LINK).click()
        return AccountOverview(self._driver)

    def get_transfer_funds_link(self) -> TransferPage:
        """
        Returns the transfer funds page object.
        :return: page objectc
        """
        self._driver.find_element(*SiteMap.TRANSFER_FUNDS_LINK).click()
        return TransferPage(self._driver)

    def get_bill_pay_link(self) -> BillPayPage:
        """
        Returns the bill pay page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.BILL_PAY_LINK).click()
        return BillPayPage(self._driver)

    def get_find_transactions_link(self) -> FindTransactionPage:
        """
        Returns the find transactions page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.FIND_TRANSACTIONS_LINK).click()
        return FindTransactionPage(self._driver)

    def get_update_info_link(self) -> UpdateProfilePage:
        """
        Returns the update profile information page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.UPDATE_INFO_LINK).click()
        return UpdateProfilePage(self._driver)

    def get_request_loan_link(self) -> RequestLoanPage:
        """
        Returns the request loan page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.REQUEST_LOAN_LINK).click()
        return RequestLoanPage(self._driver)

    def get_log_out_link(self) -> WebElement:
        """
        Returns the log out link.
        :return: webelement
        """
        return self._driver.find_element(*SiteMap.LOG_OUT_LINK)