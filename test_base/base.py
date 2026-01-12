import pytest
import yaml
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    config = yaml.safe_load(open("config/config.yaml"))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(config["base_url"])

        yield page   # test runs here

        browser.close()
