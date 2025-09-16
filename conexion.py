import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='tu_password',
        database='desarrollo_web'
    )
    return connection
