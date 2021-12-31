from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.repository_page import RepositoryPage


class AdvancedSearchPage(BasePage):

    _written_in_this_language = {"by": By.ID, "value": "search_language"}
    _in_the_state = {"by": By.ID, "value": "search_state"}
    _with_this_many_stars = {"by": By.ID, "value": "search_stars"}
    _with_this_many_followers = {"by": By.ID, "value": "search_followers"}
    _with_this_license = {"by": By.ID, "value": "search_license"}
    _search_button = {"by": By.CSS_SELECTOR, "value": "#adv_code_search button"}
    _search_result_title = {"by": By.CSS_SELECTOR, "value": ".codesearch-results .flex-column > h3"}

    def __init__(self, driver):
        self.driver = driver

    def select_written_in_this_language(self, text):
        self._select(self._written_in_this_language, text)

    def select_in_the_state(self, text):
        self._select(self._in_the_state, text)

    def set_with_this_many_stars_input(self, value):
        self._type(self._with_this_many_stars, value)

    def set_with_this_many_followers_input(self, value):
        self._type(self._with_this_many_followers, value)

    def select_with_this_license(self, text):
        self._select(self._with_this_license, text)

    def click_search_button(self):
        self._click(self._search_button)

    def get_search_result_title(self):
        return self._get_text(self._search_result_title)

    def is_repo_present(self, repo_name):
        _repo_link = {"by": By.CSS_SELECTOR, "value": ".repo-list a[data-hydro-click][href='/" + repo_name + "']"}
        return self._is_displayed(_repo_link, 1)

    def click_repo_link(self, repo_name):
        _repo_link = {"by": By.CSS_SELECTOR, "value": ".repo-list a[data-hydro-click][href='/" + repo_name + "']"}
        self._click(_repo_link)
        return RepositoryPage(self.driver)

