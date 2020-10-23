from pages.home.login_page import LoginPage
from utilities.trackstatus import TrackStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

# Use oneTimeSetUp and setUp from conftest
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    # classSetup creates the Login Page object.  This method is different than the conftest setUp method
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TrackStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("nguyenbinhit@yahoo.com", "1234576")
        #result1 = self.lp.verifyLoginTitle()
        #self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=2)
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/AP/testdata2.csv"))
    @unpack
    def test_invalidLogin(self, email, password):
        self.lp.logout()
        self.lp.login(email, password)
        result = self.lp.verifyLoginFailed()
        assert result == True