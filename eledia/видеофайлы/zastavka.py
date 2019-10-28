# добавление в папки с болезнями заставки и удаление файла zastavka
import os
import csv
import shutil

# создаем список болезней для создания папок.
def greate_list_points(url):
    url = url.strip('[]\'').split('\', \'')
    return url

def copy_video(name):
    if not os.path.exists(f'D:\видео эледиа\{name}\{name}.mp4'):
        shutil.copy(f'D:\видео эледиа\zastavka\{name}.mp4', f'D:\видео эледиа\{name}')
    else:
        print(f'{name} - существует')




def main():
    with open('list_led_poln.csv') as f:
        rider = csv.reader(f)
        counter = 0
        for i in rider:
            name = i[1].strip('"')  # название болезни
            copy_video(name)
            # counter += 1
            # if counter >= 2:
            #     break





if __name__ == '__main__':
    main()