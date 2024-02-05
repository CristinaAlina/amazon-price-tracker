# Day 47 - 100 Days of Code: The Complete Python Pro Bootcamp for 2023

## Amazon Price Tracker Program - Follow a product price on Amazon and get email notification if that product has a lower price (Personal Use)

![Amazon-price-tracker](https://mrhsridgereview.org/wp-content/uploads/2020/12/Amazon-Cart-Photo-900x657.jpg)

## Steps:
1. Choose a desired product on Amazon (set URL_PRODUCT to which product you want from [Amazon](https://www.amazon.com/))
2. Use [MY HTTP  HEADER](https://myhttpheader.com/) to get your User-Agent and Accept-Language to format headers for get method
3. Scrape the product page using get method and use BeautifulSoup module to parse the page html and take product price and title
4. Send email notification if the desired product has the price for which you are willing to buy it (set target_price as a threshold)
