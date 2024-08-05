

from pages.BasePage import BasePage


class EnterValue(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _enterValuePage = "com.code2lead.kwad:id/EnterValue", #id
    _verifyIfPageDisplayed ="Enter some Value", # text
    _enterValue = "android.widget.EditText", #classname
    _submitBtn = "SUBMIT", # text

    def openEnterValuePage(self):
        self.clickElement(self._enterValuePage, "id")
    
    def verifyIfPageDisplayed(self):
        self.isElementDisplayed(self._verifyIfPageDisplayed, "text")
    
    def enterValue(self):
        self.sendKeys(25, self._enterValue, "classname")
    
    def clickSubmitButton(self):
        self.clickElement(self._submitBtn, "text")