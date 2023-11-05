import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv



urls = [
    'https://www.klenmarket.ru/shop/cookware/crockery/'
]

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=110, chrome_options=options) as browser:
        with open('resKlen.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for url in urls:
                result = []
                browser.get(url)
                time.sleep(1)
                city = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/button[2]").click()
                time.sleep(1)
                choose = browser.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div[10]/a")
                choose.click()
                time.sleep(3)
                link = browser.find_elements(By.CLASS_NAME, 'shop-crockery-list__category-item')
                for l in link:
                    l.get_attribute('href')
                    l.click()
                    link_2 = browser.find_elements(By.CLASS_NAME, 'shop-crockery__item-head')
                    for k in link_2:
                        k.get_attribute('href')
                        k.click()
                        name = browser.find_element(By.CLASS_NAME, 'shop-item__heading').text
                        print(name)
                        result.append(name)
                        article = browser.find_element(By.CLASS_NAME, 'text-warning').text
                        print(article)
                        result.append(article)
                        country = browser.find_element(By.CLASS_NAME, 'hidden-below-m').text
                        print(country)
                        result.append(country)
                        key_discriptions = browser.find_elements(By.TAG_NAME, 'dt')
                        for k in key_discriptions:
                            print(k)
                            result.append(k.text)
                        value_discriptions = browser.find_elements(By.TAG_NAME, 'dd')
                        for v in value_discriptions:
                            print(v)
                            result.append(v.text)
                writer.writerow(result)









