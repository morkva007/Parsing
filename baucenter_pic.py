import requests
from bs4 import BeautifulSoup

urls = ['https://baucenter.ru/kabel_i_provod_gibkiy/996630/']
for u in range(len(urls)):
    url = urls[u]
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find("section", class_="product").find("p", class_="product-head_right").text.replace('\n                ', '')
    shema = 'https://baucenter.ru'
    picture = [x['src'] for x in soup.find('div', class_='product_gallery-image').find_all('img')]
    for p in range(len(picture)):
        response = requests.get(f'{shema}{picture[p]}')
        res = response.content
        with open(f'{article}_{p}.jpeg', 'wb') as file:
            file.write(res)

