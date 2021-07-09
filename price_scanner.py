from selenium import webdriver
import requests
import platform
import os

def detect_system():
    if platform.system() == 'Darwin':
        path = os.path.abspath("chromedriver")
        selenium_driver = webdriver.Chrome(path)
    elif platform.system() == 'Windows':
        path = os.path.abspath("chromedriver.exe")
        selenium_driver = webdriver.Chrome(path)
    return selenium_driver

urls = requests.get('https://bengarlock.com/api/v1/price_scanner/urls/').json()
for url in urls:
    print(url)
    driver = detect_system()
    driver.get(url['url'])
    item_name = driver.find_element_by_id("productTitle")
    try:
        price = driver.find_element_by_id("priceblock_ourprice")
    except:
        price = driver.find_element_by_id("priceblock_saleprice")

    picture = driver.find_element_by_css_selector('#landingImage').get_attribute('src')
    print(f"{item_name.text} - {price.text}")
    driver.quit()
