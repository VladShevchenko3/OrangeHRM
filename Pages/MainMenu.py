from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class MainManuLocators:
    PIM_BTN = (By.XPATH, '//ul[@class="oxd-main-menu"]//span[text()="PIM"]')
    DASHBOARD_BTN = (By.XPATH, '//ul[@class="oxd-main-menu"]//span[text()="Dashboard"]')


class MainMenu:
    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def action_click_on_PIM_btn(self):
        self.base_page.action_find_element(MainManuLocators.PIM_BTN).click()

    def action_click_on_Dashboard_btn(self):
        self.base_page.action_find_element(MainManuLocators.DASHBOARD_BTN).click()
