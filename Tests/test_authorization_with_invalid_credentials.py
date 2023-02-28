import pytest


@pytest.mark.parametrize('username, password, alert_error',
                         [('Admin', 'Admin123', 'Invalid credentials'),
                          ('admin123', 'Admin', 'Invalid credentials')])
def test_error_authorization(username, password, alert_error, login_page):
    login_page.open_page()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()
    assert login_page.check_alert_error_is_displayed(alert_error)
