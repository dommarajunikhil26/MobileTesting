import unittest
import pytest
from pages.LongClickPage import LongClick

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestLongCLickPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def set_up_page_objects(self):
        self.lc = LongClick(self.driver)

    @pytest.mark.order(15)
    def test_openLongClickPage(self):
        self.lc.openLongClickPage()
        self.assertTrue(self.lc.verifyIsPageDisplayed(), "Long Click Action did not work")
