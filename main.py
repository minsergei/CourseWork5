from src.parser_hh import HeadHunterAPI
from src.func import create_database, config, save_data_to_database
from src.dbmanager import DBManager
import os.path


def user_interaction():
    # Получаем вакансии с hh.ru. Изменяем данные под структуру !!!! и для создания объектов класса вакансии
    # hh = HeadHunterAPI()
    # search_query = input("Введите поисковый запрос: ")
    # data_hh_api = hh.load_employers(search_query)
    # create_database('hh_vacancy', config())
    # save_data_to_database(data_hh_api, 'hh_vacancy', config())
    db = config(os.path.abspath('database.ini'))
    hh = DBManager('hh_vacancy', db)
    # for i in (hh.get_companies_and_vacancies_count()):
    #     print(i)
    print(len(hh.get_all_vacancies()))
    print(hh.get_avg_salary()[0][0])
    print(len(hh.get_vacancies_with_higher_salary()))
    print(hh.get_vacancies_with_keyword('кадр'))



if __name__ == "__main__":
    user_interaction()
