from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class NavigateMenuLocators:
    EMPLOYEE_LIST = (By.XPATH, '//nav[@class="oxd-topbar-body-nav"]//a[text()="Employee List"]')


class NavigateMenuPIM:

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def action_click_on_employee_list(self):
        self.base_page.action_find_element(NavigateMenuLocators.EMPLOYEE_LIST).click()
