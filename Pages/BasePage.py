from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.base_url = 'https://opensource-demo.orangehrmlive.com/'

    def find_element(self, locator) -> WebElement:
        try:
            return self.driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
           pass

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def hover_element(self, locator):
        hover = ActionChains(self.driver).move_to_element(self.find_element(locator))
        hover.perform()

    def get_url(self):
        return self.driver.current_url

    def find_head(self, locator,  head):
        full_locator = (locator[0], locator[1].format(head))
        return self.find_element(full_locator)


