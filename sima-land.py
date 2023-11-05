import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv


urls = [
    'https://www.sima-land.ru/2954150/predtrenirovochnyy-kompleks-sportline-object-195-with-dmae-125-kapsul/',
    'https://www.sima-land.ru/1903370/predtrenirovochnyy-kompleks-sportline-t-34-with-dmae-sportivnoe-pitanie-bubble-gum-240-g/',
    'https://www.sima-land.ru/1316822/predtrenirovochnyy-kompleks-sportline-backdraft-chernaya-cmorodina-sportivnoe-pitanie-300-g/',
    'https://www.sima-land.ru/2620822/ekstrakt-guarany-sportivnoe-pitanie-1600-mg-nabor-9-flakonov-po-25-ml/',
    'https://www.sima-land.ru/4885509/predtrenirovochnyy-kompleks-black-eagle-apelsin-granat-sportivnoe-pitanie-240-g/',
    'https://www.sima-land.ru/4543043/predtrenirovochnyy-kompleks-popeye-supplenments-apelsin-marakuyya-sportivnoe-pitanie-250-g/',
    'https://www.sima-land.ru/4600925/predtrenirovochnyy-kompleks-sportline-nutrition-t-34-adrenalin-sportivnoe-pitanie-240-g/',
    'https://www.sima-land.ru/7754695/predtrenirovochnyy-kompleks-popeye-pre-workout-klubnika-laym-sportivnoe-pitanie-250-g/',
    'https://www.sima-land.ru/4543042/predtrenirovochnyy-kompleks-popeye-supplenments-limon-laym-sportivnoe-pitanie-250-g/',
    'https://www.sima-land.ru/4543041/predtrenirovochnyy-kompleks-popeye-supplenments-ekzoticheskie-frukty-sportivnoe-pitanie-250-g/'
]


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=109, chrome_options=options) as browser:
        with open('sim_2.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for i in urls:
                browser.get(i)
                result = []
                time.sleep(3)
                name = [n.text.replace("«", '').replace("»", '').replace("+", ' ') for n in browser.find_elements(By.CLASS_NAME, "fArxp")]
                result.append(*name)
                time.sleep(2)
                article = [a.text.replace('Арт: ', '') for a in browser.find_elements(By.CLASS_NAME, "XEgr0")][2]
                result.append(article)
                time.sleep(2)
                price = [a.text.replace(' ₽', '').replace('\u2009', '') for a in browser.find_elements(By.XPATH, '//*[@id="product__root"]/div/div[3]/div[1]/div/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div[1]/span')]
                result.append(price)
                time.sleep(2)
                specifications = [s.text.replace('\n', ':') for s in browser.find_elements(By.CLASS_NAME, "S3jLY")]
                result.append(specifications)
                time.sleep(2)
                discriptions = [d.text.replace('\n', ' ') for d in browser.find_elements(By.XPATH, '//*[@id="product__root"]/div/div[3]/div[2]/section[1]/div/div[1]')]
                result.append(*discriptions)
                writer.writerow(result)



