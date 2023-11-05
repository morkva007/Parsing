import requests
from bs4 import BeautifulSoup
import csv

urls = [
'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-10/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-16/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-kabelnaya-freezstop-25-2/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-8/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-kabelnaya-freezstop-25-1/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-kabelnaya-freezstop-25-3/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-4/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-kabelnaya-freezstop-25-4/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-6/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-kabelnaya-freezstop-25-20/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-kabelnaya-freezstop-25-10/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/salnik-aks-3/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-20/',
    'https://www.taen.ru/catalog/greyushiy-kabel/samoreguliruyushiysya-nagrevatelnyy-kabel-dlya-trub/teplolyuks-sektsiya-nagrevatelnaya-vnutri-truby-freezstop-inside-10-12/'
]

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

for u in range(len(urls)):
    url = urls[u]
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        title = soup.find('h1', class_='h1').text
        article = soup.find('div', class_='articul').find('span').text
        all_price = soup.find('div', class_='price').text.strip()
        old_price = soup.find('div', class_='price').find(class_='old').text.strip()
        price_salle = sale = soup.find('div', class_='price').find('sup').text.strip()
        price = soup.find('div', class_='price').find('span').text.strip()
        description_name = [x.text for x in soup.find_all('span', class_='name')]
        description_value = [x.text for x in soup.find_all('span', class_='value')]
        slov = dict(zip(description_name, description_value))
    except:
        continue
    result = []
    try:
        result.append(title)
        result.append(article)
        result.append(all_price)
        #result.append(price)
        result.append(slov)

        with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(result)
    except:
        continue

    picture = [x['href'] for x in soup.find('div', class_='picture').find_all('a')]
    for p in range(len(picture)):
        response = requests.get(picture[p])
        res = response.content
        try:
            with open(f'{article}_{p}.jpeg', 'wb') as file:
                file.write(res)
        except:
            continue