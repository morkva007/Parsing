import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv
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
        with open('resUnidom.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for l in links:
                browser.get(l)
                result = []
                name = [i.text for i in browser.find_elements(By.ID, 'pagetitle')]
                result.append(name)
                article = [i.text for i in browser.find_elements(By.CLASS_NAME, 'article__value')][1]
                result.append(article)
                price = [p.text.replace("&nbsp;", "") for p in browser.find_elements(By.CLASS_NAME, 'price.font-bold.font_mxs')]
                result.append(price)
                discriptions = [d.text.replace('\n', '; ') for d in browser.find_elements(By.ID, 'desc')]
                result.append(discriptions)
                characteristics_title = browser.find_elements(By.CLASS_NAME, 'char_name')
                for c in characteristics_title:
                    result.append(c.text)
                characteristics_value = browser.find_elements(By.CLASS_NAME, 'char_value')
                for h in characteristics_value:
                    result.append(h.text)
                time.sleep(2)
                writer.writerow(result)







