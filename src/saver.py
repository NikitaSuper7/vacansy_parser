import json

from src.abstract_classes import AbsSaver
from src.vacansy import Vacansy
from src.hh import HH


class Saver(AbsSaver):
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


if __name__ == '__main__':
    emp_1 = HH('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
               {'text': '', 'page': 0, 'per_page': 100})

    emp_1.get_response('Python, developer')

    str_vacansy = Saver(Vacansy.make_objects(emp_1))
    str_vacansy.json_saver()
