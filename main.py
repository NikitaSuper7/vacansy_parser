from src.vacansy import Vacansy
from src.hh import HH
from src.saver import JsonSaver



def user_interaction():
    """Осуществляет взаимодействие с пользователем."""
    search_request = input("Please enter your search request: ").strip()
    how_many = int(input("Please enter  TOP N vacancies where 'N' is number vacancies amount: "))
    salary_range = input("Please enter a salary range in format 'from-to': ").strip().split(sep='-')
    request_1 = HH()
    request_1.get_response(search_request)

    Vacansy._make_objects(request_1)
    Vacansy._sorter_salary()
    Vacansy._salary_range(salary_range)
    str_vacansy = JsonSaver(Vacansy.all_vacancies)
    str_vacansy.json_saver()
    str_vacansy.json_loader(how_many=how_many)


if __name__ == '__main__':
    user_interaction()
