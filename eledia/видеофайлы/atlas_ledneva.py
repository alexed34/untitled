import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    return requests.get(url).text

def write_csv(data):
    with open('atlas_led_zarub.csv', 'a', newline='') as f:
        writers = csv.writer(f)
        writers.writerow([data['url'],
                          'raz',
                         data['name']])

def get_date(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='789').find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        name = tds[0].find('a').text
        url = tds[0].find('a').get('href')
        print(url, name )
        data = {'name': name,
                'url': url,}
        write_csv(data)


def main():
    url = 'http://www.eledia.ru/publ/1'
    print(get_date(get_html(url)))


if __name__ == '__main__':
    main()
