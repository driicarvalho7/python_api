import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="Dev123"
    )
    return connection
