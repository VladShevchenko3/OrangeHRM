from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent


class AddEmployeePageLocators(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_FIRST_NAME_INPUT = (By.XPATH, '//input[@name="firstName"]')
        self.LOCATOR_MIDDLE_NAME_INPUT = (By.XPATH, '//input[@name="middleName"]')
        self.LOCATOR_LAST_NAME_INPUT = (By.XPATH, '//input[@name="lastName"]')
        self.LOCATOR_ID_INPUT = (By.XPATH, '//div[@class=""]//input[@class="oxd-input oxd-input--active"]')
        self.LOCATOR_SAVE_BUTTON = (By.XPATH, '//button[text()=" Save "]')
