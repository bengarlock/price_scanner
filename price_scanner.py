from selenium import webdriver
import requests
import time


endpoint = 'https://bengarlock.com/api/v1/price_scanner/favorites/'


favorites = requests.get(f'{endpoint}').json()

for favorite in favorites:
    print(favorite)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(favorite['url'])
    item_name = driver.find_element_by_id("productTitle")
    try:
        price = driver.find_element_by_id("priceblock_ourprice")
    except:
        price = driver.find_element_by_id("priceblock_saleprice")

    picture = driver.find_element_by_css_selector('#landingImage').get_attribute('src')

    if favorite['name'] == '':
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json'
        }

        payload = {
            'name': item_name.text,
            'image': picture
        }

        requests.patch(url=f'{endpoint}' + str(favorite['id']) + '/', data=payload)

    print(f"{item_name.text} - {price.text}")
    driver.quit()
