import csv
import requests
from bs4 import BeautifulSoup


def writer_csv(data):
    with open('list_led_zarub_poln.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['url'],
                         data['name'],
                         data['list_points']])


def get_html(url):
    return requests.get(url).text


def get_point(html):
    soup = BeautifulSoup(html, 'lxml')
    list_a = soup.find_all('a')
    #print(list_a)
    llist = []
    for point in list_a:
        if not point.text:
            continue
        else:
            point = point.text
            llist.append(point.split()[0])
    return llist
    #return [i.text.split()[0] for i in list_a]


def searсh_text(text):
    start = text.find('<div class="aa1"')
    finich = text.find('<div class="pluso"')
    text = text[start:finich]
    return text


def main():
    with open('atlas_led_zarub.csv') as file:
        f = file.readlines()
        # print(f)
        i = 0

        for name in f:
            name = name.strip('\n').split(',raz,')
            text = searсh_text(get_html(name[0]))
            data = {'url': name[0],
                    'name': name[1],
                    'list_points': get_point(text)}
            # print(name[0], name[1],  get_point(text))
            i += 1
            print(i)
            #get_point(text)
            writer_csv(data)


if __name__ == '__main__':
    main()
