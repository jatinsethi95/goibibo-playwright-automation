from locators.home_locators import HomeLocators
from utils.web_actions import WebActions

class HomePage:

    def __init__(self, page):
        self.page = page

    def verify_and_close_login_container(self):
        self.page.click(HomeLocators.CLOSE_BUTTON)
        self.page.click(HomeLocators.CLOSE_POPUP)

    def enter_from_city(self, city):
        self.page.click(HomeLocators.FROM_LABEL)
        self.page.fill(HomeLocators.FROM_INPUT, city)
        self.page.click(HomeLocators.FROM_CITY)

    def enter_to_city(self, city):
        self.page.click(HomeLocators.TO_LABEL)
        self.page.click(HomeLocators.TO_INPUT)
        self.page.fill(HomeLocators.TO_INPUT, city)
        self.page.click(HomeLocators.TO_CITY)

    def select_departure_date(self, days):
        WebActions.select_future_date(self.page, days)

    def click_search(self):
        self.page.click(HomeLocators.SEARCH_BUTTON)
