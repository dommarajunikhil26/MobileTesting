import utils.CustomLogger as cl
from pages.BasePage import BasePage


class EnterValue(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _enter_value_page = "com.code2lead.kwad:id/EnterValue" #id
    _verify_if_page_displayed ="Enter some Value" # text
    _enter_value = "android.widget.EditText" #classname
    _submit_btn = "SUBMIT" # text

    def openEnterValuePage(self):
        self.click_element(self._enter_value_page, "id")
        cl.allureLogs("Clicked on Enter Some Value Page")
    
    def verifyIfPageDisplayed(self):
        element = self.is_element_displayed(self._verify_if_page_displayed, "text")
        assert element == True
        cl.allureLogs("Page is verfied to be Enter Some Value Page")
    
    def enterValue(self):
        self.send_keys(25, self._enter_value, "classname")
        cl.allureLogs("Entered the number")
    
    def clickSubmitButton(self):
        self.click_element(self._submit_btn, "text")
        cl.allureLogs("Clicked on submit button")