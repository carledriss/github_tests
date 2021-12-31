import pytest

from pages.github_page import GitHubPage


@pytest.fixture
def github(request):
    github_page = GitHubPage()

    def quit():
        github_page.driver.quit()

    request.addfinalizer(quit)
    return github_page


def test_github_search(github):
    github.search_value("react")
    advanced_search = github.click_advanced_search_link()
    advanced_search.select_written_in_this_language("JavaScript")
    advanced_search.select_in_the_state("closed")
    advanced_search.set_with_this_many_stars_input(">45")
    advanced_search.set_with_this_many_followers_input(">50")
    advanced_search.select_with_this_license("Boost Software License 1.0")
    advanced_search.click_search_button()
    assert advanced_search.get_search_result_title() == "1 repository result"
    assert advanced_search.is_repo_present("mvoloskov/decider")
    repository = advanced_search.click_repo_link("mvoloskov/decider")
    repository.click_file_link("README.md")
    repository.click_raw_button()
    repository.print_characters(300)
