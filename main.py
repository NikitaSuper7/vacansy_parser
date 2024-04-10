from src.vacansy import Vacansy
from src.hh import HH
from src.saver import Saver
from src.abstract_classes import Parser
import requests


def user_interaction():
    """Осуществляет взаимодействие с пользователем."""
    search_request = input("Please enter your search request: ").strip()
    how_many = int(input("Please enter  TOP N vacancies where 'N' is number vacancies amount: "))
    request_1 = HH()
    request_1.get_response(search_request)

    Vacansy.make_objects(request_1)
    Vacansy.sorter_salary()
    str_vacansy = Saver(Vacansy.all_vacancies)
    str_vacansy.json_saver()
    str_vacansy.json_loader(how_many=how_many)


if __name__ == '__main__':
    user_interaction()
