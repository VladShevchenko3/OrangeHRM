from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AddEmployeeLocators:
    FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    MIDDLE_NAME = (By.XPATH, '//input[@name="middleName"]')
    LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    ID = (By.XPATH, '//div[@class=""]//input[@class="oxd-input oxd-input--active"]')
    SAVE_BTN = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')


class AddEmployeePage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.url_page = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'

    def action_edit_firstName(self, firstName_text):
        firstName = self.base_page.action_find_element(AddEmployeeLocators.FIRST_NAME)
        firstName.clear()
        firstName.send_keys(firstName_text)

    def action_edit_middleName(self, firstName_text):
        middleName = self.base_page.action_find_element(AddEmployeeLocators.MIDDLE_NAME)
        middleName.clear()
        middleName.send_keys(firstName_text)

    def action_edit_lastName(self, firstName_text):
        lastName = self.base_page.action_find_element(AddEmployeeLocators.LAST_NAME)
        lastName.clear()
        lastName.send_keys(firstName_text)

    def action_edit_id(self, id):
        employee_id = self.base_page.action_find_element(AddEmployeeLocators.ID)
        employee_id.send_keys(Keys.CONTROL + "a")
        employee_id.send_keys(Keys.DELETE)
        employee_id.send_keys(id)

    def action_click_on_save_btn(self):
        self.base_page.action_find_element(AddEmployeeLocators.SAVE_BTN).click()
