from src.parser_hh import HeadHunterAPI, Parser


def user_interaction():
    # Получаем вакансии с hh.ru. Изменяем данные под структуру !!!! и для создания объектов класса вакансии
    hh = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    print(hh.load_employers(search_query))
    # pars_hh = Parser(hh.load_employers(search_query))
    # list_vacancies = pars_hh.get_pars()

if __name__ == "__main__":
    user_interaction()
