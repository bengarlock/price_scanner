from selenium import webdriver
import requests
import time





urls = requests.get('https://bengarlock.com/api/v1/price_scanner/urls/').json()
for url in urls:
    print(url)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url['url'])
    item_name = driver.find_element_by_id("productTitle")
    try:
        price = driver.find_element_by_id("priceblock_ourprice")
    except:
        price = driver.find_element_by_id("priceblock_saleprice")

    picture = driver.find_element_by_css_selector('#landingImage').get_attribute('src')
    print(f"{item_name.text} - {price.text}")
    driver.quit()
