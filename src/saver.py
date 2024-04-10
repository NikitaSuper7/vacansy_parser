import json

# from src.abstract_classes import AbsSaver
from src.vacansy import Vacansy
from src.hh import HH


class Saver:
    def __init__(self, all_vacancies: list):
        self.all_vacancies = all_vacancies

        # self.id = vac_id
        # self.name = name
        # self.description = description
        # self.salary = salary
        # self.location = location
        # self.link = link
        # self.vac_type = vac_type

    def json_saver(self):
        """Переформатирует список объекто в JSON-объекты и сохраняет в файл."""
        total_vacansies = []
        for vacansy in self.all_vacancies:
            dict_vacansy = {'id': vacansy.vac_id, 'name': vacansy.name,
                            'description': vacansy.description if vacansy.description is None else vacansy.description.replace(
                                '</highlighttext>', '').replace(
                                '<highlighttext>', ''),
                            'salary': vacansy.salary,
                            'location': vacansy.location, 'link': vacansy.link, 'type': vacansy.vac_type}
            total_vacansies.append(dict_vacansy)
        with open('vacansies.json', 'w', encoding='utf-8') as file:
            json.dump(total_vacansies, file, ensure_ascii=False, indent=4)

    def json_loader(self, how_many: int,  file: json = 'src/vacansies.json'):
        """Достает нужные вакансии"""
        with open('src/vacansies.json', 'r', encoding='utf-8') as file:
            responds = json.load(file)
            responds = responds[0:how_many]
        rang_vac = 1
        for respond in responds:
            print(f"\nRang № {rang_vac}")
            rang_vac += 1
            for key, value in respond.items():
                print(key, value, end='\n')
        return responds

# if __name__ == '__main__':
#     emp_1 = HH('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
#                {'text': '', 'page': 0, 'per_page': 100})
#
#     emp_1.get_response('Python, developer')
#     Vacansy.make_objects(emp_1)
#     Vacansy.sorter_salary()
#     str_vacansy = Saver(Vacansy.all_vacancies)
#     str_vacansy.json_saver()
#     # print(str_vacansy.all_vacancies)
