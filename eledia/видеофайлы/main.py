import os
import csv
import shutil
import time

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
    name2 = f'D:\\видео эледиа\\{name}\\{name}.txt'
    with open(name2, 'w') as f:
        f.write(f'{name}\n')
        f.write(f'{name} лечение с помощью акупунктурных точек \n')
        f.write(f'акупунктура,эледиа,эледия,электроакупунктура \n')
        for i in list:
            f.write(f'{i:{5}}- {dict_points[i]}\n')


def write_txt_mpeg(name, list):
    name2 = f'D:\видео эледиа\{name}\mpeg2.txt'
    with open(name2, 'w') as f:
        f.write(f"file 'zastavka.mp4'\n")
        for i in list:
            f.write(f"file '{i}.mp4'\n")


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


def remove_file(name):
    # os.rename('a.txt', 'b.kml')
    path1 = f'D:\видео эледиа\{name}\{name}.mp4'
    path2 = f'D:\видео эледиа\{name}\zastavka.mp4'
    os.rename(path1, path2)


def ffmpeg_file(name):
    os.chdir(f'D:\видео эледиа\{name}')
    os.system('ffmpeg -f concat -i mpeg2.txt -c copy all.mp4')
    time.sleep(10)

def rider_img_ffmpeg(name, counter):
    os.chdir(f'D:\видео эледиа\imgg')
    os.system(f'ffmpeg -i input.png -vf "drawtext=font=arial:text={name}:\
        fontcolor=0x000000:fontsize=60:x=50:y=200:" output{counter}.png ')

def main():
    with open('list_led_poln.csv', ) as f:
        rider = csv.reader(f)
        counter = 0
        for i in rider:
            name = i[1].strip('"')  # название болезни
            # name = name.encode('utf-8')
            #
            # name = name.decode('utf-8')
            print(name)
            #list = greate_list_points(i[2])  # список с точками болезни
            # for point in list:
            #     #print(point)
            #     if not os.path.exists(f'D:\видео эледиа\points\{point}.mp4'):
            #         print(f'{point}')
            # writ_dir(name)  # создаем папку с именем болезни
            # print(name, list)
            # write_txt_mpeg(name, list)  # создаем txt файл с точками в папке с болезнью
            # copy_video(name, list)
            # remove_file(name)
            # write_txt(name, list)
            # break
            #ffmpeg_file(name)
            rider_img_ffmpeg(name, counter)
            counter += 1
            # if counter >= 1:
            #     break


if __name__ == '__main__':
    main()
