from datetime import datetime, timedelta

class WebActions:

    @staticmethod
    def get_future_date(days):
        future = datetime.today() + timedelta(days=days)
        return future.strftime("%a %b %d %Y")

    @staticmethod
    def select_future_date(page, days):
        date = WebActions.get_future_date(days)
        xpath = f"//div[contains(@class,'DayPicker-Day') and @aria-label='{date}']"

        while True:
            if page.locator(xpath).count() > 0:
                page.click(xpath)
                break

