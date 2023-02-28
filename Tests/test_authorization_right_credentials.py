import pytest


@pytest.mark.parametrize('username, password', [('Admin', 'admin123')])
def test_well_authorization(username, password, login_page, dashboard_page):
    login_page.open_page()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()
    dashboard_page.check_the_head_is_displayed()
