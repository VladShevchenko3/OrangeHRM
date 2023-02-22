from Pages.BasePage import BasePage
from Pages.sectionPIMPages.NavigateMenuPIM import NavigateMenuPIM


class EmployeeInformationPage:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.navigate_menu = NavigateMenuPIM(driver)
        self.url_page = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'

    def action_click_on_employee_list(self):
        self.navigate_menu.action_click_on_employee_list()
