import requests


class Parser:
    """
    Класс обработки вакансий, полученных из API запроса. Позволяет создать экземпляры класса вакансии.
    """
    def __init__(self, file_vacancies: list):
        self.file_vacancies = file_vacancies

    def get_pars(self):
        """
        Переделываем вывод данных для создания объектов класса вакансия и сохранения в json-файл
        """
        vacancies = []
        for item in self.file_vacancies:
            new_name = item["name"].replace('"', "'")
            if not item["salary"]:
                create_dict = {"name": new_name, "experience": item["experience"]["name"],
                               "salary_from": 0, "salary_to": 0,
                               "snippet": item["snippet"]["responsibility"], "url": item["alternate_url"]}
                vacancies.append(create_dict)
            elif not item["salary"]["from"]:
                create_dict = {"name": new_name, "experience": item["experience"]["name"],
                               "salary_from": 0, "salary_to": item["salary"]["to"],
                               "snippet": item["snippet"]["responsibility"], "url": item["alternate_url"]}
                vacancies.append(create_dict)
            elif not item["salary"]["to"]:
                create_dict = {"name": new_name, "experience": item["experience"]["name"],
                               "salary_from": item["salary"]["from"], "salary_to": 0,
                               "snippet": item["snippet"]["responsibility"], "url": item["alternate_url"]}
                vacancies.append(create_dict)
            else:
                create_dict = {"name": new_name, "experience": item["experience"]["name"],
                               "salary_from": item["salary"]["from"], "salary_to": item["salary"]["to"],
                               "snippet": item["snippet"]["responsibility"], "url": item["alternate_url"]}
                vacancies.append(create_dict)
        return vacancies


class HeadHunterAPI:
    """
    Класс для получения данных о вакансиях с сайта hh.ru
    :param Параметр для поиска: ключевое слово, количество вакансий в выводе(50), регион поиска(1575 - Пенза)
    """
    def __init__(self):
        self.url = "https://api.hh.ru/employers/"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 10, "sort_by": "by_vacancies_open"}
        self.employers = []

    def load_employers(self, word: str):
        self.params["text"] = word.lower()
        response = requests.get(self.url, headers=self.headers, params=self.params)
        self.employers.extend(response.json()["items"])
        for item in self.employers:
            print(item["name"], item["open_vacancies"], item["vacancies_url"])

        # return self.employers

        # self.params["text"] = word.lower()
        # response = requests.get(self.url, headers=self.headers, params=self.params)
        # self.vacancies.extend(response.json()["items"])
        # return self.vacancies
