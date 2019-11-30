import requests


def get_requests_jobs(url, param):
    response = requests.get(url, params=param)
    response.raise_for_status()
    response = response.json()
    return response


def find_number_vacancies(vacancies):
    return vacancies.get('found')


def find_rub_salary(vacancy, page):
    url = 'https://api.hh.ru/vacancies'
    url_parameter = {'text': vacancy, 'area': '1', 'describe_arguments': 'true', 'page': page}
    works = get_requests_jobs(url, url_parameter).get('items')
    salaries = []
    for work in works:
        salary = work.get('salary')
        if salary is None:
            continue
        elif salary.get('currency') != 'RUR':
            continue
        elif salary.get('to') is None:
            salaries.append(salary.get('from') * 1.2)
        elif salary.get('from') is None:
            salaries.append(salary.get('to') * 0.8)
        else:
            salaries.append((salary.get('to') - salary.get('from')) / 2 + salary.get('from'))
    return salaries


def write_data(text):
    with open('data.txt', 'a') as f:
        for key, val in text.items():
            f.write('{}:{}\n'.format(key, val))


def main():
    url = 'https://api.hh.ru/vacancies'
    programming_languages = ['Python', 'C', 'C++', 'Java',
                             'JavaScript', 'PHP', 'C#', 'Swittl',
                             'Perl', '1C']
    all_languages_stat = {}
    all_languages_data = {}
    for programming_language in range(len(programming_languages)):
        page = 0
        url_parameter = {'text': programming_languages[programming_language], 'area': '1', 'page': page}
        pages = get_requests_jobs(url, url_parameter).get('pages')
        language_data = []
        while page < pages:
            url_parameter = {'text': programming_languages[programming_language], 'area': '1', 'page': page}
            salary = find_rub_salary(programming_languages[programming_language], page)
            language_data.extend(salary)
            page += 1
            all_languages_data[programming_languages[programming_language]] = language_data
        vacancies_found = find_number_vacancies(get_requests_jobs(url, url_parameter))
        language = {"vacancies_found": vacancies_found, "vacancies_processed": len(language_data),
                    "average_salary": int(sum(language_data) / len(language_data))}
        all_languages_stat[programming_languages[programming_language]] = language
    write_data(all_languages_stat)
    print(all_languages_stat)


if __name__ == '__main__':
    main()
