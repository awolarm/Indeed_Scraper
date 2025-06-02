from bs4 import BeautifulSoup
from seleniumbase import SB
# import json

# reviews_data = []

with SB(uc=True, test=True, locale="en") as sb:
    url = "https://www.indeed.com/cmp/Walmart/reviews"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    page_html = sb.get_page_source()
    soup = BeautifulSoup(page_html, 'html.parser')

    reviewList = soup.find('ul', class_='css-u74ql7 eu4oa1w0')
    
    for child in reviewList: 
        title = child.find('span', class_='css-15r9gu1 eu4oa1w0')
        description = child.find_next('span', class_='css-15r9gu1 eu4oa1w0')
        if title and description: 
            print(title)
            print(description)
            # review = {
            #     'title' : title.text.strip(),
            #     'description': description.text.strip(),
            #     'company' : 'Walmart', 
            # }
            # reviews_data.append(review)
        
# with open('reviews.json', 'w', encoding='utf-8') as f: 
#     json.dump(reviews_data, f, indent=2, ensure_ascii=False)



