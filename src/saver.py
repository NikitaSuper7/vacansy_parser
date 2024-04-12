import json

from src.abstract_classes import AbsRedactor
from src.vacansy import Vacansy
from src.hh import HH


class JsonSaver(AbsRedactor):
    "Класс сохраняет, добавляет, удаляет вакансии из/в файл."

    def __init__(self, all_vacancies: list):
        self.all_vacancies = all_vacancies

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

    def json_loader(self, how_many: int, file: json = 'src/vacansies.json'):
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

    def _json_adder(self, vac_id: str, name: str, description: str, salary: float, location: str, link: str,
                    vac_type: str):
        """Добавляет вакансию в файл"""
        vac_dict = {"id": vac_id, "name": name, "description": description,
                    "salary": salary, "location": location, "link": link,
                    "type": vac_type}
        with open('vacansies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(vac_dict)
        with open('vacansies.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def _json_deleter(self, vac_id: str):
        """Удаляет вакансии из файла."""
        with open('vacansies.json', 'r', encoding='utf-8') as file:
            responds = json.load(file)
            for respond in range(len(responds)):
                if responds[respond]['id'] == vac_id:
                    responds.pop(respond)
                    break
        with open('vacansies.json', 'w', encoding='utf-8') as file:
            json.dump(responds, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    emp_1 = HH('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
               {'text': '', 'page': 0, 'per_page': 100})

    emp_1.get_response('Python, developer')
    Vacansy._make_objects(emp_1)
    Vacansy._sorter_salary()
    Vacansy._salary_range([50_000, 100_000])

    str_vacansy = JsonSaver(Vacansy.all_vacancies)
    str_vacansy.json_saver()

    str_vacansy._json_adder(vac_id='123', name='test', description='test', salary=75_000, location='here is',
                            link='test_ru', vac_type='open_test')
