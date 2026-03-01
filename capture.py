from playwright.sync_api import sync_playwright
import time

def capture_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        time.sleep(5)  # Wait for the server to start
        page.goto('http://localhost:3000')
        page.screenshot(path='screenshot.png')
        browser.close()

if __name__ == '__main__':
    capture_screenshot()
