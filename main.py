import os
import requests
from bs4 import BeautifulSoup
import lxml

# For Amazon Scrapping
MY_HEADER_USER_AGENT = os.environ.get("MY_HEADER_USER_AGENT")
MY_HEADER_ACCEPT_LANGUAGE = os.environ.get("MY_HEADER_ACCEPT_LANGUAGE")
# For Email
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

amazon_headers = {
    "User-Agent": MY_HEADER_USER_AGENT,
    "Accept-Language": MY_HEADER_ACCEPT_LANGUAGE
}

"""
E.g. :
Amazon product - Full set for gaming
----------------
Gaming Keyboard and Mouse and Mouse pad and Gaming Headset, Wired LED RGB Backlight Bundle for 
PC Gamers and Xbox and PS4 Users - 4 in 1 Edition Hornet RX-250
"""
URL_PRODUCT = ("https://www.amazon.com/Gaming-Keyboard-Headset-Backlight-Bundle/dp/B07TVK8WJP/"
               "ref=sxin_14_pa_sp_search_thematic_sspa?_encoding=UTF8&"
               "content-id=amzn1.sym.9877e0e3-4e2c-4fe3-bc39-5d1afac8a97a%3Aamzn1.sym.9877e0e3-4e2c-4fe3-bc39-"
               "5d1afac8a97a&cv_ct_cx=gaming%2Bkeyboard&keywords=gaming%2Bkeyboard&pd_rd_i=B07TVK8WJP&"
               "pd_rd_r=2a4977e7-be38-403e-9f94-b1bd3ac4b3a4&pd_rd_w=9LRJ5&pd_rd_wg=GKXYR&"
               "pf_rd_p=9877e0e3-4e2c-4fe3-bc39-5d1afac8a97a&pf_rd_r=PR60RR95HXB99CJMQN39&qid=1707133278&"
               "sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-1-2c727eeb-987f-452f-86bd-c2978cc9d8b9-spons&"
               "sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1")

# Desired price that the chosen product must have (or smaller than it)
target_price = 50

response = requests.get(url=URL_PRODUCT, headers=amazon_headers, timeout=120)
amazon_product_html = response.text

soup = BeautifulSoup(amazon_product_html, "lxml")

whole_price_content_tag = soup.find(name="div", class_="a-section a-spacing-none aok-align-center aok-relative")

whole_price_content = soup.find(name="span", class_="aok-offscreen").getText().strip()
# We need to take only the price with symbol, because content can look like this: "$49.91 with 9 percent savings"
price_with_symbol = whole_price_content.split()[0]  # Result: "$49.91"

# Take the currency symbol from price tag
price_symbol = whole_price_content_tag.find(name="span", class_="a-price-symbol").getText()  # Result: "$"

# Get the price float number by splitting by resulted symbol
product_price = float(price_with_symbol.split(price_symbol)[1])  # Result: "49.91"

# Get product title
product_title = soup.find(id="productTitle").getText().strip()
