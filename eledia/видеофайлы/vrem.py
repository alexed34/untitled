import csv


list_url = []
def dict_url(): # функция выдает словарь с ключь - имя точки, значение - url
    with open('dict.csv' ) as f:
        file = csv.reader(f)
        dict_f = {}
        for i in file:
            if i:
                a = i[1].split('\'')
                #print(a[1])
                dict_f[i[0]] = f'http://www.eledia.ru{a[1]}'
    return dict_f


dict_points = dict_url()


# with open('dict_url.csv', "a", newline="") as f:
#     for name, key in dict2.items():
#         f.write(f'{name}:{key}\n')

