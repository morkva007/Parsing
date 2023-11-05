from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import urllib
import time

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

        for i in urls:
            browser.get(i)
            article = [a.text.replace('Арт: ', '') for a in browser.find_elements(By.CLASS_NAME, "XEgr0")][2]
            s = browser.find_elements(By.XPATH,
                                      '//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div/div/div/picture/img')
            time.sleep(1)
            for x in s:
                x.click()
                time.sleep(1)
            picture = []

            for _ in range(5):
                image = browser.find_elements(By.XPATH,
                                              '//*[@id="product__root"]/div/div[3]/div[3]/div/div[2]/div[4]/div/div/div/div[1]/div/div[2]/div/div/img')
                for i in image:
                    picture.append(i.get_attribute('src'))

                    n = browser.find_element(By.XPATH,
                                             '//*[@id="product__root"]/div/div[3]/div[3]/div/div[2]/div[4]/div/div/div/div[1]/div/div[2]/button[2]')


                    if n == None:
                        urllib.request.urlretrieve(picture[p], f'{article}.png')
                    else:
                        n.click()
                        for p in range(len(picture)):
                            urllib.request.urlretrieve(picture[p], f'картинки_4/{article}_{p}.png')
                            time.sleep(1)

