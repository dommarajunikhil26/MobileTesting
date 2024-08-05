import unittest
import pytest

from pages.ScrollViewPage import ScrollViewPage

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestScrollViewPage(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def set_up_page_objects(self):
        self.svp = ScrollViewPage(self.driver)
    
    @pytest.mark.order(5)
    def test_openScrollViewPage(self):
        self.svp.openScrollViewPage()
        self.assertTrue(self.svp.verifyIfPageIsDisplayed(), "Scroll View Page did not open")
    
    @pytest.mark.order(6)
    def test_scrollToButton16(self):
        self.svp.scrollToBtn16()
        self.assertTrue(self.svp.verifyIfButton16IsDisplayed(), "Scroll action unsuccessful")
    
    @pytest.mark.order(7)
    def test_clickBtn16(self):
        self.svp.clickBtn16()
        self.assertTrue(self.svp.checkAlert(), "Button 16 click unsuccessful")
    
    @pytest.mark.order(8)
    def test_clickNo(self):
        self.svp.clickNo()
        self.assertTrue(self.svp.verifyIfButton16IsDisplayed(), "No Button click unsuccessful")
    
    @pytest.mark.order(9)
    def test_ClickYes(self):
        self.svp.clickBtn16()
        self.svp.clickYes()
        self.assertTrue(self.svp.verifyIfReturnedToHome(), "Yes button click unsuccessful")
    