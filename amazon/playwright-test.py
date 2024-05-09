from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser_type=p.chromium
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.amazon.com/Jewelili-Enchanted-Sterling-Gemstones-Majestic/dp/B0CW77Z1CM/ref=sr_1_3?dib=eyJ2IjoiMSJ9.MAQoA5voQ2UaXcLrwTO4ixe6fzcrNjPAd8bWIMDbpyCUVcxHqxQAMXR5C5sFQ3KXLcW6utVp4ndqy3-oDlAkAg.yywRJdStzv2wYqv3AeF4P53Et7s07LY_LrSB9DEAUBw&dib_tag=se&keywords=100th+anniversary&qid=1715139844&refinements=p_n_date_first_available_absolute%3A15196853011&s=apparel&sr=1-3')
    page.screenshot(path=f'screenshot-{browser_type.name}.png')
    print(page.title())
