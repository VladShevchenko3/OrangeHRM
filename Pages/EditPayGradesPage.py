from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class EditPayGradesLocators:
    HEAD_PAGE = (By.XPATH, "//h1[contains(text(), '{}')]")
    PAY_GRADES_TITLE_FIELD_INPUT = (By.XPATH, "//input[@id='payGrade_name']")
    ADD_PAY_GRADES_SAVE_BTN = (By.XPATH, "//input[@id='btnSave']")
    ADD_CURRENCY_BTN = (By.XPATH, "//input[@id ='btnAddCurrency']")
    CURRENCY_NAME_FIELD_INPUT = (By.XPATH, "//input[@id ='payGradeCurrency_currencyName']")
    CURRENCY_MIN_SALARY_FIELD_INPUT = (By.XPATH, "//input[@id='payGradeCurrency_minSalary']")
    CURRENCY_MAX_SALARY_FIELD_INPUT = (By.XPATH, "//input[@id='payGradeCurrency_maxSalary']")
    CURRENCY_SAVE_BTN = (By.XPATH, "//input[@id='btnSaveCurrency']")
    CURRENCY_DELETE_BTN = (By.CSS_SELECTOR, '#btnDeleteCurrency')
    FIND_CURRENCY_FIELD = (By.XPATH, "//a[contains(text(), '{}')]")
    FIND_SMS_ERROR = (By.XPATH, "//span[contains(text(),'{}')]")
    FIND_CHECKBOX = (By.XPATH, "//a[contains(text(),'{}')]/../..//input")


class EditPayGrades:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)

    def enter_pay_grade(self, title):
        self.base_page.enter_text(EditPayGradesLocators.PAY_GRADES_TITLE_FIELD_INPUT, title)
        self.base_page.find_element(EditPayGradesLocators.ADD_PAY_GRADES_SAVE_BTN).click()

    def enter_currency(self, title, min_salary, max_salary):
        self.base_page.find_element(EditPayGradesLocators.ADD_CURRENCY_BTN).click()
        self.base_page.enter_text(EditPayGradesLocators.CURRENCY_NAME_FIELD_INPUT, title)
        self.base_page.enter_text(EditPayGradesLocators.CURRENCY_MIN_SALARY_FIELD_INPUT, min_salary)
        self.base_page.enter_text(EditPayGradesLocators.CURRENCY_MAX_SALARY_FIELD_INPUT, max_salary)
        self.base_page.find_element(EditPayGradesLocators.CURRENCY_SAVE_BTN).click()

    def delete_currency(self, title_currency):
        self.find_checkbox(title_currency).click()
        self.base_page.find_element(EditPayGradesLocators.CURRENCY_DELETE_BTN).click()

    def find_currency(self, title):
        full_locator = (
            EditPayGradesLocators.FIND_CURRENCY_FIELD[0], EditPayGradesLocators.FIND_CURRENCY_FIELD[1].format(title))
        return self.base_page.find_element(full_locator)

    def find_head(self, head):
        return self.base_page.find_head(EditPayGradesLocators.HEAD_PAGE, head)

    def find_sms_error(self, message):
        full_locator = (
            EditPayGradesLocators.FIND_SMS_ERROR[0], EditPayGradesLocators.FIND_SMS_ERROR[1].format(message))
        return self.base_page.find_element(full_locator)

    def find_checkbox(self, title):
        full_locator = (EditPayGradesLocators.FIND_CHECKBOX[0], EditPayGradesLocators.FIND_CHECKBOX[1].format(title))
        return self.base_page.find_element(full_locator)
