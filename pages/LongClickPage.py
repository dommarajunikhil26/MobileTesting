from pages.BasePage import BasePage
from utils.Gestures import long_press
import utils.CustomLogger as cl

class LongClick(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver
    
    _verify_long_click_page = "ENTER YOUR PASSWORD" # text
    _enter_email = "3"
    _submit_btn = "SUBMIT"

    def openLongClickPage(self):
        start_x = 146
        start_y = 1902
        end_x = 934
        end_y = 2033
        center_x = (end_x-start_x)/2 + start_x
        center_y = (end_y-start_y)/2 + start_y
        long_press(self.driver, center_x, center_y, 6)
        cl.allureLogs("Long Clicked on Long Click Page")
    
    def verifyIsPageDisplayed(self):
        element = self.is_element_displayed(self._verify_long_click_page, "text")
        cl.allureLogs("Long Click Page verified")
        return element
