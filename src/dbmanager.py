import psycopg2


class DBManager:
    def __init__(self, database_name: str, params: dict):
        self.database_name = database_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT name_employer, open_vacancies FROM employers")
        result = cur.fetchall()
        conn.close()
        return result

    def get_all_vacancies(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT employers.name_employer, name_vacancy, CONCAT('от ', salary_from, ' до ', salary_to) "
                    "AS salary FROM vacancies JOIN employers USING(employer_id)")
        result = cur.fetchall()
        conn.close()
        return result

    def get_avg_salary(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT round(AVG((salary_from+salary_to)/2),2) FROM vacancies")
        result = cur.fetchall()
        conn.close()
        return result

    def get_vacancies_with_higher_salary(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT employers.name_employer, name_vacancy, salary_from+salary_to/2 AS salary "
                    "FROM vacancies	JOIN employers USING(employer_id) WHERE (salary_from+salary_to)/2 > "
                    "(SELECT AVG((salary_from+salary_to)/2) FROM vacancies) ORDER BY salary")
        result = cur.fetchall()
        conn.close()
        return result

    def get_vacancies_with_keyword(self, word):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT employers.name_employer, name_vacancy, salary_from+salary_to/2 AS salary FROM vacancies	JOIN employers USING(employer_id) WHERE name_vacancy LIKE '%кадр%'")
        result = cur.fetchall()
        conn.close()
        return result
