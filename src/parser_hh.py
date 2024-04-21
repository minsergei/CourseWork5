import math

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
    Класс для получения данных о работадателях и вакансиях с сайта hh.ru
    :param Параметр для поиска: ключевое слово, количество вакансий в выводе(50), сортировка по кол-ву вакансий
    количество страниц, количество выводимых результатов на странице
    """
    def __init__(self):
        self.url = "https://api.hh.ru/employers/"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params_employers = {"text": "", "page": 0, "per_page": 5, "sort_by": "by_vacancies_open"}
        self.params_vacancies = {"page": 0, "per_page": 20}
        self.employers = []
        self.employer_vacancies = []

    def load_employers(self, word: str):
        self.params_employers["text"] = word.lower()
        response = requests.get(self.url, headers=self.headers, params=self.params_employers)
        self.employers.extend(response.json()["items"])

        for item in self.employers:
            vacancies = []
            employer = (item["name"], item["open_vacancies"], item["vacancies_url"])
            print(employer)
            #определяем количество страниц, выставляю 10 максимум
            count_page = math.ceil(int(item["open_vacancies"])/20)
            if count_page > 10:
                count_page = 10

            while self.params_vacancies["page"] != count_page:
                response_vacancies = requests.get(item["vacancies_url"], headers=self.headers,
                                                  params=self.params_vacancies)
                self.params_vacancies["page"] += 1
                pars_hh = Parser(response_vacancies.json()["items"])
                vacancies.extend(pars_hh.get_pars())
            self.employer_vacancies.append({'employer': employer, 'vacancies': vacancies})
            self.params_vacancies["page"] = 0
        return self.employer_vacancies
