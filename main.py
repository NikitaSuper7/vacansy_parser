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
    save_vac = Saver(Vacansy.sorter_salary())
    save_vac.json_saver()

    with open('src/vacansies.json', 'r', encoding='utf-8') as file:
        respond = json.load(file)
        respond = respond[0:how_many]

    print(respond, len(respond), sep='\n')
    return respond


if __name__ == '__main__':
    user_interaction()
