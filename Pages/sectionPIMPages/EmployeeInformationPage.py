from Pages.SeleniumAgent import SeleniumAgent
from Pages.sectionPIMPages.NavigateMenuLocators import NavigateMenuLocators


class EmployeeInformationPage(SeleniumAgent):
    def __init__(self, driver):
        super().__init__(driver)
        self.__actions = SeleniumAgent(driver)
        self.__locator_nav_menu = NavigateMenuLocators(driver)

    def click_employee_list(self):
        self.__actions._find_element_click(self.__locator_nav_menu.LOCATOR_EMPLOYEE_LIST)
