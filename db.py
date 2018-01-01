import sqlite3


class QDataBase(object):
    def _connent(self, *args):
        return NotImplemented

    def _execute_sql(self, sql):
        return NotImplemented


class QSQLite(QDataBase):
    def __init__(self, name):
        self.name = name

    def _connent(self):
        conn = sqlite3.connect(self.name)
        return conn

    def _execute_sql(self, sql):
        print('QSQLite execute sql: {}'.format(sql))
        conn = self._connent()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = [m for m in cursor]
        conn.commit()
        conn.close()
        return data

    def execute_sql(self, sql):
        return self._execute_sql(sql)
