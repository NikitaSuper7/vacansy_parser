from src.abstract_classes import Parser
import requests


class Vacansy(Parser):
    """Класс получения вакансий."""

    def __init__(self, url, headers, params):
        self.url = url  # 'https://api.hh.ru/vacancies'
        self.headers = headers  # {'User-Agent': 'HH-User-Agent'}
        self.params = params  # {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_response(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            vacansies = response.json()['items']
            self.vacancies.extend(vacansies)
            self.params['page'] += 1

    def __str__(self):
        return self.vacancies


emp_1 = Vacansy('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
                {'text': '', 'page': 0, 'per_page': 100})

emp_1.get_response('Python')

print(emp_1.vacancies)
