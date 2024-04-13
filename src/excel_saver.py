import pandas as pd
from src.abstract_classes import AbsRedactor
from src.hh import HH
from src.vacansy import Vacansy
from pandas.io.excel import ExcelWriter as ew
# from pandas.io.excel import _openpy



class ExcelSaver(AbsRedactor):
    """Класс для форматирования вакансий в Excel объекты."""

    def __init__(self, all_vacansy: list):
        """Получает на вход лист с объектами класса вакансий и инициализирует их."""
        self.all_vacansy = all_vacansy

    def _saver(self):
        """Сохраняет экземпляры класса Vacansy в excel файл."""
        data_frame = pd.DataFrame(columns=['vac_id', 'name', 'description', 'salary', 'location', 'link', 'type'])

        for vacansy in self.all_vacansy:
            vacansy = [vacansy.vac_id, vacansy.name, vacansy.description, vacansy.salary, vacansy.location,
                       vacansy.link, vacansy.vac_type]
            # pd.concat([data_frame, pd.DataFrame(vacansy)])
            data_frame.loc[len(data_frame)] = vacansy

        data_frame.to_excel('vacansy.xlsx', index=False, sheet_name='vacasies')
        # with ew('ext_came_back_test.xlsx') as writer:
        #     data_frame.to_excel(writer, sheet_name='data', startrow=1, startcol=1)


        return data_frame

    def _loader(self, file):
        """Выгружает excel file"""
        df = pd.read_excel(file)
        return df

    def _deleter(self, file, vac_id: int):
        """удаляет вакансию из файла"""
        new_df = self._loader(file)
        new_df = new_df.loc[new_df['vac_id'] != vac_id]
        new_df.to_excel('new_df.xlsx', index=False)




if __name__ == '__main__':
    emp_1 = HH('https://api.hh.ru/vacancies', {'User-Agent': 'HH-User-Agent'},
               {'text': '', 'page': 0, 'per_page': 100})

    emp_1.get_response('Python, developer')
    Vacansy._make_objects(emp_1)
    Vacansy._sorter_salary()
    Vacansy._salary_range([50_000, 100_000])
    excel_1 = ExcelSaver(Vacansy.all_vacancies)
    excel_1._saver().head()
    excel_1._deleter('vacansy.xlsx', vac_id=95150405)
