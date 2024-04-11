from src.abstract_classes import Parser
import requests


hh_headers = {'User-Agent': 'HH-User-Agent'}
hh_params = {'text': '', 'page': 0, 'per_page': 100}
class HH(Parser):
    """Класс получения вакансий."""

    def __init__(self, url='https://api.hh.ru/vacancies', headers=hh_headers, params=hh_params):
        """Создает объект класса для запроса. Работает с дефолтным URL."""
        super().__init__(url, headers, params)
        self.url = url  # 'https://api.hh.ru/vacancies'
        self.headers = headers  # {'User-Agent': 'HH-User-Agent'}
        self.params = params  # {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_response(self, keyword):
        """Получет ответ от API запроса."""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            vacansies = response.json()['items']
            self.vacancies.extend(vacansies)
            # with open('vacansies.json', 'w',  encoding='utf-8') as e:
            #     json.dump(self.vacancies, e, ensure_ascii=False, indent=4)
            self.params['page'] += 1

    def __str__(self):
        return self.vacancies
