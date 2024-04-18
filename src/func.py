def get_filter_vacancies(data, keys_word: list):
    """
    Функция отбирает вакансии по ключевым словам в описании вакансии
    """
    filtered_vacancies = []
    for item in data:
        if item["snippet"]:
            for item2 in keys_word:
                if item2.lower() in item["snippet"].lower():
                    filtered_vacancies.append(item)
                    break
    return filtered_vacancies


def get_ranged_vacancies(data, sal_range: str):
    """
    Функция выбирает вакансии, которые попадают в диапазон зарплат указанные пользователем
    """
    list_ranged_vacancies = []
    str_sal_range = ''
    for c in sal_range:
        if c.isdigit():
            str_sal_range += c
        else:
            str_sal_range += " "
    salary = str_sal_range.split()
    if len(salary) != 2 or int(salary[0]) > int(salary[1]):
        raise TypeError("Введен не верный диапозон зарплат")
    else:
        for item in data:
            if (((item["salary_from"] <= int(salary[0]) <= item["salary_to"] or
                  item["salary_from"] <= int(salary[1]) <= item["salary_to"]) or
                 int(salary[0]) <= item["salary_from"] <= int(salary[1])) or
                    int(salary[0]) <= item["salary_to"] <= int(salary[1])):
                list_ranged_vacancies.append(item)
        return list_ranged_vacancies
