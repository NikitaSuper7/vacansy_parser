from abc import ABC

class Parser(ABC):
    """Абстрактный класс для получения вакансий."""

    def __init__(self, url, headers, params):
        pass
    def get_response(self, keyword):
        pass

class AbsVacansy(ABC):
    def __init__(self):
        pass
    def json_saver(self):
        pass
    def json_load(self):
        pass

    def del_vacansy(self):
        pass