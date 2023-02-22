import pytest


@pytest.mark.parametrize('firstName, middleName, lastName, id', [('Vlad', 'Vadimovich', 'Shevchenko', '1001')])
def test_add_employee(firstName, middleName, lastName, id, home_page_with_authorise, pim_page, add_employee_page,
                      employee_info_page):
    home_page_with_authorise.action_open_PIM_page()
    pim_page.action_click_on_add_employee()
    add_employee_page.action_edit_firstName(firstName)
    add_employee_page.action_edit_middleName(middleName)
    add_employee_page.action_edit_lastName(lastName)
    add_employee_page.action_edit_id(id)
    add_employee_page.action_click_on_save_btn()
    employee_info_page.action_click_on_employee_list()
    pim_page.action_edit_id(id)
    pim_page.action_click_on_search_btn()
    pim_page.assert_employee_is_displayed(0, lastName, f'{firstName} {middleName}')
    pim_page.action_delete_employee(0)
    pim_page.assert_employee_is_deleted()
