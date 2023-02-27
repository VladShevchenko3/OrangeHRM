from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent


class NavigateMenuLocators(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_EMPLOYEE_LIST = (By.XPATH, '//nav[@class="oxd-topbar-body-nav"]//a[text()="Employee List"]')
