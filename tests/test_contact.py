from seleniumbase import BaseCase


class ContactTest(BaseCase):

    def test_contact_page(self):
        # open page
        self.open("https://practice.automationbro.com/contact")

        # scroll to the empty form and take screenshot
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty_contact_form", "custom_screenshots")

        # fill in all the fields
        self.send_keys('.contact-name input', 'Test Name')
        self.send_keys('.contact-email input', 'test@mail.com')
        self.send_keys('.contact-phone input', '123456789')
        self.send_keys('.contact-message textarea', 'This is a test message')

        # take screenshot when the form is filled
        self.save_screenshot("filled_contact_form", "custom_screenshots")

        # click the submit button
        self.click("#evf-submit-277")

        # verify submit message
        self.assert_text("Thanks for us! We will be in touch with you shortly", "div[role=alert]")