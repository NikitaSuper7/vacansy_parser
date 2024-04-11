from src.hh import HH


class Vacansy:
    """Класс для работы с вакансиями"""
    all_vacancies: list

    def __init__(self, vac_id: str, name: str, description: str, salary: float, location: str, link: str,
                 vac_type: str):
        self.vac_id = vac_id
        self.name = name
        self.description = description
        self.salary = salary
        self.location = location
        self.link = link
        self.vac_type = vac_type

    def __salary_validator(self):
        """валидатор зарплаты"""
        if self.salary is None:
            self.salary = 0

    def __lt__(self, other):
        """Сравнивает зарплаты объектов"""
        return self.salary < other.salary

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"({self.vac_id}, {self.name}, {self.description}, {self.salary}, {self.location}, {self.link}, {self.vac_type})")

    @classmethod
    def _sorter_salary(cls):
        """Сортирует зарплаты по убыванию."""
        cls.all_vacancies.sort(reverse=True)
        return cls.all_vacancies

    @classmethod
    def _salary_range(cls, lst: list):
        """Отбирает зарплаты входящие в диапазон."""
        salary_from = int(lst[0])
        salary_to = int(lst[1])
        new_list = []
        for vacansy in cls.all_vacancies:
            # print(salary_from <= vacansy.salary <= salary_to)
            if salary_from <= vacansy.salary <= salary_to:
                new_list.append(vacansy)
        cls.all_vacancies = new_list
        return cls.all_vacancies

    # def __del__(self):
    #     print('object_deleted')

    @classmethod
    def _make_objects(cls, all_vacansies: HH):
        """Создает объекты класса."""
        list_vacansy = []
        for vacansy in all_vacansies.vacancies:
            name = f"{vacansy['id']}"
            list_vacansy.append(name)
            if vacansy['salary']:
                if vacansy['salary']['to']:
                    list_vacansy[-1] = cls(vacansy['id'], vacansy['name'], vacansy['snippet']['requirement'],
                                           vacansy['salary']['to'],
                                           vacansy['area']['name'], vacansy['alternate_url'],
                                           vacansy['type']['id'])
                else:
                    list_vacansy[-1] = cls(vacansy['id'], vacansy['name'], vacansy['snippet']['requirement'],
                                           vacansy['salary']['from'],
                                           vacansy['area']['name'], vacansy['alternate_url'],
                                           vacansy['type']['id'])
            else:
                list_vacansy[-1] = cls(vacansy['id'], vacansy['name'], vacansy['snippet']['requirement'],
                                       vacansy['salary'],
                                       vacansy['area']['name'], vacansy['alternate_url'],
                                       vacansy['type']['id'])
            list_vacansy[-1].__salary_validator()
            cls.all_vacancies = list_vacansy
        return cls.all_vacancies


# if __name__ == '__main__':
#     emp_1 = HH('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
#                {'text': '', 'page': 0, 'per_page': 100})
#
#     emp_1.get_response('Python, developer')
#     Vacansy._make_objects(emp_1)
#     Vacansy._sorter_salary()
#     Vacansy._salary_range([50000, 100_000])
#
#     for vacansy in Vacansy.all_vacancies:
#         print(vacansy.salary)
