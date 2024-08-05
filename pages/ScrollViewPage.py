from utils.Gestures import scroll
from pages.BasePage import BasePage
import utils.CustomLogger as cl

class ScrollViewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _open_scroll_view_page = "com.code2lead.kwad:id/ScrollView" # id
    _verify_scroll_view_page = "ScrollView"  # text
    _button16 = "BUTTON16" # text
    _alert_pop = "com.code2lead.kwad:id/alertTitle" # id
    _yes_btn = "YES" # text
    _no_btn = "NO"  # text

    def openScrollViewPage(self):
        self.click_element(self._open_scroll_view_page, "id")
        cl.allureLogs("Clicked on Scroll View Page")

    def verifyIfPageIsDisplayed(self):
        element = self.is_element_displayed(self._verify_scroll_view_page, "text")
        cl.allureLogs("Verfied the page")
        return element
    
    def scrollToBtn16(self):
        scroll(self.driver, self._button16)
        element = self.is_element_displayed(self._button16, "text")
        cl.allureLogs("Checked if the button 16 is visible")
        return element
    
    def clickBtn16(self):
        self.click_element(self._button16, "text")
        cl.allureLogs("Clicked on button 16")
    
    def checkAlert(self):
        element =self.is_element_displayed(self._alert_pop, "id")
        cl.allureLogs("Alert pop is displayed")
        return element
    
    def clickNo(self):
        self.click_element(self._no_btn, "text")
        cl.allureLogs("Clicked on No")
    
    def clickYes(self):
        self.click_element(self._yes_btn, "text")
        cl.allureLogs("Clicked on Yes")
    
    def verifyIfButton16IsDisplayed(self):
        element = self.is_element_displayed(self._button16, "text")
        cl.allureLogs("Button 16 is displayed")
        return element
    
    def verifyIfReturnedToHome(self):
        element = self.is_element_displayed(self._open_scroll_view_page, "id")
        cl.allureLogs("In Home Page of the App")
        return element