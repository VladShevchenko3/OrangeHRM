from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumAgent:
    def __init__(self, driver):
        self.__element: WebElement
        self.__elements: WebElement
        self.__driver: WebDriver = driver
        self.__base_url = 'https://opensource-demo.orangehrmlive.com/'

    def _open_base_page(self):
        self.__driver.get(self.__base_url)

    def _find_element_click(self, locator, wait_time=3):
        WebDriverWait(self.__driver, wait_time).until(
            EC.visibility_of_element_located((locator[0], locator[1])))
        self.__element = self.__driver.find_element(locator[0], locator[1])
        self.__element.click()

    def _find_element(self, locator, wait_time=3):
        WebDriverWait(self.__driver, wait_time).until(
            EC.visibility_of_element_located((locator[0], locator[1])))
        self.__element = self.__driver.find_element(locator[0], locator[1])

    def _find_elements(self, locator, wait_time=5):
        WebDriverWait(self.__driver, wait_time).until(
            EC.visibility_of_element_located((locator[0], locator[1])))
        self.__elements = self.__driver.find_elements(locator[0], locator[1])

    def _format_locator(self, locator, value) -> tuple[str, str]:
        return locator[0], locator[1].format(value)

    def _input_text(self, locator, text):
        self._find_element(locator)
        self.__element.clear()
        self.__element.send_keys(text)

    def _input_text_with_manual_data_cleaning(self, locator, text):
        self._find_element(locator)
        self.__element.send_keys(Keys.CONTROL + "a")
        self.__element.send_keys(Keys.DELETE)
        self.__element.send_keys(text)

    def _check_element_is_displayed(self, locator):
        self._find_element(locator)
        return self.__element.is_displayed()

    def _check_element_in_list_with_position_is_displayed(self, locator_list, position, locator_element):
        self._find_elements(locator_list)
        list_item = self.__elements[position]
        self.__element = list_item.find_element(locator_element[0], locator_element[1])
        return self.__element.is_displayed()

    def _click_ob_element_in_list_with_position(self, locator_list, position, locator_element):
        self._find_elements(locator_list)
        list_item = self.__elements[position]
        self.__element = list_item.find_element(locator_element[0], locator_element[1])
        self.__element.click()

    def refresh(self):
        self.__driver.refresh()

    def _get_list(self, locator_list):
        self._find_elements(locator_list)
        return self.__elements
