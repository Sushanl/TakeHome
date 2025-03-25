from playwright.sync_api import sync_playwright

def test_booking_flow(url):
    result = {
        "demoButton" : False,
        "submitted" : False,
        "steps" : [],
        "error" : ""
    }   

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        result["steps"].append("Navigated to " + url)
        demoButton = page.query_selector("text=Book a Demo") or page.query_selector("text=Schedule a Demo") or page.query_selector("text=Schedule a Meeting")
        if demoButton:
            result["demoButton"] = True
            result["steps"].append("Demo Button exists")
            demoButton.click()
            result["steps"].append("Clicked Demo Button")
            browser.close()
            return result
        else:
            result["error"] = "No Demo Button found"
            result["sumbitted"] = False
            return result

    browser.close()
    return result   