from bs4 import BeautifulSoup
from seleniumbase import SB

with SB(uc=True, test=True, locale="en") as sb:
    url = "https://www.indeed.com/cmp/Walmart/reviews"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    page_html = sb.get_page_source()
    soup = BeautifulSoup(page_html, 'html.parser')

    titles = soup.find_all('span', class_='css-15r9gu1 eu4oa1w0')

    for title in titles:
        print(title.text)

# booyyaaaaa
