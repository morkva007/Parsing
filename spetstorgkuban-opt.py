import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import undetected_chromedriver as uc
import csv


with open('res_s.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование',
                     'Артикул',
                     'Цена',
                     'Описание'])

urls = 'https://spetstorgkuban-opt.mag1c.ru/applications/Store?state=catalog-0-5c92b6ed-91b8-45d2-bfb4-6e862693e1da'

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=105, chrome_options=options) as browser:
        browser.get(urls)
        time.sleep(10)
        still = browser.find_elements(By.CLASS_NAME, "_wj1953c")
        still[1].click()
        time.sleep(2)
        cash = browser.find_element(By.CLASS_NAME, "_p5k7u1").click()
        time.sleep(5)
        while True:
            try:
                still[3].click()
                still[3].send_keys(Keys.DOWN)
            except:
                break
            time.sleep(7)
        product = browser.find_elements(By.CLASS_NAME, "_oxngbz")
        result = []
        for p in range(25, len(product) + 1, 10):
            try:
                product[p].click()
            except:
                continue
            try:
                name = browser.find_element(By.CLASS_NAME, "_145490k").find_element(By.CLASS_NAME, "_1i5yfgfw").text
                print(name)
                result.append(name)
            except:
                continue
            try:
                article = [a.text for a in browser.find_element(By.TAG_NAME, "aside").find_element(By.CLASS_NAME, "_glrrv9w")]
                print(article)
                result.append(article)
            except:
                continue
            try:
                price = browser.find_element(By.CLASS_NAME, "_19gqkxp0").text
                print(price)
                result.append(price)
            except:
                continue
            try:
                discriptions = browser.find_element(By.CLASS_NAME, "_8wo4ylw").text
                print(discriptions)
                result.append(discriptions)
            except:
                continue

            time.sleep(10)
            path = browser.find_element(By.CLASS_NAME, "_lzttes").click()


        with open('res_s.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(result)



