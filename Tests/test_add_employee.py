import time

import pytest


@pytest.mark.parametrize('firstName, middleName, lastName, id', [('Vlad', 'Vadimovich', 'Shevchenko', '1101')])
def test_add_employee(firstName, middleName, lastName, id, dashboard_page_with_authorise, pim_page, add_employee_page,
                      employee_info_page):
    dashboard_page_with_authorise.open_PIM_page()
    pim_page.click_add_employee()
    add_employee_page.input_firstName(firstName)
    add_employee_page.input_middleName(middleName)
    add_employee_page.input_lastName(lastName)
    add_employee_page.input_id(id)
    add_employee_page.click_save_button()
    employee_info_page.click_employee_list()
    pim_page.input_id_in_search_block(id)
    pim_page.click_search_button()
    pim_page.check_employee_is_displayed(0, lastName)
    pim_page.delete_employee(0)
    pim_page.refresh()
    pim_page.input_id_in_search_block(id)
    pim_page.click_search_button()
    pim_page.check_employee_is_not_find()
