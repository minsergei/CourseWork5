from typing import Any
import psycopg2
from configparser import ConfigParser
import os


def config(filename=os.path.abspath("database.ini"), section="postgresql"):
    """Функция для чтения конфигурационнага файла и возвращает его в виде словаря"""
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f"DROP DATABASE {database_name}")
    except Exception as e:
        print('Информация:', {e}, 'создадим ее')
    # else:
    # Исключений не произошло, БД дропнута
    finally:
        cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                employer_id SERIAL PRIMARY KEY,
                name_employer VARCHAR(255) NOT NULL,
                open_vacancies INTEGER,
                vacancies_url VARCHAR(255) NOT NULL
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                employer_id INT REFERENCES employers(employer_id),
                name_vacancy VARCHAR NOT NULL,
                experience VARCHAR,
                salary_from INTEGER,
                salary_to INTEGER,
                snippet TEXT,
                url_vacancy VARCHAR
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict):
    """Сохранение данных о работадателях и вакансиях в базу данных."""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for employer in data:

            cur.execute(
                """
                INSERT INTO employers (name_employer, open_vacancies, vacancies_url)
                VALUES (%s, %s, %s)
                RETURNING employer_id
                """,
                (employer['employer'][0], employer['employer'][1], employer['employer'][2]))
            employer_id = cur.fetchone()[0]
            vacancy_data = employer['vacancies']
            for vacancy in vacancy_data:
                cur.execute(
                    """
                    INSERT INTO vacancies (employer_id, name_vacancy, experience, salary_from, salary_to, snippet, url_vacancy)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (employer_id, vacancy['name'], vacancy['experience'], vacancy['salary_from'], vacancy['salary_to'],
                     vacancy['snippet'], vacancy['url'])
                )

    conn.commit()
    conn.close()
