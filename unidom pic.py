import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import urllib
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


urls = [
    'https://krasnodar.unidom.ru/catalog/category/nabory_dlya_uborki_1/'
]


links = []

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=110, chrome_options=options) as browser:
        for i in urls:

            try:
                browser.get(i)
                wait = WebDriverWait(browser, 10)
                still = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       '/html/body/div[5]/div[6]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div/div/div[3]/div[2]/div[2]/div[2]/div/div/a')))
                if still is not None:
                    still.click()
                    time.sleep(2)
            except Exception as e:
                print(e)
            element = browser.find_elements(By.CLASS_NAME, 'dark_link.option-font-bold.font_sm')
            for e in element:
                links.append(e.get_attribute('href'))

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=110, chrome_options=options) as browser:
        try:

            for i in links:
                browser.get(i)
                article = [i.text for i in browser.find_elements(By.CLASS_NAME, 'article__value')][1]
                picture = browser.find_elements(By.CLASS_NAME,
                                                'product-detail-gallery__link.popup_link.fancy')
                if picture is not None:
                    for x in range(len(picture)):
                        href = picture[x].get_attribute('href')
                        urllib.request.urlretrieve(href, f'картинки_1/{article}_{x+1}.png')
        except Exception as e:
                print(e)
