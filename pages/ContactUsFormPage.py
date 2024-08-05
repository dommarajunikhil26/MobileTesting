import utils.CustomLogger as cl
from pages.BasePage import BasePage


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _enter_contact_form_page = "com.code2lead.kwad:id/ContactUs"    #id
    _verify_if_page_displayed = "Contact Us form"   #text
    _enter_name = "Enter Name"  #text
    _enter_email = "Enter Email" #text
    _enter_address = "Enter Address"    #text
    _enter_mobile_number = "Enter Mobile No"
    _submit_btn = "SUBMIT"  #text
    _registration_success = "register Successfully!"    #text

    def openContactFormPage(self):
        self.click_element(self._enter_contact_form_page, "id")
        cl.allureLogs("Clicked on Contact Form Page")
    
    def verifyContactFormPage(self):
        element = self.is_element_displayed(self._verify_if_page_displayed, "text")
        assert element == True
        cl.allureLogs("Verified the Contact Form Page")

    def enterFormDetailsAndSubmit(self):
        self.send_keys("Admin", self._enter_name, "text")
        self.send_keys("Admin@gmail.com", self._enter_email, "text")
        self.send_keys("Admin st nw", self._enter_address, "text")
        self.send_keys("123456789", self._enter_mobile_number, "text")
        self.click_element(self._submit_btn, "text")
        
    def verifyRegistration(self):
        self.is_element_displayed(self._registration_success, "text")