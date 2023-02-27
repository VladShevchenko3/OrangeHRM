from selenium.webdriver.common.by import By

from Pages.SeleniumAgent import SeleniumAgent
from Pages.sectionPIMPages.PimPageLocators import PIMPageLocators


class PIMPage(SeleniumAgent):

    def __init__(self, driver):
        super().__init__(driver)
        self.__actions = SeleniumAgent(driver)
        self.__locators = PIMPageLocators(driver)

    def click_add_employee(self):
        self.__actions._find_element_click(self.__locators.LOCATOR_ADD_EMPLOYEE_BUTTON)

    def input_id_in_search_block(self, id):
        self.__actions._input_text(self.__locators.LOCATOR_ID_EMPLOYEE_INPUT, id)

    def click_search_button(self):
        self.__actions._find_element_click(self.__locators.LOCATOR_SEARCH_BUTTON)

    def delete_employee(self, position):
        self.__actions._click_ob_element_in_list_with_position(self.__locators.LOCATOR_EMPLOYEES_LIST,
                                                               position,
                                                               self.__locators.LOCATOR_EMPLOYEE_DELETE_BTN)
        self.__actions._find_element_click(self.__locators.LOCATOR_DELETE_BUTTON)

    def refresh_page(self):
        self.__actions.refresh()

    def check_employee_is_displayed(self, position, lastName):
        locator = self.__actions._format_locator(self.__locators.LOCATOR_EMPLOYEE_LASTNAME, lastName)
        assert self.__actions._check_element_in_list_with_position_is_displayed(self.__locators.LOCATOR_EMPLOYEES_LIST,
                                                                                position, locator)

    def check_employee_is_not_find(self):
        employee_list = self.__actions._get_list(self.__locators.LOCATOR_EMPLOYEES_LIST)
        assert len(employee_list) == 1 and employee_list[0].text == ''
