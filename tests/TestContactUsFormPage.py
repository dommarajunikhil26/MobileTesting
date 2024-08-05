import unittest
import utils.CustomLogger as cl
import pytest
from pages.ContactUsFormPage import ContactForm

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestContactUsFormPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def set_up_page_objects(self):
        self.cp = ContactForm(self.driver)

    @pytest.mark.order(3)
    def test_openContactUsFormPage(self):
        cl.allureLogs("App Launched")
        self.cp.openContactFormPage()
        self.assertTrue(self.cp.verifyContactFormPage(), "Contact Us Form Page not visible")

    @pytest.mark.order(4)
    def test_enterFormDetails(self):
        self.cp.enterFormDetailsAndSubmit()
        self.assertTrue(self.cp.verifyRegistration(), "Registration not successful")
    