from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent


class MainMenuLocators(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_PIM_BUTTON = (By.XPATH, '//ul[@class="oxd-main-menu"]//span[text()="PIM"]')
        self.LOCATOR_DASHBOARD_BUTTON = (By.XPATH, '//ul[@class="oxd-main-menu"]//span[text()="Dashboard"]')
