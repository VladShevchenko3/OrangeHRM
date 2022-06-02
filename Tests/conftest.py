import os

import pytest
from selenium import webdriver

from Pages.AddJobTitlePage import AddJobPage
from Pages.EditPayGradesPage import EditPayGrades
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.JobTitlePage import JobTitle
from Pages.LoginPage import LoginPage
from Pages.PayGradesPage import PayGrades


@pytest.fixture(scope="function")
def driver():
    dir_project_path = os.getcwd()
    driver_path = os.path.join(dir_project_path, 'chromedriver.exe')
    driver = webdriver.Chrome(driver_path)
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
    login_page.go_to_site()
    login_page.authorization('Admin', 'admin123')


@pytest.fixture(scope="function")
def home_page(authorise, driver):
    return HomePage(driver)


@pytest.fixture(scope="function")
def job_title_page(authorise, driver):
    return JobTitle(driver)


@pytest.fixture(scope="function")
def add_job_page(driver):
    return AddJobPage(driver)


@pytest.fixture(scope="function")
def pay_grades_page(home_page, driver):
    return PayGrades(driver)


@pytest.fixture(scope="function")
def edit_pay_grades(driver):
    return EditPayGrades(driver)
