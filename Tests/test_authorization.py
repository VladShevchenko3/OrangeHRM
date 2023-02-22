import pytest


class TestAuthorizationPositiveCases:

    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('username, password', [('Admin', 'admin123')])
    def test_well_authorization(self, username, password, login_page, home_page):
        login_page.action_open_page()
        login_page.action_edit_text_username(username)
        login_page.action_edit_text_password(password)
        login_page.action_click_on_the_login_btn()
        home_page.assert_check_equality_current_and_base_urls()

    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('username, password, alert_error',
                             [('Admin', 'Admin123', 'Invalid credentials'),
                              ('admin123', 'Admin', 'Invalid credentials')])
    def test_error_authorization(self, username, password, alert_error, login_page):
        login_page.action_open_page()
        login_page.action_edit_text_username(username)
        login_page.action_edit_text_password(password)
        login_page.action_click_on_the_login_btn()
        login_page.assert_alert_error_is_displayed()
        login_page.assert_alert_error_has_text(alert_error)


class TestAuthorizationNegativeCases:
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('username, password', [('Admin', 'Admin123'), (' Admin', ' Admin123')])
    def test_wrong_credential(self, username, password, login_page, home_page):
        login_page.action_open_page()
        login_page.action_edit_text_username(username)
        login_page.action_edit_text_password(password)
        login_page.action_click_on_the_login_btn()
        home_page.assert_check_equality_current_and_base_urls()
