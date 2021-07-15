import datetime

from selenium import webdriver
import requests
import platform
import os
import time

endpoint = 'https://bengarlock.com/api/v1/price_scanner/favorites/'


def detect_system():
    if platform.system() == 'Darwin':
        path = os.path.abspath("chromedriver")
        selenium_driver = webdriver.Chrome(path)
        return selenium_driver
    elif platform.system() == 'Windows':
        path = os.path.abspath("chromedriver.exe")
        selenium_driver = webdriver.Chrome(path)
        return selenium_driver
    elif platform.system() == 'Linux':
        path = os.path.abspath("chromedriver-linux")
        selenium_driver = webdriver.Chrome(path)
        return selenium_driver


def push_price(favorite, price):
    print(favorite['name'], price)
    payload = {
        'price': price,
        'favorite': favorite['id']
    }
    requests.post(url='https://bengarlock.com/api/v1/price_scanner/prices/', data=payload)


def run_scan():
    favorites = requests.get(f'{endpoint}').json()
    driver = detect_system()
    driver.minimize_window()
    for favorite in favorites:
        driver.get(favorite['url'])
        item_name = driver.find_element_by_id("productTitle")
        try:
            price = driver.find_element_by_id("priceblock_ourprice")

        except:
            price = driver.find_element_by_id("priceblock_saleprice")

        picture = driver.find_element_by_css_selector('#landingImage').get_attribute('src')
        if favorite['name'] == '':
            payload = {
                'name': item_name.text,
                'image': picture
            }
            requests.patch(url=f'{endpoint}' + str(favorite['id']) + '/', data=payload)
        push_price(favorite, price.text)
    driver.quit()


n = True
while n:
    run_scan()
    print(f"Last Run Time - " + str(datetime.datetime.now()))
    print("Waiting 24 hours...")
    time.sleep(86400)
