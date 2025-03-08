import pytest
import allure

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage
from pageobjects.contactpage import ContactPage

class TestContactUs(BaseClass):

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for sending the customer care tickets")
    @allure.sub_suite("Contact us form tests")
    @allure.tag("Contact page", "Form", "Positive", "Support ticket")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 69")
    @allure.description("This test attempts to send the customer care support ticket.")
    @pytest.mark.contactus
    def test_contact_form_positive(self):
        """
        Tests attempts to send the customer care support ticket.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Sending support ticket", "Positive ticket")
        log.info("Clicking the Contact us icon.")
        contact_page = home_page.get_contact_icon()
        with allure.step("Step 1: Verify the proper page title"):
            log.info("Verifying if the the page title is correct.")
            assert contact_page.get_page_title() == contact_page.VALID_PAGE_TITLE
        with allure.step("Step 2: Enter the proper data"):
            name = faker.name()
            log.info(f"Entering the full name {name}.")
            contact_page.get_name().send_keys(name)
            email = faker.ascii_email()
            log.info(f"Entering the email address {email}.")
            contact_page.get_email_address().send_keys(email)
            phonenumber = faker.phone_number()
            log.info(f"Entering the phone number {phonenumber}.")
            contact_page.get_phone_number().send_keys(phonenumber)
            # Generate the message consisting of 5 sentences (defined in contact page object)
            message = faker.paragraph(ContactPage.MESSAGE_SENTENCES)
            log.info(f"Entering the message text {message}.")
            contact_page.get_message_body().send_keys(message)
            log.info("Clicking the Send button.")
            contact_page.get_send_button().click()
        with allure.step("Step 3: Verify the successful sending"):
            log.info("Verifying the successful sending of the form.")
            assert contact_page.get_success_message().text == contact_page.CUSTOMER_CARE_SUCCESS_MSG + name



