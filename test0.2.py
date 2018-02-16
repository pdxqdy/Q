import sqlite3
import random
import string
from q import QSQLite
from q import Q
from q import T
from q import CharField
from q import IntegerField


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
        id = IntegerField()
        name = CharField()
        age = IntegerField()
        gender = IntegerField()
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

    users = User.select().where(User.name == 'sen').range(1).execute()
    user = users[0]
    print(user.id, user.name, user.age, user.phone)

    users = User.select().range(0, 10).execute()
    user = users[0]
    print(user.id, user.name, user.age, user.phone)

    users = User.select().order_by(User.age).execute()
    for user in users:
        print(user.id, user.name, user.age, user.phone)

    users = User.select(T.alias(T.count(User.age), 'count'), User.age).group_by(User.age).execute()
    for user in users:
        print(user.age, user.count)
