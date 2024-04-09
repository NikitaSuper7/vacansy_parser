from src.hh import HH


class Vacansy:
    """Класс для работы с вакансиями"""

    def __init__(self, id: str, name: str, description: str, salary: float, location: str, link: str, type: str):
        self.id = id
        self.name = name
        self.description = description
        self.salary = salary
        self.location = location
        self.link = link
        self.type = type

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"({self.id}, {self.name}, {self.description}, {self.salary}, {self.location}, {self.link}, {self.type})")

    @classmethod
    def make_objects(cls, all_vacansies: HH):
        list_vacansy = []
        for vacansy in all_vacansies.vacancies:
            name = f"{vacansy['id']}"
            list_vacansy.append(name)
            list_vacansy[-1] = cls(vacansy['id'], vacansy['name'], vacansy['snippet']['requirement'],
                                   vacansy['salary'],
                                   vacansy['area']['name'], vacansy['alternate_url'],
                                   vacansy['type']['id'])

        return list_vacansy


if __name__ == '__main__':
    emp_1 = HH('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
               {'text': '', 'page': 0, 'per_page': 100})

    emp_1.get_response('Python')

    print(Vacansy.make_objects(emp_1))
