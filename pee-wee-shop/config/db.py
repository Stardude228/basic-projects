from peewee import PostgresqlDatabase

postgres_db = PostgresqlDatabase(
    database="peewee_shop",
    user="hello",
    password="1",
    host="localHost",
    port="5432"
)