from q import Q
from q import IntegerField
from q import CharField
from q import T
from q import _join_string


if __name__ == '__main__':
    class User(Q):
        __tablename__ = 'user'
        name = CharField()
        age = IntegerField()
        gender = CharField()
        phone = CharField()


    form = dict(
        name='sen',
        age=18,
    )

    sqls = [
        {
            'comment': 'User.select().generate_sql()',
            'sql': User.select().generate_sql(),
        },
        {
            'comment': 'User.select(User.name).generate_sql()',
            'sql': User.select(User.name).generate_sql(),
        },
        {
            'comment': 'User.select(User.name, User.age).generate_sql()',
            'sql': User.select(User.name, User.age).generate_sql(),
        },
        {
            'comment': "User.select(User.name, User.age).where(User.phone == '136********').generate_sql()",
            'sql': User.select(User.name, User.age).where(User.phone == '136********').generate_sql(),
        },
        {
            'comment': "User.select(User.name, User.age).where((User.gender == '男') & (User.age >= 18)).generate_sql()",
            'sql': User.select(User.name, User.age).where((User.gender == '男') & (User.age >= 18)).generate_sql(),
        },
        {
            'comment': 'User.select(T.count(User.name)).generate_sql()',
            'sql': User.select(T.count(User.name)).generate_sql(),
        },
        {
            'comment': 'User.select(T.distinct(User.name)).generate_sql()',
            'sql': User.select(T.distinct(User.name)).generate_sql(),
        },
        {
            'comment': 'User.select(T.max(User.age), T.distinct(User.name)).generate_sql()',
            'sql': User.select(T.max(User.age), T.distinct(User.name)).generate_sql(),
        },
        {
            'comment': 'User.new(form).generate_sql()',
            'sql': User.new(form).generate_sql(),
        },
        {
            'comment': 'User.select(T.max(User.age), T.distinct(User.name)).generate_sql()',
            'sql': User.select(T.max(User.age), T.distinct(User.name)).generate_sql(),
        },
        {
            'comment': "User.update(form).where(User.name != '森').generate_sql()",
            'sql': User.update(form).where(User.name != '森').generate_sql(),
        },
        {
            'comment': "User.delete().where(User.name != '森').generate_sql()",
            'sql': User.delete().where(User.name != '森').generate_sql(),
        },
        {
            'comment': "User.select(T.alias(T.max(User.age), 'max_age'), T.distinct(User.name)).generate_sql()",
            'sql': User.select(T.alias(T.max(User.age), 'max_age'), T.distinct(User.name)).generate_sql(),
        },
        {
            'comment': "User.select(T.alias(User.name, 'user_name')).generate_sql()",
            'sql': User.select(T.alias(User.name, 'user_name')).generate_sql(),
        },
    ]

    template_print = '''
    {comment}
    >>>
    {sql}
    '''
    sqls = map(lambda v: template_print.format(**v), sqls)
    s = _join_string(sqls, glue='\n')

    template = '''
    class User(Queryable):
        __tablename__ = 'user'
        name = CharField()
        age = IntergerField()
        gender = CharField()
        phone = CharField()

    form = dict(
        name='sen',
        age=18,
    )

    {}
    '''.format(s)
    print(template)
