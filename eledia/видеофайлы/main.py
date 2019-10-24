import os
import csv
import shutil

list_diseas = []
list_diseas_points = []


# создаем список болезней для создания папок.
def greate_list_points(url):
    url = url.strip('[]\'').split('\', \'')
    return url


# создаем папку с названием болезни
def writ_dir(name):
    path = f'D:\видео эледиа\{name}'
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана директория %s " % path)


def dict_url():  # функция выдает словарь с ключь - имя точки, значение - url
    with open('dict.csv') as f:
        file = csv.reader(f)
        dict_f = {}
        for i in file:
            if i:
                a = i[1].split('\'')
                # print(a[1])
                dict_f[i[0]] = f'http://www.eledia.ru{a[1]}'
    return dict_f


dict_points = dict_url()


# записываем текстовый файл
def write_txt(name, list):
    name = f'D:\видео эледиа\{name}\{name}.txt'
    with open(name, 'a') as f:
        for i in list:
            f.write(f'{i:{5}}- {dict_points[i]}\n')


def copy_video(name, list):
    shutil.copyfile(f'D:\видео эледиа\points\zastavka.mp4', f'D:\видео эледиа\{name}\zastavka.mp4')
    for point in list:
        if os.path.exists(f'D:\видео эледиа\points\{point}.mp4'):
            shutil.copyfile(f'D:\видео эледиа\points\{point}.mp4', f'D:\видео эледиа\{name}\{point}.mp4')
        else:
            print(f'{point} - не существует')
            name2 = f'D:\видео эледиа\{name}\{name}.txt'
            with open(name2, 'a') as f:
                f.write(f'{point} - не существует')


def main():
    with open('list_led_poln.csv') as f:
        rider = csv.reader(f)
        for i in rider:
            name = i[1]  # название болезни
            list = greate_list_points(i[2])  # список с точками болезни
            writ_dir(name)  # создаем папку с именем болезни
            print(name, list)
            write_txt(name, list)  # создаем txt файл с точками в папке с болезнью
            copy_video(name, list)
            break


if __name__ == '__main__':
    main()
