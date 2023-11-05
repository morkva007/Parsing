from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

with open('res_b.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

urls = ['https://baucenter.ru/kabel_i_provod_gibkiy/996630/']
for u in range(len(urls)):
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    result = []
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get(urls[u])
        try:
            name = browser.find_element(By.CLASS_NAME, "product").find_element(By.TAG_NAME, "h1").text
        except:
            continue
        try:
            article = browser.find_element(By.CLASS_NAME, "product").find_element(By.CLASS_NAME, "product-head_right").text.replace('Арт. ', '')
        except:
            continue
        try:
            price = browser.find_element(By.CLASS_NAME, "product").find_element(By.CLASS_NAME, "totalJsPrice").text
        except:
            continue
        try:
            descriptions = browser.find_element(By.CLASS_NAME, "product-collapse_drop").text
        except:
            continue
        try:
            descriptions_more = [d.text.replace('\n', ' ') for d in browser.find_elements(By.TAG_NAME, "p")][4:5]
        except:
            continue
        try:
            specifications = [s.text for s in browser.find_elements(By.CLASS_NAME, "description-more_table-row")]
        except:
            continue
        result.append(name)
        result.append(article)
        result.append(price)
        result.append(descriptions)
        result.append(descriptions_more)
        result.append(specifications)

with open('res_b.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(result)