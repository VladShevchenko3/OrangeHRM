from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    HEAD_PAGE = (By.XPATH, "//h1[contains(text(), '{}')]")
    USERNAME_FIELD_INPUT = (By.CSS_SELECTOR, '#txtUsername')
    PASSWORD_FIELD_INPUT = (By.CSS_SELECTOR, '#txtPassword')
    LOGIN_BTN = (By.CSS_SELECTOR, '#btnLogin')
    SMS_ERROR = (By.CSS_SELECTOR, '#spanMessage')

class LoginPage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def authorization(self, username, password):
        self.base_page.enter_text(LoginPageLocators.USERNAME_FIELD_INPUT, username)
        self.base_page.enter_text(LoginPageLocators.PASSWORD_FIELD_INPUT, password)
        self.base_page.find_element(LoginPageLocators.LOGIN_BTN).click()

    def go_to_site(self):
        return self.base_page.go_to_site()

    def get_url(self):
        return self.base_page.get_url()

    def find_head(self, head):
        return self.base_page.find_head(LoginPageLocators.HEAD_PAGE, head)

    def find_sms_error(self):
        return self.base_page.find_element(LoginPageLocators.SMS_ERROR)

