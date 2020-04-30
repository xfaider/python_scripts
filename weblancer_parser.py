import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.weblancer.net/jobs/'


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print ("Error")
        quit()

def get_page_count(html):
    soup = BeautifulSoup(html, features="lxml")
    paggination = soup.find('div', class_='pagination_box')
    return int(paggination.find_all('a')[-1]['href'].split("=")[1])


def parse(html):
    soup = BeautifulSoup(html, features="lxml")
    table = soup.find('div', class_='page_content').find('div', class_='cols_table')
    rows = table.find_all('div', class_='row')

    projects = []
    nmbr = 1
    for row in rows:
        # Знак валюты в конец строки
        price = row.find('div', class_='float-right float-sm-none title amount indent-xs-b0').text
        if price != '':
            price=price[1:]+price[0]
            
        projects.append({
            'title': row.find('a', class_='text-bold show_visited').text,
            'short_description': row.find('p').text,
            'categories': [category.text for category in row.find('div', class_='col-sm-8 text-muted dot_divided').find_all('a')],
            'price': price,
            'application': row.find('div', class_='float-left float-sm-none text_field').text.strip(),
            'link': 'https://www.weblancer.net' + str(row.find('a', class_='text-bold show_visited').get('href'))
        })
    return projects

def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Проект', 'Краткое описание', 'Категории', 'Цена', 'Заявки', 'Link'))
        writer.writerows(
            (project['title'], project['short_description'], project['categories'], project['price'], project['application'], project['link']) for project in projects
        )



def main():
    total_pages = get_page_count(get_html(BASE_URL))
    print('Всего найдено %d страниц...' % total_pages)
    projects = []

    for page in range(1, total_pages + 1):
        print('Парсинг %d%% (%d/%d)' % (page / total_pages * 100, page, total_pages))
        projects.extend(parse(get_html(BASE_URL + "?page=%d" % page)))

    print('Сохранение...')
    save(projects, 'projects.csv')
    print('Готово!')


if __name__ == '__main__':
    main()