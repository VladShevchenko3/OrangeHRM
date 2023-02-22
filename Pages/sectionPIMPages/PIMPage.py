from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class PIMPageLocators:
    ADD_EMPLOYEE = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    EMPLOYEE_ID = (By.XPATH, '//div[@class=""]//input[@class="oxd-input oxd-input--active"]')
    SEARCH_BTN = (
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    DELETE_BTN = (
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')
    EMPLOYEES_LIST = (By.XPATH, '//div[@class="oxd-table-body"]')


class Employee:
    LASTNAME = (By.XPATH, '//div[contains(text(), "{}")]')
    FIRST_MIDDLE_NAME = (By.XPATH, '//div[contains(text(), "{}")]')
    DELETE_BTN = (By.XPATH, '//i[@class="oxd-icon bi-trash"]')


class PIMPage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.url_page = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'

    def action_click_on_add_employee(self):
        self.base_page.action_find_element(PIMPageLocators.ADD_EMPLOYEE).click()

    def action_edit_id(self, id):
        employee_id = self.base_page.action_find_element(PIMPageLocators.EMPLOYEE_ID)
        employee_id.send_keys(id)

    def action_click_on_search_btn(self):
        self.base_page.action_find_element(PIMPageLocators.SEARCH_BTN).click()

    def action_delete_employee(self, position):
        employeeList = self.base_page.action_find_elements(PIMPageLocators.EMPLOYEES_LIST)
        employee = employeeList[position]
        employee.find_element(Employee.DELETE_BTN[0], Employee.DELETE_BTN[1]).click()
        self.base_page.action_find_element(PIMPageLocators.DELETE_BTN).click()

    def assert_employee_is_displayed(self, position, lastName, firstAndMiddle):
        employeeList = self.base_page.action_find_elements(PIMPageLocators.EMPLOYEES_LIST)
        employee = employeeList[position]
        employee.find_element(Employee.LASTNAME[0], Employee.LASTNAME[1].format(lastName)).is_displayed()
        employee.find_element(Employee.LASTNAME[0],
                              Employee.LASTNAME[1].format(firstAndMiddle)).is_displayed()

    def assert_employee_is_deleted(self):
        employeeList = self.base_page.action_find_elements(PIMPageLocators.EMPLOYEES_LIST)
        assert len(employeeList) == 0
