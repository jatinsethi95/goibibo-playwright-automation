import pytest
import yaml
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    config = yaml.safe_load(open("config/config.yaml"))

    with sync_playwright() as p:
        headless_mode = True if os.getenv("CI") else False

        browser = p.chromium.launch(
            headless=headless_mode,
            args=["--start-maximized"] if not headless_mode else []
        )
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(config["base_url"])

        yield page   # test runs here

        browser.close()
