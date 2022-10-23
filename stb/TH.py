import sqlite3


class TableOperator(object):
    def __init__(self, table_name: str, file_name: str):
        self._table_name: str = table_name
        self._file_name: str = file_name

    def write(self, values: list | tuple):
        conn = sqlite3.connect(self._file_name)
        cur = conn.cursor()
        questions = "?"
        for x in range(len(values) - 1):
            questions += ", ?"
        try:
            cur.execute(f"insert or replace into {self._table_name} values({questions});", values)
            conn.commit()
        except sqlite3.OperationalError as e:
            print(f"Sorry, you have too many values than your table. T{str(e)[1:]}")
        conn.close()

    def read_a_row(self, column_name: str, key: str | int):
        if key.isnumeric():
            key = str(key)
        conn = sqlite3.connect(self._file_name)
        cur = conn.cursor()
        cur.execute(f'SELECT * from {self._table_name} WHERE {column_name} = ? ', (key,))
        result = cur.fetchone()
        return result

    def read_all(self):
        conn = sqlite3.connect(self._file_name)
        cur = conn.cursor()
        cur.execute(f'Select * from {self._table_name}')
        result = cur.fetchall()
        conn.close()
        return result
