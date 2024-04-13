from abc import ABC

class Parser(ABC):
    """Абстрактный класс для получения вакансий."""

    def __init__(self, url, headers, params):
        pass
    def get_response(self, keyword):
        pass

class AbsRedactor(ABC):
    def __init__(self):
        pass
    def _saver(self):
        pass
    def _loader(self):
        pass

    def _deleter(self):
        pass