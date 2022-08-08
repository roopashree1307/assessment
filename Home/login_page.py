from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    _login_link ="Sign in"
    _email_field = "login_field"
    _password_field = "password"
    _login_button = "commit"

    def getloginlink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getemailfield(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getpasswordfield(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getloginbutton(self):
        return self.driver.find_element(By.NAME, self._login_button)

    def clickloginlink(self):
        self.getloginlink().click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self._login_link)).click()

    def enteremailfield(self, email):
        self.getemailfield().send_keys(email)

    def enterpasswordfield(self, password):
        self.getpasswordfield().send_keys(password)

    def clickloginbutton(self):
        self.getloginbutton().click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self._login_button)).click()

    def login(self, email, password):
        self.clickloginlink()
        self.enteremailfield(email)
        self.enterpasswordfield(password)
        self.clickloginbutton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locator="//div/h1[contains(text(),'The home for all developers — including you.')]",locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='px-2']",locatorType="xpath")
        return result