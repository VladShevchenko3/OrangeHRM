from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AddJobPageLocators:
    JOB_TITLE_FIELD_INPUT = (By.CSS_SELECTOR, '#jobTitle_jobTitle')
    JOB_DESCRIPTION_FIELD_INPUT = (By.CSS_SELECTOR, '#jobTitle_jobDescription')
    SAVE_BTN = (By.CSS_SELECTOR, '#btnSave')


class AddJobPage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def enter_data(self, title, description):
        self.base_page.enter_text(AddJobPageLocators.JOB_TITLE_FIELD_INPUT, title)
        self.base_page.enter_text(AddJobPageLocators.JOB_DESCRIPTION_FIELD_INPUT, description)
        self.base_page.find_element(AddJobPageLocators.SAVE_BTN).click()

    def edit_data(self, title, description):
        self.base_page.find_element(AddJobPageLocators.SAVE_BTN).click()
        self.base_page.enter_text(AddJobPageLocators.JOB_TITLE_FIELD_INPUT, title)
        self.base_page.enter_text(AddJobPageLocators.JOB_DESCRIPTION_FIELD_INPUT, description)
        self.base_page.find_element(AddJobPageLocators.SAVE_BTN).click()

    def get_url(self):
        return self.base_page.get_url()
