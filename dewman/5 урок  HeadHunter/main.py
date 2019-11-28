import requests

def get_requests_jobs(url, param):
    response = requests.get(url,  params=param)
    response.raise_for_status()
    response = response.json()
    return response

def find_number_vacancies(vacancies):
    return vacancies.get('found')

def find_rub_salary(vacancy):
    url = 'https://api.hh.ru/vacancies'
    request_parameter = {'text': vacancy, 'area': '1', 'describe_arguments': 'true'}
    works = get_requests_jobs(url, request_parameter).get('items')
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



def main():
    url = 'https://api.hh.ru/vacancies'
    programming_languages = ['Python', 'C', 'C++', 'Java',
                             'JavaScript', 'PHP', 'C#', 'Swittl',
                             'Perl', '1C']
    all_languages = {}
    for programming_language in range(len(programming_languages)):
        work = {'text': programming_languages[programming_language], 'area': '1'}
        print(programming_languages[programming_language])
        vacancies_found = find_number_vacancies(get_requests_jobs(url, work))
        salary = find_rub_salary(programming_languages[programming_language])
        language = {"vacancies_found": vacancies_found, "vacancies_processed": len(salary),
                    "average_salary": int(sum(salary) / len(salary))}
        all_languages[programming_languages[programming_language]] = language

    print(all_languages)


if __name__ == '__main__':
    main()