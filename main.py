"""Small example of connecting to an MSSQL DB using a Lambda on Linux"""

from os import environ

from pymssql import connect
from dotenv import load_dotenv

def handler(event=None, context=None):

    conn = connect(
        server=environ["DB_HOST"],
        port=environ["DB_PORT"],
        user=environ["DB_USER"],
        password=environ["DB_PASSWORD"],
        database=environ["DB_NAME"],
        as_dict=True
    )

    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE general.example;")
        cur.executemany("INSERT INTO general.example (word) VALUES (%s);", ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
        cur.execute("SELECT TOP 8 * FROM general.example;")
        data = cur.fetchall()
    conn.commit()

    return data

if __name__ == "__main__":

    load_dotenv()

    handler()