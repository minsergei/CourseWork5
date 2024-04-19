import requests


# vacancies = []
# response = requests.get("https://api.hh.ru/employers/", headers={"User-Agent": "HH-User-Agent"}, params={"text": "продажа", "page": 0, "per_page": 10, "sort_by": "by_vacancies_open"})
# vacancies.append(response.json()["items"])
# print(vacancies)
#
#
# https://api.hh.ru/vacancies?employer_id=880927    https://api.hh.ru/vacancies?employer_id=9498112


# vacancies = []
# response = requests.get("https://api.hh.ru/vacancies/", headers={"User-Agent": "HH-User-Agent"}, params={"employer_id": ["880927", "10063965"], "page": 0, "per_page": 10})
# vacancies.append(response.json()["items"])
# print(vacancies)

vacancies = []
response = requests.get("https://api.hh.ru/vacancies?employer_id=9498112", headers={"User-Agent": "HH-User-Agent"}, params={"page": 0, "per_page": 10})
vacancies.append(response.json()["items"])
print(vacancies)
