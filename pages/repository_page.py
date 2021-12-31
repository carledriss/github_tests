from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RepositoryPage(BasePage):

    _raw_button = {"by": By.CSS_SELECTOR, "value": "#raw-url"}
    _raw_text = {"by": By.CSS_SELECTOR, "value": "pre[style]"}

    def __init__(self, driver):
        self.driver = driver

    def click_file_link(self, file_name):
        _file_link = {"by": By.CSS_SELECTOR, "value": "a[title='" + file_name + "']"}
        self._click(_file_link)

    def click_raw_button(self):
        assert self._is_displayed(self._raw_button, 1)
        self._click(self._raw_button)

    def print_characters(self, num_characters):
        assert self._is_displayed(self._raw_text, 1)
        raw_text = self._get_text(self._raw_text)
        print(raw_text[0:num_characters])
