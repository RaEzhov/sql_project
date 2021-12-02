-- Подключаем расширение dblink (однажды подключил - используется всегда)
CREATE EXTENSION dblink;


-- функция создания БД с заданым именем
CREATE OR REPLACE FUNCTION f_create_db(dbname text)
  RETURNS integer AS
$func$
BEGIN
-- проверка на существование БД с таким же именем
IF EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
   -- Возвращаем сообщение (не ошибку)
   RAISE NOTICE 'Database already exists'; 
ELSE
   -- выполняем SQL запрос на создание БД. оператор || - конкатенация
   -- current_database() - возврашает название БД в которой сейчас выполняется транзакция
   -- принцип работы dblink_exec: подключается к указанной бд(в примере - текущая), и выполняет запрос, 
   -- переданный вторым аргументом.
   -- для доп.информации можно добавить hostaddr=127.0.0.1 port=5432 dbname=mydb user=postgres password=mypasswd
   PERFORM dblink_exec('dbname=' || current_database()   -- current db
                     , 'CREATE DATABASE ' || quote_ident(dbname));
END IF;

END
$func$ LANGUAGE plpgsql;

