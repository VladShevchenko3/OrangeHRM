import pytest


@pytest.mark.parametrize('username, password', [('Admin', 'admin123')])
def test_authorization_positive(username, password, login_page):
    login_page.go_to_site()
    login_page.authorization(username, password)
    # expected_url = home_page.get_url()
    # actual_url = login_page.get_url()
    # assert expected_url == actual_url
    assert login_page.find_head('Dashboard')


@pytest.mark.parametrize('username, password', [('Admin', 'Admin123'), ('admin123', 'Admin')])
def test_authorization_positive(username, password, login_page):
    login_page.go_to_site()
    login_page.authorization(username, password)
    # expected_url = home_page.get_url()
    # actual_url = login_page.get_url()
    # assert expected_url == actual_url
    assert login_page.find_head('Dashboard') is None
    assert login_page.find_sms_error()
