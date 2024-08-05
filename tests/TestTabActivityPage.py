

import unittest

import pytest

from pages.TabActivityPage import TabActivity

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestTabActivityPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def set_up_page_objects(self):
        self.ta = TabActivity(self.driver)
    
    @pytest.mark.order(10)
    def test_openTabActivityPage(self):
        self.ta.openTabActivityPage()
        self.assertTrue(self.ta.verifyIfTabPageDisplayed(), "Tab Activity Page is not displayed")

    @pytest.mark.order(11)
    def test_swipeRightFromHome(self):
        self.ta.swipeRight()
        self.assertTrue(self.ta.verifySportsFragment(), "Swipe Right from Home Fragment is unsuccessful")
    
    @pytest.mark.order(12)
    def test_swipeRightFromSports(self):
        self.ta.swipeRight()
        self.assertTrue(self.ta.verifyMovieFragment(), "Swipe Right from Sports Fragment is unsuccessful")
    
    @pytest.mark.order(13)
    def test_swipeLeftFromMovie(self):
        self.ta.swipeLeft()
        self.assertTrue(self.ta.verifySportsFragment(), "Swipe Left from Movie Fragment is unsuccessful")
    
    @pytest.mark.order(14)
    def test_swipeLeftFromSports(self):
        self.ta.swipeLeft()
        self.assertTrue(self.ta.verifyHomeFragment(), "Swipe Left from Sports Fragment is unsuccessful")