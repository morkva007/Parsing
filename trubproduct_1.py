from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
urls = []
for i in range(1, 6):
    url = f'https://ekb.truboproduct.ru/list_iz_splava_nicrofer/page/{i}/'
    urls.append(url)
result = []
for u in range(len(urls)):
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get(urls[u])
        discripshion = [txt.text.replace('\n', '') for txt in browser.find_elements(By.CLASS_NAME, 'box-content')][1:2]
        name = [txt.text for txt in browser.find_elements(By.TAG_NAME, 'td')]

        result.append(name)
        result.append(discripshion)

with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(result)