import requests
import csv
#from bs4 import BeautifulSoup


def get_list_url():  # создаем список url для  парсинга
    with open('url.csv', newline='') as f:
        rider = csv.reader(f)
        list_url = []
        for i in rider:
            if i:
                # print(''.join(i))
                list_url.append(''.join(i))
        return list_url


def get_dict_url():  # получаем словарь с значениями точка - ссылка 'P.10': '<a href="http://www.eledia.ru/publ/17-1-0-75" target="_blank">P10 Юй-цзи </a>',
    with open('dict.csv') as f:
        rider = csv.reader(f)
        dict_ul = {}
        for i in rider:
            if i:
                key_point = list(i[0])
                vrem_list = []

                for n in range(len(key_point)):
                    if key_point[n].isdigit():
                        if '.' not in vrem_list:
                            vrem_list.append('.')
                    vrem_list.append(key_point[n])
                get_point = ''.join(vrem_list)
                # list_points_with_point.append(''.join(ns))

                dict_ul[get_point] = i[1]
        return dict_ul


def delet_name_point():  # создаем список названий точек которые удалим из ориг. текста
    with open('dict.csv') as f:
        rider = csv.reader(f)
        point_del = []
        #print('aa')
        for i in rider:
            if i:
                a = i[1].split()
                point_del.append(a[3])
                # print(a[3])
        return point_del


def get_html(url):
    r = requests.get(url)
    return r.text


#
def searh_text(text):
    one = text.find('Сочетание:')
    two = text.find('Техника:')
    text = text[one:two]
    text = text.replace('.<br>', ' <br>')
    text = text.replace(',', ' ')
    text = text.replace('.<br />', ' <br>')
    text = text.replace('.З', '.3')
    text = text.replace('Е.36.', 'Е.36')
    text = text.replace('Лин-даоС.4', 'Лин-дао C.4')
    text = text.replace('МС.З', 'МС.3 ')
    text = text.replace('G1', 'GI')
    text = text.replace('GT', 'GI')
    text = text.replace('Шан-синVG.23', 'Шан-син VG.23')
    text = text.replace('С.б', 'C.6')
    text = text.replace('Ю.5', 'IG.5 ')
    text = text.replace('IG. 17', 'IG.17')
    text = text.replace('Шан-CHHVG.23', 'Шан-CHH VG.23')
    text = text.replace('1G.4', 'IG.4')
    text = text.replace('К.41', 'Е.41')
    text = text.replace('1G.2', 'IG.2')
    text = text.replace('Чжи-гоуТR.6', 'Чжи-гоу ТR.6')
    text = text.replace('F.I3', 'F.13')
    text = text.replace('http://www.eledia.ru/publ/', '/publ/')
    text = text.replace('.1З', '.13')
    text = text.replace('Е.3З', 'Е.33')
    text = text.replace('МС. 7', 'МС.7')
    text = text.replace('С. 7', 'С.7')
    text = text.replace('Р. 10', 'Р.10')
    text = text.replace('style="color: rgb(0 0 0); font-family: verdana arial helvetica; font-size: 13.3333px; line-height: normal;"', '')
    text = text.replace('style="color: rgb(9 102 28); font-family: verdana arial helvetica; font-size: 13.3333px; line-height: normal;"', '')

    text = text.split()
    return text


def replace_text(text, del_point, repl_point):
    new_text = []
    new_text2 = []
    for i in text:
        if i not in del_point:
            new_text.append(i)
    for i in new_text:
        if i in repl_point:
            new_text2.append(repl_point.get(i) + ',')
            continue
        new_text2.append(i)
    return ' '.join(new_text2)


def writer_text(text):
    with open('text.txt', 'a') as f:
        f.write(text)
        f.write('\n')


# def check_link(text):
#     num = 0
#     for i in text:
#         #print(i)
#         if "href='/publ" in i:
#             #print('Уже менял')
#             num += 1
#             #print(num)
#             break
#     if num == 0:
#         return text
#     else:
#         return 'noy'



def main():
    for url in get_list_url()[:50]:
        if url:
            text = searh_text(get_html(url))
            #text = check_link(text)
            #print(text)
            num = 0
            for i in text:
                if ("href='/publ" in i or 'href="/publ/' in i):
                    num += 1
                    break
            if num == 0:
                writer_text(url + '-13')
                writer_text(replace_text(text, delet_name_point(), get_dict_url()))
                writer_text('\n')
            else:
                writer_text('уже менял')
                #writer_text('\n')







if __name__ == '__main__':
    main()
