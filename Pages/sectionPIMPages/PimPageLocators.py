from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent


class PIMPageLocators(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_ADD_EMPLOYEE_BUTTON = (
            By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.LOCATOR_ID_EMPLOYEE_INPUT = (By.XPATH, '//div[@class=""]//input[@class="oxd-input oxd-input--active"]')
        self.LOCATOR_SEARCH_BUTTON = (By.XPATH, '//button[text()=" Search "]')
        self.LOCATOR_DELETE_BUTTON = (By.XPATH, '//button[text() = " Yes, Delete "]')
        self.LOCATOR_EMPLOYEES_LIST = (By.XPATH, '//div[@class="oxd-table-body"]')
        self.LOCATOR_EMPLOYEE_LASTNAME = (By.XPATH, '//div[contains(text(), "{}")]')
        self.LOCATOR_EMPLOYEE_DELETE_BTN = (By.XPATH, '//i[@class="oxd-icon bi-trash"]')
