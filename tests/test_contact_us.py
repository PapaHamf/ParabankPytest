import time

import pytest
import allure

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage
from pageobjects.contactpage import ContactPage
from pageobjects.intwebmailpage import IntMailPage

class TestContactUs(BaseClass):

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for sending the customer care tickets")
    @allure.sub_suite("Contact us form tests")
    @allure.tag("Contact page", "Form", "Positive", "Support ticket")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 69")
    @allure.description("This test attempts to send the customer care support ticket.")
    @pytest.mark.positive
    @pytest.mark.functional
    @pytest.mark.skip
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
            data_collection.add_data("name", name)
            log.info(f"Entering the full name {name}.")
            contact_page.get_name().send_keys(name)
            email = faker.ascii_email()
            data_collection.add_data("email", email)
            log.info(f"Entering the email address {email}.")
            contact_page.get_email_address().send_keys(email)
            phonenumber = faker.phone_number()
            data_collection.add_data("phonenumber", phonenumber)
            log.info(f"Entering the phone number {phonenumber}.")
            contact_page.get_phone_number().send_keys(phonenumber)
            # Generate the message consisting of 5 sentences (defined in contact page object)
            message = faker.paragraph(ContactPage.MESSAGE_SENTENCES)
            data_collection.add_data("message", message)
            log.info(f"Entering the message text {message}.")
            contact_page.get_message_body().send_keys(message)
            log.info("Clicking the Send button.")
            contact_page.get_send_button().click()
            data_collection.save_data()
        with allure.step("Step 3: Verify the successful sending"):
            log.info("Verifying the successful sending of the form.")
            assert contact_page.get_success_message().text == contact_page.CUSTOMER_CARE_SUCCESS_MSG + name

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for sending the customer care tickets")
    @allure.sub_suite("Contact us form tests")
    @allure.tag("Contact page", "Form", "Negative", "Support ticket")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 70")
    @allure.description("This test attempts to send the customer care support ticket with all fields empty.")
    @pytest.mark.negative
    @pytest.mark.functional
    @pytest.mark.skip
    def test_contact_form_negative(self):
        """
        Tests attempts to send the customer care support ticket with all fields empty.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        log.info("Clicking the Contact us icon.")
        contact_page = home_page.get_contact_icon()
        with allure.step("Step 1: Verify the proper page title"):
            log.info("Verifying if the the page title is correct.")
            assert contact_page.get_page_title() == contact_page.VALID_PAGE_TITLE
        with allure.step("Step 2: Click the button w/o entering data"):
            log.info("Clicking the Send button.")
            contact_page.get_send_button().click()
        with allure.step("Step 3: Verify the number of errors"):
            log.info("Verifying if the number of displayed errors is correct.")
            # Four empty fields
            no_of_errors = 4
            assert contact_page.get_errors() == no_of_errors

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for sending the customer care tickets")
    @allure.sub_suite("Contact us form tests")
    @allure.tag("Contact page", "Form", "Positive", "Confirmation message")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 71")
    @allure.description("This test verifies if the support ticket confirmation message is sent to the"
                        " given customer e-mail address.")
    @pytest.mark.positive
    @pytest.mark.functional
    @pytest.mark.skip
    def test_contact_form_verify_email(self):
        """
        Tests attempts to verify if the support ticket confirmation message is sent to the given
        customer e-mail address.
        :return:
        """
        log = self.get_logger()
        faker = self.get_faker()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        data_collection = ExcelData("Sending support ticket", "Confirmation message")
        log.info("Clicking the Contact us icon.")
        contact_page = home_page.get_contact_icon()
        with allure.step("Step 1: Verify the proper page title"):
            log.info("Verifying if the the page title is correct.")
            assert contact_page.get_page_title() == contact_page.VALID_PAGE_TITLE
        with allure.step("Step 2: Enter the proper data"):
            name = faker.name()
            data_collection.add_data("name", name)
            log.info(f"Entering the full name {name}.")
            contact_page.get_name().send_keys(name)
            email = IntMailPage.TICKET_EMAIL
            data_collection.add_data("email", email)
            log.info(f"Entering the email address {email}.")
            contact_page.get_email_address().send_keys(email)
            phonenumber = faker.phone_number()
            data_collection.add_data("phonenumber", phonenumber)
            log.info(f"Entering the phone number {phonenumber}.")
            contact_page.get_phone_number().send_keys(phonenumber)
            # Generate the message consisting of 5 sentences (defined in contact page object)
            message = faker.paragraph(ContactPage.MESSAGE_SENTENCES)
            data_collection.add_data("message", message)
            log.info(f"Entering the message text {message}.")
            contact_page.get_message_body().send_keys(message)
            log.info("Clicking the Send button.")
            contact_page.get_send_button().click()
            data_collection.save_data()
        with allure.step("Step 3: Verify the successful sending"):
            log.info("Verifying the successful sending of the form.")
            assert contact_page.get_success_message().text == contact_page.CUSTOMER_CARE_SUCCESS_MSG + name
        with allure.step("Step 4: Verify the message in the inbox"):
            log.info("Creating new tab and switching to it.")
            self.driver.switch_to.new_window('tab')
            self.driver.get(IntMailPage.TICKET_SERVER)
            webmail_page = IntMailPage(self.driver)
            webmail_page.get_external_email_address().send_keys(IntMailPage.TICKET_EMAIL)
            webmail_page.get_external_password().send_keys(IntMailPage.TICKET_PASSWORD)
            inbox_page = webmail_page.get_external_login_button()
            sender_name = inbox_page.get_external_message_senders()[0].text
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            assert "Parabank" in sender_name

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for sending the customer care tickets")
    @allure.sub_suite("Contact us form tests")
    @allure.tag("Contact page", "Form", "Negative", "Resizing")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 72")
    @allure.description("This test attempts to resize the support ticket message text area.")
    @pytest.mark.negative
    @pytest.mark.functional
    @pytest.mark.skip
    def test_contact_form_resize_textarea(self):
        """
        Tests attempts to resize the support ticket message text area.
        :return:
        """
        log = self.get_logger()
        self.driver.get(BasePage.HOME_PAGE)
        home_page = HomePage(self.driver)
        log.info("Clicking the Contact us icon.")
        contact_page = home_page.get_contact_icon()
        with allure.step("Step 1: Verify the proper page title"):
            log.info("Verifying if the the page title is correct.")
            assert contact_page.get_page_title() == contact_page.VALID_PAGE_TITLE
        with allure.step("Step 2: Resize the text area"):
            log.info("Resizing the text area.")
            contact_page.resize_message_body_text_area()
        with allure.step("Step 3: Verify if the text area was enlarged"):
            log.info("Verifying if the text area was enlarged properly.")
            sizes = contact_page.get_message_body_size()
            assert sizes[0] >= ContactPage.MESSAGE_BODY_WIDTH and sizes[1] >= ContactPage.MESSAGE_BODY_HEIGHT


