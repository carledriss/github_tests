from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from pages.advanced_search_page import AdvancedSearchPage
from pages.base_page import BasePage


class GitHubPage(BasePage):
    _search_input = {"by": By.CSS_SELECTOR, "value": ".header-search-input"}
    _advanced_search_link = {"by": By.CSS_SELECTOR, "value": ".d-md-block a[href*='/search/advanced']"}

    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self._visit("https://github.com")

    def search_value(self, value):
        self._type(self._search_input, value)
        self._type(self._search_input, Keys.RETURN)

    def click_advanced_search_link(self):
        self._click(self._advanced_search_link)
        return AdvancedSearchPage(self.driver)
