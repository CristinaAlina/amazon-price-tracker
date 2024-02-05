import os

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
