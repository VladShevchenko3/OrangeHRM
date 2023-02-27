from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent


class LoginPageLocators(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
        self.LOCATOR_PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
        self.LOCATOR_LOGIN_BUTTON = (By.XPATH, '//button[text()=" Login "]')
        self.LOCATOR_ALERT_ERROR = (By.XPATH, '//p[text()="{}"]')
        self.LOCATOR_HEAD = (By.XPATH, '//h5[@class="oxd-text oxd-text--h5 orangehrm-login-title"]')
