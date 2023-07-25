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
    cur.execute("INSERT INTO income (user_id, income, data) VALUES (?, ?, ?)", value)
    connection.commit()


def _print_expenses_mount(mount: str) -> list:  # вывод расходов за текущий месяц

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    cur.execute(f"SELECT users.name_user, sum(expenses.expenses) AS exp "
                f"from expenses JOIN users on users.user_id == expenses.user_id "
                f"GROUP BY expenses.user_id, strftime('%m', expenses.data)"
                f"HAVING strftime('%m', expenses.data) == '{mount}'")
    result = cur.fetchall()
    return result


def _print_expenses_year(year: str) -> list:  # вывод расходов за текущий год

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    cur.execute(f"SELECT users.name_user, sum(expenses.expenses) AS exp, strftime('%m', expenses.data) AS mount "
                f"from expenses JOIN users on users.user_id == expenses.user_id "
                f"GROUP BY expenses.user_id, strftime('%m', expenses.data), strftime('%Y', expenses.data) "
                f"HAVING strftime('%Y', expenses.data) == '{year}'")
    result = cur.fetchall()
    return result


def _print_expenses_detail_mount(user: str, mount: str) -> list:  # вывод детальной информации о расходах за текущий месяц

    connection = sqlite3.connect('finanse.db')
    cur = connection.cursor()
    cur.execute(f"SELECT users.name_user, expenses.name_category, sum(expenses.expenses) AS exp "
                f"from expenses JOIN users on users.user_id == expenses.user_id "
                f"GROUP BY strftime('%m', expenses.data), expenses.name_category, expenses.user_id "
                f"HAVING strftime('%m', expenses.data) == '{mount}' AND expenses.user_id == '{user}' "
                f"ORDER BY exp DESC")
    result = cur.fetchall()
    return result


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

    @staticmethod
    def print_expenses():
        return _print_expenses_mount

    @staticmethod
    def print_year_expenses():
        return _print_expenses_year

    @staticmethod
    def print_detail_expenses():
        return _print_expenses_detail_mount


crud = CRUDInteface()
