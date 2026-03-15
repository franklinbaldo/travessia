from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})

        # Navigate to the local dev server
        page.goto('http://localhost:4321/travessia/carta/31-ted')

        # Take standard viewport screenshots
        page.screenshot(path='verification/screenshot_light.png')

        browser.close()

if __name__ == "__main__":
    verify_frontend()
