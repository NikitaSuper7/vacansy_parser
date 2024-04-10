from src.vacansy import Vacansy
from src.hh import HH
from src.saver import Saver
import json


def user_interaction():
    """Осуществляет взаимодействие с пользователем."""
    search_request = input("Please enter your search request: ").split()
    how_many = int(input("Please enter  TOP N vacancies where 'N' is number vacancies amount: "))
    request_1 = HH()
    request_1.get_response(search_request)

    Vacansy.make_objects(request_1)
    Vacansy.sorter_salary()
    str_vacansy = Saver(Vacansy.all_vacancies)
    str_vacansy.json_saver()

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


if __name__ == '__main__':
    user_interaction()
