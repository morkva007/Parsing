import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urls = ['https://www.avito.ru/moskva/tovary_dlya_kompyutera/synology_rs822_novyy_nas_setevoe_hranilische_2503353325?utm_campaign=native&utm_medium=item_page_ios&utm_source=soc_sharing']

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=112, chrome_options=options) as browser:
        with open('resAvito.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for url in urls:
                result = []
                browser.get(url)
                try:
                    wait = WebDriverWait(browser, 15)
                    name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title-info-title-text")))
                    result.append(name.text)
                    price = browser.find_element(By.CLASS_NAME, 'styles-module-size_xxxl-A2qfi')
                    result.append(price.text.replace('&nbsp;', ''))
                    time.sleep(1)
                    subscriptions = [result.append(i.text) for i in browser.find_elements(By.CLASS_NAME, 'style-item-description-html-qCwUL')]
                    time.sleep(1)
                except:
                    print(f'нет товара по ссылке: {url}')
                writer.writerow(result)

