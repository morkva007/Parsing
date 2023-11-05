from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import urllib
import time

urls = [
    'https://www.sima-land.ru/4232024/kollagen-s-ironman-sportivnoe-pitanie-144-kapsuly/',
    'https://www.sima-land.ru/7754700/vitaminy-popeye-liquid-chlorophyll-concentrate-500-ml/',
'https://www.sima-land.ru/4600930/specialnyy-preparat-sportline-nutrition-glucosamine-chondroitin-msm-powder-mandarin-sportivnoe-pitanie-300-g/',
    'https://www.sima-land.ru/4600931/specialnyy-preparat-sportline-nutrition-glucosamine-chondroitin-msm-powder-tropik-sportivnoe-pitanie-300-g/',

]


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=109, chrome_options=options) as browser:

        for i in urls:
            browser.get(i)
            article = [a.text.replace('Арт: ', '') for a in browser.find_elements(By.CLASS_NAME, "XEgr0")][2]
            s = browser.find_elements(By.XPATH,
                                      '//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div/div/div/picture/img')
            time.sleep(1)
            for x in s:
                x.click()
                time.sleep(2)
            picture = []

            for _ in range(5):
                image = browser.find_elements(By.XPATH,
                                              '//*[@id="product__root"]/div/div[3]/div[3]/div/div[2]/div[4]/div/div/div/div[1]/div/div[2]/div/div/img')
                for i in image:
                    picture.append(i.get_attribute('src'))
                    for p in range(len(picture)):
                        urllib.request.urlretrieve(picture[p], f'картинки_4/{article}.png')



