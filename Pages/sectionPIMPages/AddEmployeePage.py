from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent
from Pages.sectionPIMPages.AddEmployeeLocators import AddEmployeePageLocators


class AddEmployeePage(SeleniumAgent):

    def __init__(self, driver):
        super().__init__(driver)
        self.__actions = SeleniumAgent(driver)
        self.__locators = AddEmployeePageLocators(driver)

    def input_firstName(self, firstName):
        self.__actions._input_text(self.__locators.LOCATOR_FIRST_NAME_INPUT, firstName)

    def input_middleName(self, middleName):
        self.__actions._input_text(self.__locators.LOCATOR_MIDDLE_NAME_INPUT, middleName)

    def input_lastName(self, lastName):
        self.__actions._input_text(self.__locators.LOCATOR_LAST_NAME_INPUT, lastName)

    def input_id(self, id):
        self.__actions._input_text_with_manual_data_cleaning(self.__locators.LOCATOR_ID_INPUT, id)

    def click_save_button(self):
        self.__actions._find_element_click(self.__locators.LOCATOR_SAVE_BUTTON)
