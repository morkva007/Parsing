from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import urllib


url = ['https://www.sima-land.ru/4881071/molochnik-vysokiy-bernadotte-dekor-dikaya-roza-otvodka-zoloto-180-cm/',
       'https://www.sima-land.ru/4880505/molochnik-vysokiy-bernadotte-dekor-blednye-rozy-otvodka-platina-180-ml/',
'https://www.sima-land.ru/4880357/podnos-s-ruchkami-bernadotte-dekor-otvodka-zoloto-23-cm/',
       'https://www.sima-land.ru/7344880/molochnik-vysokiy-bernadotte-dekor-angliyskaya-roza-otvodka-zoloto-250-ml/',
'https://www.sima-land.ru/4880583/saharnica-bernadotte-dekor-gusi-220-ml/',
'https://www.sima-land.ru/4880520/saharnica-bernadotte-dekor-blednye-rozy-otvodka-platina-300-ml/',
'https://www.sima-land.ru/4880837/saharnica-bernadotte-dekor-meysenskiy-buket-300-ml/',
'https://www.sima-land.ru/6913549/derzhatel-dlya-salfetok-17-3-17-3-9-cm-metall/',
'https://www.sima-land.ru/2976756/podnos-fruktskel-35-x-5-x-23-cm/',
       'https://www.sima-land.ru/7344887/podnos-louise-dekor-otvodka-platina-35-cm/'
       ]
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=107, chrome_options=options) as browser:
        for i in url:
            browser.get(i)
            article = [a.text.replace('Арт: ', '') for a in browser.find_elements(By.CLASS_NAME, "XEgr0")][2]
            picture = []
            image = browser.find_elements(By.XPATH, '//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div/div/div/picture/source[1]')
            for i in image:
                picture.append(i.get_attribute('srcset'))
            for p in range(len(picture)):
                urllib.request.urlretrieve(picture[p], f'картинка_3/{article}_{p}.png')



