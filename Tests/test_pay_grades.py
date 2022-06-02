import pytest


def test_add_pay_grades(pay_grades_page, edit_pay_grades):
    pay_grades_page.open()
    pay_grades_page.add_pay_grade()
    edit_pay_grades.enter_pay_grade('test')
    pay_grades_page.open()
    assert pay_grades_page.find_pay_grade('test')


def test_delete_pay_grades(pay_grades_page):
    pay_grades_page.open()
    pay_grades_page.delete_pay_grade('test')
    assert pay_grades_page.find_pay_grade('test') is None


@pytest.mark.parametrize('min_salary, max_salary', [(0, 999999999), (999999999, 999999999)])
def test_add_currency_positive(min_salary, max_salary, pay_grades_page, edit_pay_grades):
    pay_grades_page.open()
    pay_grades_page.modify_pay_grade('test')
    edit_pay_grades.enter_currency('CYP - Cyprus Pound', min_salary, max_salary)
    assert edit_pay_grades.find_currency('Cyprus Pound')
    edit_pay_grades.delete_currency('Cyprus Pound')


@pytest.mark.parametrize('min_salary, max_salary',
                         [(-1, -1), (10.5, 10.5), (1000000000, 1000000000), ('t', 't'), ('*', '*'), (' ', ' ')])
def test_add_currency_negative(min_salary, max_salary, pay_grades_page, edit_pay_grades):
    pay_grades_page.open()
    pay_grades_page.modify_pay_grade('test')
    edit_pay_grades.enter_currency('CYP - Cyprus Pound', min_salary, max_salary)
    assert edit_pay_grades.find_currency('Cyprus Pound') is None
    assert edit_pay_grades.find_head('Add Currency')


@pytest.mark.parametrize('min_salary, expected_result',
                         [(-1, 'Should be a positive number'), (10.5, 'Should be a positive number'),
                          ('t', 'Should be a positive number'), ('*', 'Should be a positive number'),
                          (' ', 'Should be a positive number'),
                          (1000000000, 'Should be less than 1000,000,000')])
def test_add_currency_error_sms_min_salary(min_salary, expected_result, pay_grades_page, edit_pay_grades):
    pay_grades_page.open()
    pay_grades_page.modify_pay_grade('test')
    edit_pay_grades.enter_currency('CYP - Cyprus Pound', min_salary, 1)
    assert edit_pay_grades.find_sms_error(expected_result)


@pytest.mark.parametrize('max_salary, expected_result',
                         [(-1, 'Should be a positive number'), (10.5, 'Should be a positive number'),
                          ('t', 'Should be a positive number'), ('*', 'Should be a positive number'),
                          (' ', 'Should be a positive number'),
                          (1000000000, 'Should be less than 1000,000,000')])
def test_add_currency_error_sms_max_salary(max_salary, expected_result, pay_grades_page, edit_pay_grades):
    pay_grades_page.open()
    pay_grades_page.modify_pay_grade('test')
    edit_pay_grades.enter_currency('CYP - Cyprus Pound', 1, max_salary)
    assert edit_pay_grades.find_sms_error(expected_result)


def test_delete_currency(pay_grades_page, edit_pay_grades):
    pay_grades_page.open()
    pay_grades_page.modify_pay_grade('test')
    assert edit_pay_grades.find_currency('Euro')
    edit_pay_grades.delete_currency('Euro')
    assert edit_pay_grades.find_currency('Euro') is None
