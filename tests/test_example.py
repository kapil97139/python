from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        print(page.title())  # This will print the title of the page
        browser.close()

if __name__ == "__main__":
    test_example()
