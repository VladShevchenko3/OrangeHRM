from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.base_url = 'https://opensource-demo.orangehrmlive.com/'

    def action_find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((locator[0], locator[1]))
        )

    def action_find_elements(self, locator) -> list[WebElement]:
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((locator[0], locator[1]))
        )

    def action_open_page(self):
        return self.driver.get(self.base_url)

    def action_get_current_url(self):
        return self.driver.current_url
