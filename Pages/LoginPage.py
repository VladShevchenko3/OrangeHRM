from Pages.LoginPageLocators import LoginPageLocators
from Pages.SeleniumAgent import SeleniumAgent


class LoginPage(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.__actions = SeleniumAgent(driver)
        self.__locators = LoginPageLocators(driver)

    def open_page(self):
        return self.__actions._open_base_page()

    def input_username(self, text):
        self.__actions._input_text(self.__locators.LOCATOR_USERNAME_INPUT, text)

    def input_password(self, text):
        self.__actions._input_text(self.__locators.LOCATOR_PASSWORD_INPUT, text)

    def click_login_button(self):
        self.__actions._find_element_click(self.__locators.LOCATOR_LOGIN_BUTTON)

    def check_alert_error_is_displayed(self, text):
        locator = self.__actions._format_locator(self.__locators.LOCATOR_ALERT_ERROR, text)
        self.__actions._check_element_is_displayed(locator)
