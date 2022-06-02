from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.HomePage import HomePageLocators


class PayGradesLocators:
    ADD_PAY_GRADE_BTN = (By.XPATH, "//input[@id='btnAdd']")
    FIND_PAY_GRADE_FILD = (By.XPATH, "//a[contains(text(), '{}')]")
    FIND_CHECKBOX = (By.XPATH, "//a[contains(text(),'{}')]/../..//input")
    DELETE_BTN = (By.XPATH, "//input[@id = 'btnDelete']")
    OK_BTN_DIALOG_DELETE = (By.XPATH, "//input[@id='dialogDeleteBtn']")


class PayGrades:

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def open(self):
        self.base_page.hover_element(HomePageLocators.MENU_ADMIN_BTN)
        self.base_page.find_element(HomePageLocators.MENU_JOB_BTN).click()
        self.base_page.find_element(HomePageLocators.MENU_JOB_PAY_GRADES_BTN).click()

    def add_pay_grade(self):
        return self.base_page.find_element(PayGradesLocators.ADD_PAY_GRADE_BTN).click()

    def modify_pay_grade(self, pay_grade_title):
        self.find_pay_grade(pay_grade_title).click()

    def delete_pay_grade(self, pay_grade_title):
        self.find_checkbox(pay_grade_title).click()
        self.base_page.find_element(PayGradesLocators.DELETE_BTN).click()
        self.base_page.find_element(PayGradesLocators.OK_BTN_DIALOG_DELETE).click()

    def find_pay_grade(self, title):
        full_locator = (
            PayGradesLocators.FIND_PAY_GRADE_FILD[0], PayGradesLocators.FIND_PAY_GRADE_FILD[1].format(title))
        return self.base_page.find_element(full_locator)

    def find_checkbox(self, title):
        full_locator = (PayGradesLocators.FIND_CHECKBOX[0], PayGradesLocators.FIND_CHECKBOX[1].format(title))
        return self.base_page.find_element(full_locator)
