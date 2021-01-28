from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "hebei")

    # Press Enter
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=hebei&fenlei=256&rsv_pq=c50817ec00043dd2&rsv_t=4ddazcUJo09Kpc0kD1hffifY6xjEBPiETe0zAp/yJc4cyMd4CPAPz2tKKus&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1194&rsv_sug4=1194"):
    with page.expect_navigation():
        page.press("input[name=\"wd\"]", "Enter")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
