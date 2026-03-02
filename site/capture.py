from playwright.sync_api import sync_playwright
import time

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:3000/travessia/carta/86-rio')
        time.sleep(5)  # Wait for page to fully load

        # Scroll to bottom to capture everything
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

        page.screenshot(path='screenshot.png', full_page=True)
        browser.close()

if __name__ == '__main__':
    take_screenshot()