from Pages.DashboardPageLocators import DashboardPageLocators
from Pages.MainMenu import MainMenu
from Pages.SeleniumAgent import SeleniumAgent


class DashboardPage(SeleniumAgent):

    def __init__(self, driver):
        super().__init__(driver)
        self.__main_menu = MainMenu(driver)
        self.__actions = SeleniumAgent(driver)
        self.__locators = DashboardPageLocators(driver)

    def open_PIM_page(self):
        self.__main_menu.click_on_PIM_button()
