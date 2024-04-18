import json


class Vacancy:
    vacancy_list = []

    def __init__(self, name: str, experience: str, salary_from: int, salary_to: int, snippet: str, url: str):
        self.__name = name
        self.experience = experience
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.snippet = snippet
        self.url = url

    def __repr__(self):
        """
        :return: Возвращает словарь для инициализации объекта
        """
        dict_vacancy = (f'"name": "{self.get_name}", "experience": "{self.experience}", '
                        f'"salary_from": {self.salary_from}, '
                        f'"salary_to": {self.salary_to}, "snippet": "{self.snippet}", "url": "{self.url}"')
        return '{' + dict_vacancy + '}'

    def __str__(self):
        """
        Описание объекта вакансии
        """
        return (f"\nВакансия: {self.get_name}\nЗарплата: {self.salary_from} руб. - {self.salary_to} руб.\n"
                f"Опыт работы: {self.experience}\nОписание: {self.snippet}")

    def __lt__(self, other):
        """
        Магические методы для сравнение и сортировки объктов по зарплате
        """
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from < other.salary_from
            else:
                return self.salary_from < other.salary_to
        elif other.salary_from > 0:
            return self.salary_to < other.salary_from
        else:
            return self.salary_to < other.salary_to

    def __le__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from <= other.salary_from
            else:
                return self.salary_from <= other.salary_to
        elif other.salary_from > 0:
            return self.salary_to <= other.salary_from
        else:
            return self.salary_to <= other.salary_to

    def __gt__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from > other.salary_from
            else:
                return self.salary_from > other.salary_to
        elif other.salary_from > 0:
            return self.salary_to > other.salary_from
        else:
            return self.salary_to > other.salary_to

    def __ge__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from >= other.salary_from
            else:
                return self.salary_from >= other.salary_to
        elif other.salary_from > 0:
            return self.salary_to >= other.salary_from
        else:
            return self.salary_to >= other.salary_to

    def __eq__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from == other.salary_from
            else:
                return self.salary_from == other.salary_to
        elif other.salary_from > 0:
            return self.salary_to == other.salary_from
        else:
            return self.salary_to == other.salary_to

    def __ne__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from != other.salary_from
            else:
                return self.salary_from != other.salary_to
        elif other.salary_from > 0:
            return self.salary_to != other.salary_from
        else:
            return self.salary_to != other.salary_to

    @property
    def get_name(self):
        return self.__name

    @classmethod
    def cast_to_object_list(cls, vacancy_json):
        """
        Класс-метод для создания экземпляров вакансий из файла json и добавления в общий список
        :param vacancy_json:
        :return:
        """
        for item in vacancy_json:
            vacancy = cls(item["name"], item["experience"], item["salary_from"], item["salary_to"],
                          item["snippet"], item["url"])
            Vacancy.vacancy_list.append(vacancy)

    @staticmethod
    def get_top(top: int):
        """
        Выводит топ вакансий по зарплате и передает данные для записи в json файл
        """
        sorted_vacancy = sorted(Vacancy.vacancy_list, reverse=True)
        top = (sorted_vacancy[:top])
        [print(i) for i in top]
        return json.loads(repr(top))
