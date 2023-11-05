import requests
from bs4 import BeautifulSoup
import csv

urls = [
'https://anepmetall.ru/poliamid-maslonapolnennyj-blochnyj-listovoj-vysshij-sort-pa-6-a-10-mm-tu-2224-001-78534599-2006/'
]

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

for u in range(len(urls)):
    url = urls[u]
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('li', class_='breadcrumb-item active').text
    article = soup.find('div', class_='articul').find('span').text
    all_price = soup.find('div', class_='price').text.strip()
    old_price = soup.find('div', class_='price').find(class_='old').text.strip()
    price_salle = sale = soup.find('div', class_='price').find('sup').text.strip()
    price = soup.find('div', class_='price').find('span')
    description = [x.text for x in soup.find_all('ul', class_="product-info list-unstyled ps-md-3 mb-4")]
    description_value = soup.find('div', class_="text-description").find('p').text
    slov = dict(zip(description_name, description_value))
    result = []
    result.append(title)
    result.append(description_value)
    result.append(article)
    result.append(all_price)
    result.append(price)
    result.append(slov)

    for i in description:
        result.append(i)


    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(result)

    picture = [x['src'] for x in soup.find('img', {'itemprop':'image'})]
    for p in range(len(picture)):
        response = requests.get(picture[p])
        res = response.content
        with open(f'{article}_{p}.jpeg', 'wb') as file:
            file.write(res)

