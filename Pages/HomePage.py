from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators:
    MENU_ADMIN_BTN = (By.CSS_SELECTOR, '#menu_admin_viewAdminModule')
    MENU_JOB_BTN = (By.CSS_SELECTOR, '#menu_admin_Job')
    MENU_JOB_TITLE_BTN = (By.CSS_SELECTOR, '#menu_admin_viewJobTitleList')
    MENU_JOB_PAY_GRADES_BTN = (By.CSS_SELECTOR, '#menu_admin_viewPayGrades')


class HomePage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.url_page = 'https://opensource-demo.orangehrmlive.com/index.php/dashboard'

    def get_url(self):
        return self.base_page.get_url()
