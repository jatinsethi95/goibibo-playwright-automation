from pages.home_page import HomePage
from test_base.base import page

def test_flight_search(page):

        home = HomePage(page)
        home.verify_and_close_login_container()
        home.enter_from_city("Delhi")
        home.enter_to_city("Mumbai")
        home.select_departure_date(0)
        home.click_search()

        page.wait_for_timeout(5000)
        assert "flight" in page.url.lower()
