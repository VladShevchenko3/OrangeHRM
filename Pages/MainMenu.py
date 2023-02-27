from Pages.MainMenuLocators import MainMenuLocators
from Pages.SeleniumAgent import SeleniumAgent


class MainMenu(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.__actions = SeleniumAgent(driver)
        self.__locators = MainMenuLocators(driver)

    def click_on_PIM_button(self):
        self.__actions._find_element_click(self.__locators.LOCATOR_PIM_BUTTON)

    def click_on_Dashboard_btn(self):
        self.__actions._find_element_click(self.__locators.LOCATOR_DASHBOARD_BUTTON)
