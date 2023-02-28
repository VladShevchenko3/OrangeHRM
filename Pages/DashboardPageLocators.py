from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent


class DashboardPageLocators(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_HEAD = (By.XPATH, '//h6[text()="Dashboard"]')
