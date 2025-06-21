from playwright.sync_api import sync_playwright

def scrape_chapter(url, image_path="data/chapter1.png", text_path="data/chapter1.txt"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Screenshot
        page.screenshot(path=image_path, full_page=True)

        # Extract main content
        try:
            content = page.inner_text("div#mw-content-text")
        except:
            print("❌ Content not found")
            content = ""

        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()
        print("✅ Done scraping and screenshot saved.")
