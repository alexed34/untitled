import requests
from terminaltables import AsciiTable


def get_request(url, params, headers):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    response = response.json()
    return response


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to in (0, None):
        return salary_from * 1.2
    elif salary_from in (0, None) and salary_to:
        return salary_to * 0.8
    elif salary_from and salary_to:
        return (salary_to - salary_from) / 2 + salary_from


def predict_rub_salary_for_SuperJob(vacancy):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    params = {'keyword': vacancy, 'count': 1, 'town': 4, 'catalogues': 48, 'page': 0}
    headers = {
        'X-Api-App-Id': 'v3.r.131389760.063d0996c4850f4be0f6ba6ee363ea55af14ec7a.935c128e7e4f53fb85a51269278ba78a44cc9699'}
    response_vacancy = get_request(url, params, headers)
    count_vacancy = response_vacancy.get('total')
    language_data = []
    for i in range(count_vacancy // 100 + 1):
        params = {'keyword': vacancy, 'count': 100, 'town': 4, 'catalogues': 48, 'page': i}
        for i in get_request(url, params, headers).get('objects'):
            if i.get('currency') == 'rub':
                # print(f"{i.get('profession')}, {i.get('town').get('title')}, {predict_salary(i.get('payment_from'), i.get('payment_to'))} ")
                language_data.append(predict_salary(i.get('payment_from'), i.get('payment_to')))
    language = {"vacancies_found": count_vacancy, "vacancies_processed": len(list(filter(None, language_data))),
                "average_salary": int(
                    int(sum(list(filter(None, language_data)))) / len(list(filter(None, language_data))))}
    return language


def predict_rub_salary_hh(vacancy):
    url = 'https://api.hh.ru/vacancies'
    page = 0
    url_parameter = {'text': vacancy, 'area': '1', 'describe_arguments': 'true', 'page': page}
    headers = {}
    pages = get_request(url, url_parameter, headers).get('pages')
    vacancies_found = get_request(url, url_parameter, headers).get('found')
    language_data = []
    while page < pages:
        works = get_request(url, url_parameter, headers).get('items')
        for work in works:
            salary = work.get('salary')
            if salary is None:
                continue
            elif salary.get('currency') != 'RUR':
                continue
            salary_from = salary.get('from')
            salary_to = salary.get('to')
            language_data.append(predict_salary(salary_from, salary_to))
        page += 1
    language = {"vacancies_found": vacancies_found, "vacancies_processed": len(language_data),
                "average_salary": int(sum(language_data) / len(language_data))}
    return language


def create_table_consol(data, title):
    table_data = [
        ['Язык програмирование', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language in data:
        row = []
        row.append(language)
        values = data.get(language)
        for value in values:
            row.append(values.get(value))
        table_data.append(row)
    table_instance = AsciiTable(table_data, title)
    return table_instance.table


def main():
    programming_languages = ['Python', 'C', 'C++', 'Java',
                             'JavaScript', 'PHP', 'C#', 'Swift',
                             'Perl', '1C']
    all_languages_stat_SJ = {}
    all_languages_stat_HH = {}
    for programming_language in programming_languages:
        all_languages_stat_SJ[programming_language] = predict_rub_salary_for_SuperJob(programming_language)
        # all_languages_stat_HH[programming_language] = predict_rub_salary_hh(programming_language)
    print(create_table_consol(all_languages_stat_SJ, 'SuperJob Moscow'))
    print(create_table_consol(all_languages_stat_SJ, 'HeadHunter Moscow'))


if __name__ == '__main__':
    main()
