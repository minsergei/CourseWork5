import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, data):
        pass


class JsonSaver(Saver):
    def __init__(self, file_json, mode="r"):
        self.file_json = file_json
        self.mode = mode

    def add_vacancy(self, data):
        """
        Функция добавления данных о вакансии в файл json
        """
        with open(self.file_json, self.mode) as outfile:
            if os.stat(self.file_json).st_size == 0:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
            else:
                load_outfile = json.load(outfile)
                outfile.seek(0)
                [load_outfile.append(item) for item in data]
                json.dump(load_outfile, outfile, ensure_ascii=False, indent=4)

    def delete_vacancy(self, name: str):
        """
        Удаляем вакансию по названию вакансии
        """
        with open(self.file_json, self.mode) as outfile:
            if not os.stat(self.file_json).st_size == 0:
                text = json.load(outfile)
                new_len = []
                for i in range(len(text)):
                    if text[i]['name'] == name:
                        new_len.append(i)
                new_len2 = new_len[::-1]
                for i in new_len2:
                    del text[i]
            else:
                print("Файл не содержит вакансий")
        with open(self.file_json, "w") as outfile:
            json.dump(text, outfile, ensure_ascii=False, indent=4)

    def read_file(self):
        """
        Получаем вакансии из json файла
        """
        with open(self.file_json, "r") as outfile:
            text = json.load(outfile)
        return text


# Получаем путь до json файла
path_json = os.path.abspath('../data/vacancies.json')
# Создаем экземпляр класса
save_file = JsonSaver(path_json, "r+")
# Сохраняем вакансии
# save_file.add_vacancy(rate)
# save_file.delete_vacancy("Преподаватель робототехники | программирования")
