import os

import pytest
from selenium import webdriver

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage
from Pages.sectionPIMPages.AddEmployeePage import AddEmployeePage
from Pages.sectionPIMPages.EmployeeInformationPage import EmployeeInformationPage
from Pages.sectionPIMPages.PIMPage import PIMPage


@pytest.fixture(scope="function")
def driver():
    dir_project_path = os.getcwd()
    driver_path = os.path.join(dir_project_path, 'chromedriver.exe')
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def authorise(login_page):
    login_page.open_page()
    login_page.input_username("Admin")
    login_page.input_password("admin123")
    login_page.click_login_button()


@pytest.fixture(scope="function")
def dashboard_page_with_authorise(authorise, driver):
    return DashboardPage(driver)


@pytest.fixture(scope="function")
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture(scope="function")
def pim_page(driver):
    return PIMPage(driver)


@pytest.fixture(scope="function")
def add_employee_page(driver):
    return AddEmployeePage(driver)


@pytest.fixture(scope="function")
def employee_info_page(driver):
    return EmployeeInformationPage(driver)
