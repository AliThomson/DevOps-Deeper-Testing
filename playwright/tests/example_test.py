import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_code_gen(page: Page) -> None:

    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Generate some code")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Check it disappears when done")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.locator("body")).to_contain_text("Check it disappears when done")
    expect(page.locator("body")).to_contain_text("Generate some code")
    page.locator("li").filter(has_text="Check it disappears when done").get_by_label("Toggle Todo").check()
    page.get_by_role("button", name="Clear completed").click()
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("Generate some code")
    # expect(page.get_by_test_id("todo-title")).not.to_contain_text("The one that disappeared")
