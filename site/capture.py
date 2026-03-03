from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 1024})

    # Wait a few seconds for server to start
    time.sleep(5)

    # Navigate to the specific URL
    page.goto('http://localhost:3000/travessia/carta/132-rio/')

    # Wait for content to load
    page.wait_for_selector('main', timeout=10000)

    # Scroll slightly to see content
    page.evaluate('window.scrollBy(0, 300)')

    page.screenshot(path='screenshot.png')
    print("Screenshot saved to screenshot.png")

    browser.close()
