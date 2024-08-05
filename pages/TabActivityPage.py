from pages.BasePage import BasePage
import utils.CustomLogger as cl
from utils.Gestures import swipe

class TabActivity(BasePage):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _open_tab_activity_page = "com.code2lead.kwad:id/TabView"   #id
    _verify_is_tab_page_displayed = "Tab View"  #text
    _home_fragment="HomeFragment"
    _sport_fragment="SportFragment"
    _movie_fragment="MovieFragment"

    def openTabActivityPage(self):
        self.click_element(self._open_tab_activity_page, "id")
        self.log.info("Clicked on Tab Activity Page")
    
    def verifyIfTabPageDisplayed(self):
        element = self.is_element_displayed(self._verify_is_tab_page_displayed, "text")
        self.log.info("Verified Tab Page")
        return element
    
    def verifyHomeFragment(self):
        element = self.is_element_displayed(self._home_fragment, "text")
        self.log.info("Home Fragment verified")
        return element
    
    def verifySportsFragment(self):
        element = self.is_element_displayed(self._sport_fragment, "text")
        self.log.info("Sports Fragment verified")
        return element

    def verifyMovieFragment(self):
        element = self.is_element_displayed(self._movie_fragment, "text")
        self.log.info("Movie Fragment verified")
        return element
    
    # 950 1300 200 1300
    def swipeRight(self):
        swipe(self.driver, 950, 1300, 200, 1300)
    
    def swipeLeft(self):
        swipe(self.driver, 200, 1300, 950, 1300)