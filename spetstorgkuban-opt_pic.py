import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import undetected_chromedriver as uc
import urllib

urls = 'https://spetstorgkuban-opt.mag1c.ru/applications/Store?state=catalog-0-bf585ca0-5638-4b16-bee2-c7a7a6ed97c8'

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
            time.sleep(5)
        name = [n.text for n in browser.find_elements(By.CLASS_NAME, "_16asfvgw")]
        print(name)
        images = [i for i in browser.find_elements(By.TAG_NAME, 'img')]
        picture = []
        for image in range(5, len(images)):
            im = images[image].get_attribute('src')
            picture.append(im)
        print(picture)
        for x in range(len(picture)):
            try:
                urllib.request.urlretrieve(picture[x], f'{name[x]}.png')
            except:
                continue
