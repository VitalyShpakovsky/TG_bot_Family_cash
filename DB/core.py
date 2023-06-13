import sqlite3


def _new_create_database() -> None:  # Создается база данных

    # Создаем базу данных

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    print('Database created')

    # Создаем таблицу users

    cur.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_user TEXT, user_id INTEGER)""")
    connection.commit()
    print('Table created')


    # Создаем таблицу expenses

    cur.execute("""CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, 
    name_category TEXT, expenses REAL, data TEXT)""")
    connection.commit()
    print('Table created')

    # Создаем таблицу income

    cur.execute("""CREATE TABLE IF NOT EXISTS income(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INT, income TEXT, data TEXT)""")
    connection.commit()
    print('Table created')


def _add_user_table(value: tuple) -> None:  # добавление данных в таблицу users

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO users (name_user, user_id) VALUES (?, ?)", value)
    connection.commit()



def _add_expenses(value: tuple) -> None:  # добавление данных в таблицу expenses

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO expenses (user_id, name_category, expenses, data) VALUES (?, ?, ?, ?)", value)
    connection.commit()


def _add_income(value: tuple) -> None:  # добавление данных в таблицу income

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO income (name_user, income, data) VALUES (?, ?, ?)", value)
    connection.commit()


# def _write_value_country() -> list:  # функция вывода списка всех городов в отсортированном порядке по алфавиту
#     connection = sqlite3.connect('diploma.db')
#     cur = connection.cursor()
#     cur.execute(f"SELECT name_city from city ORDER BY name_city")
#     result = cur.fetchall()
#     return result
#
#
# def _write_value_city(city: str) -> list:  # функция вывода конкретного города
#     connection = sqlite3.connect('diploma.db')
#     cur = connection.cursor()
#     cur.execute(f"SELECT name_city from city WHERE name_city = '{city}'")
#     result = cur.fetchall()
#     return result
#
#
# def _write_value_compression() -> list:   # функция вывода городов и стран имеющихся в базе данных (2 значения)
#     connection = sqlite3.connect('diploma.db')
#     cur = connection.cursor()
#     cur.execute(f"SELECT name_city, name_country from city")
#     result = cur.fetchall()
#     return result
#
#
# def _delete_table() -> None:  # функция удаления таблицы city
#     connection = sqlite3.connect('diploma.db')
#     cur = connection.cursor()
#     cur.execute("DELETE FROM city")
#     connection.commit()
#
#
# def _add_history(*args) -> None:  # функция записи данных в таблицу history
#     connection = sqlite3.connect('diploma.db')
#     cur = connection.cursor()
#     cur.execute(f"INSERT INTO history(command, country, city, data) "
#                 f"VALUES ('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}')")
#     connection.commit()
#
#
# def _read_history(limit: int = 10) -> list:  # функция вывода данных из таблицы history
#     connection = sqlite3.connect('diploma.db')
#     cur = connection.cursor()
#     cur.execute(f"SELECT command, country, city, data from history ORDER BY id_history DESC LIMIT {limit}")
#     result = cur.fetchall()
#     return result


class CRUDInteface:
    @staticmethod
    def create():
        return _new_create_database

    @staticmethod
    def ad_user():
        return _add_user_table

    @staticmethod
    def ad_expenses():
        return _add_expenses

    @staticmethod
    def ad_income():
        return _add_income


crud = CRUDInteface()