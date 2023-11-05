from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

url = 'https://ekb.truboproduct.ru/stalnaja_polirovannaja_lenta/page/1/'

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

with webdriver.Chrome() as browser:
    browser.get(url)
    discripshion = [txt.text.replace('\n', '') for txt in browser.find_elements(By.CLASS_NAME, 'box-content')][1:2]
    #name = [txt.text for txt in browser.find_element(By.TAG_NAME, 'td')]
    name = [txt.text for txt in browser.find_elements(By.TAG_NAME, 'td')]
    print(discripshion)
    print(name)

result = []
result.append(name)
result.append(discripshion)

with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(result)


#with webdriver.Chrome() as browser:
    #browser.get('https://stepik-parsing.ru/selenium/1/1.html')
    #input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
    #time.sleep(5)
