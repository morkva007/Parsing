import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv
import urllib



urls = [
    'https://ekaterinburg.leroymerlin.ru/product/obogrevatel-infrakrasnyy-gazovyy-ballu-bigh-55-15519307/',
    'https://ekaterinburg.leroymerlin.ru/product/obogrevatel-gazovyy-infrakrasnyy-45-kvt-82024151/'
]

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=107, chrome_options=options) as browser:
        with open('resLM.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for url in urls:
                result = []
                browser.get(url)
                time.sleep(1)
                try:
                    article = [n.text for n in browser.find_elements(By.CLASS_NAME, "t12nw7s2_pdp")][0]
                    result.append(article)
                    images = [i for i in browser.find_elements(By.TAG_NAME, "source")]
                    picture = []
                    for image in images:
                        p = image.get_attribute('srcset')
                        picture.append(p)
                    img = []
                    for i in range(0, len(picture), 5):
                        img.append(picture[i])
                    for x in range(10):
                        try:
                            urllib.request.urlretrieve(img[x], f'{article}_{x}.png')
                        except:
                            continue
                except:
                    continue
                try:
                    name = [n.text for n in browser.find_elements(By.CLASS_NAME, "t12nw7s2_pdp")][1]
                    result.append(name)
                except:
                    continue
                try:
                    price = [p.text for p in browser.find_elements(By.TAG_NAME, "showcase-price-view")][1]
                    result.append(price)
                except:
                    continue
                try:
                    description = [d.text for d in browser.find_elements(By.CLASS_NAME, "p11satbv_pdp")]
                    result.append(description)
                except:
                    continue
                try:
                    features = [f.text for f in browser.find_elements(By.TAG_NAME, "li")]
                    result.append(features)
                except:
                    continue
                try:
                    specifications = [s.text.replace('\n', ': ') for s in browser.find_elements(By.CLASS_NAME, "p2o81wx_pdp")]
                    result.append(specifications)
                except:
                    continue
                writer.writerow(result)

                browser.find_element(By.XPATH, '')














