from config import auth
from sqlalchemy import create_engine


engine = create_engine('postgresql://{}:{}@localhost/sqlachemy_db'.format(auth['user'], auth['password']), echo=True)

cursor = engine.connect()

query = '''
select *
from authors
where id >=2
'''
query = """
select create_db_proc('MY_NEW_BD')
"""

query2 = '''
insert into authors
values (1323 , 'ewqe') , (1211131 ,'piasdkabu')
'''

# query = """
# CREATE TABLE authors(
# id serial PRIMARY KEY,
# name text
# );
# """
result = cursor.execute(query)
print(result)
print(list(result))
