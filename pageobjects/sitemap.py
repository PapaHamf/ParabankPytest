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
    driver: Chrome

    # Declaring the page objects (these need chaining)
    right_panel: tuple = (By.ID, "rightPanel")
    about_us_link: tuple = (By.LINK_TEXT, "About Us")
    services_link: tuple = (By.LINK_TEXT, "Services")
    admin_page_link: tuple = (By.LINK_TEXT, "Admin Page")

    # Declaring the account services page objects
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

    def get_about_us_link(self) -> AboutUs:
        """
        Returns the about us page object.
        :return: page object
        """
        r_panel = self._driver.find_element(*SiteMap.right_panel)
        r_panel.find_element(*SiteMap.about_us_link).click()
        return AboutUs(self._driver)

    def get_services_link(self) -> WebElement:
        """
        Returns the services link.
        :return: webelement
        """
        r_panel = self._driver.find_element(*SiteMap.right_panel)
        return r_panel.find_element(*SiteMap.services_link)

    def get_admin_page_link(self) -> AdminPage:
        """
        Returns the admin page object.
        :return: page object
        """
        r_panel = self._driver.find_element(*SiteMap.right_panel)
        r_panel.find_element(*SiteMap.admin_page_link).click()
        return AdminPage(self._driver)

    def get_open_account_link(self) -> OpenAccountPage:
        """
        Returns the open account page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.open_account_link).click()
        return OpenAccountPage(self._driver)

    def get_accounts_overview_link(self) -> AccountOverview:
        """
        Returns the accounts overview page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.accounts_overview_link).click()
        return AccountOverview(self._driver)

    def get_transfer_funds_link(self) -> TransferPage:
        """
        Returns the transfer funds page object.
        :return: page objectc
        """
        self._driver.find_element(*SiteMap.transfer_funds_link).click()
        return TransferPage(self._driver)

    def get_bill_pay_link(self) -> BillPayPage:
        """
        Returns the bill pay page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.bill_pay_link).click()
        return BillPayPage(self._driver)

    def get_find_transactions_link(self) -> FindTransactionPage:
        """
        Returns the find transactions page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.find_transactions_link).click()
        return FindTransactionPage(self._driver)

    def get_update_info_link(self) -> UpdateProfilePage:
        """
        Returns the update profile information page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.update_info_link).click()
        return UpdateProfilePage(self._driver)

    def get_request_loan_link(self) -> RequestLoanPage:
        """
        Returns the request loan page object.
        :return: page object
        """
        self._driver.find_element(*SiteMap.request_loan_link).click()
        return RequestLoanPage(self._driver)

    def get_log_out_link(self) -> WebElement:
        """
        Returns the log out link.
        :return: webelement
        """
        return self._driver.find_element(*SiteMap.log_out_link)