import sqlite3
import random
import string
from db import QSQLite
from q import Q
from q import T
from q import CharField
from q import IntergerField


def log(models):
    for m in models:
        print(m)


if __name__ == '__main__':
    sql = '''
        CREATE TABLE user
          (
             id     INTEGER PRIMARY KEY AUTOINCREMENT,
             name   CHAR(50) NOT NULL,
             age    INT NOT NULL,
             gender INT,
             phone  CHAR(50)
          );
    '''
    try:
        QSQLite('test.db').execute_sql(sql)
    except sqlite3.OperationalError:
        print('user表已经创建')


    class User(Q):
        __tablename__ = 'user'
        id = IntergerField()
        name = CharField()
        age = IntergerField()
        gender = CharField()
        phone = CharField()


    for n in range(10):
        name = ''.join(random.sample(string.ascii_letters, 4))
        form = dict(
            name=name,
            age=random.randint(10, 30),
            gender=random.randint(0, 2),
        )
        User.new(form).execute()

    users = User.select(User.age).where(User.name == 'sen').execute()
    log(users)

    users = User.select().where(User.id == 1).execute()
    log(users)

    User.update({'name': 'sen'}).where(User.id == 2).execute()
    users = User.select(User.name).where(User.id == 2).execute()
    log(users)

    users = User.select(T.max(User.age)).execute()
    log(users)

    users = User.select(T.distinct(User.age)).execute()
    log(users)
