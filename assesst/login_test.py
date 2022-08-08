import pytest
from selenium import webdriver
from Home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):
    baseURL = "https://github.com/login"
    driver = webdriver.chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("roopashree1307@gmail.com", "Roopashree@123456789")
        result= self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

