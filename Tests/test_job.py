
def test_add_job(job_title_page, add_job_page):
    job_title_page.open()
    job_title_page.add_job()
    add_job_page.enter_data("QA Lead", "important team man")
    actual_url = add_job_page.get_url()
    expected_url = job_title_page.url_page
    assert expected_url == actual_url


def test_edit_job(job_title_page, add_job_page):
    job_title_page.open()
    job_title_page.modify_job("QA Lead")
    add_job_page.edit_data("QA tester", "-")
    actual_url = add_job_page.get_url()
    expected_url = job_title_page.url_page
    assert expected_url == actual_url


def test_delete_job(job_title_page):
    job_title_page.open()
    job_title_page.delete_job('QA tester')
    assert job_title_page.find_job('QA tester') is None
