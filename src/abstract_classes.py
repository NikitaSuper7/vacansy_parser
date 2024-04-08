from abc import ABC

class Parser(ABC):
    """Абстрактный класс для получения вакансий."""

    def __init__(self, url, headers, params):
        pass
    def get_response(self, keyword):
        pass