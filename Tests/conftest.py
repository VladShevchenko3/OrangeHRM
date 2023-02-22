import os

import pytest
from selenium import webdriver

from Pages.sectionPIMPages.AddEmployeePage import AddEmployeePage
from Pages.BasePage import BasePage
from Pages.sectionPIMPages.EmployeeInformationPage import EmployeeInformationPage
from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage
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
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def authorise(login_page):
    login_page.action_open_page()
    login_page.action_edit_text_username("Admin")
    login_page.action_edit_text_password("admin123")
    login_page.action_click_on_the_login_btn()


@pytest.fixture(scope="function")
def home_page_with_authorise(authorise, driver):
    return DashboardPage(driver)


@pytest.fixture(scope="function")
def home_page(driver):
    return DashboardPage(driver)


@pytest.fixture(scope="function")
def pim_page(driver):
    return PIMPage(driver)


@pytest.fixture(scope="function")
def add_employee_page(driver):
    return AddEmployeePage(driver)


@pytest.fixture(scope="function")
def employee_information_page(driver):
    return EmployeeInformationPage(driver)
