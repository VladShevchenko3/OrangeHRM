from Pages.BasePage import BasePage
from Pages.MainMenu import MainMenu


class DashboardPage:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_menu = MainMenu(driver)
        self.url_page = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    def action_open_PIM_page(self):
        self.main_menu.action_click_on_PIM_btn()

    def assert_check_equality_current_and_base_urls(self):
        assert self.base_page.action_get_current_url() == self.url_page
