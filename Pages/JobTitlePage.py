from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import BaseWebElement, WebElement
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePageLocators


class JobTitleLocators:
    ADD_JOB_BTN = (By.CSS_SELECTOR, '#btnAdd')
    DELETE_JOB_BTN = (By.CSS_SELECTOR, '#btnDelete')
    OK_BTN_DIALOG_DELETE = (By.CSS_SELECTOR, '#dialogDeleteBtn')
    FIND_JOB_FILD = (By.XPATH, "//*[contains(text(), '{}')]")
    FIND_CHECKBOX = (By.XPATH, "//*[@value='{}']")
    FIND_CHECKBOX2 = (By.XPATH, "//a[contains(text(),'{}')]/../..//input")


class JobTitle:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.url_page = 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList'

    def open(self):
        self.base_page.hover_element(HomePageLocators.MENU_ADMIN_BTN)
        self.base_page.find_element(HomePageLocators.MENU_JOB_BTN).click()
        self.base_page.find_element(HomePageLocators.MENU_JOB_TITLE_BTN).click()

    def add_job(self):
        self.base_page.find_element(JobTitleLocators.ADD_JOB_BTN).click()

    def modify_job(self, work_name):
        self.find_job(work_name).click()

    def delete_job(self, work_name):
        self.find_checkbox2(work_name).click()
        self.base_page.find_element(JobTitleLocators.DELETE_JOB_BTN).click()
        self.base_page.find_element(JobTitleLocators.OK_BTN_DIALOG_DELETE).click()
        # job_description_link = self.find_job(work_name).get_attribute('href')
        # checkbox_id = job_description_link.split("=")[-1]
        # self.find_checkbox(checkbox_id).click()
        # self.find_element(JobTitleLocators.DELETE_BUTTON).click()
        # self.find_element(JobTitleLocators.DIALOG_DELETE_BUTTON).click()

    def find_job(self, work_name):
        full_locator = (JobTitleLocators.FIND_JOB_FILD[0], JobTitleLocators.FIND_JOB_FILD[1].format(work_name))
        return self.base_page.find_element(full_locator)

    # def find_checkbox(self, id):
    #     full_locator = (JobTitleLocators.FIND_CHECKBOX[0], JobTitleLocators.FIND_CHECKBOX[1].format(id))
    #     return self.base_page.find_element(full_locator)

    def find_checkbox2(self, id):
        full_locator = (JobTitleLocators.FIND_CHECKBOX2[0], JobTitleLocators.FIND_CHECKBOX2[1].format(id))
        return self.base_page.find_element(full_locator)
