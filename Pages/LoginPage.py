from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BTN = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
    ALERT_ERROR = (By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')


class LoginPage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def action_edit_text_username(self, text_username):
        username = self.base_page.action_find_element(LoginPageLocators.USERNAME)
        username.clear()
        username.send_keys(text_username)

    def action_edit_text_password(self, text_password):
        password = self.base_page.action_find_element(LoginPageLocators.PASSWORD)
        password.clear()
        password.send_keys(text_password)

    def action_click_on_the_login_btn(self):
        self.base_page.action_find_element(LoginPageLocators.LOGIN_BTN).click()

    def action_open_page(self):
        return self.base_page.action_open_page()

    def action_get_url(self):
        return self.base_page.action_get_current_url()

    def assert_alert_error_is_displayed(self):
        alert_error = self.base_page.action_find_element(LoginPageLocators.ALERT_ERROR)
        assert alert_error.is_displayed() is True, "Alert error is not displayed"

    def assert_alert_error_has_text(self, text):
        alert_error = self.base_page.action_find_element(LoginPageLocators.ALERT_ERROR)
        assert alert_error.text == text
