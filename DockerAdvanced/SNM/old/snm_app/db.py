import mysql.connector


class DB:

    def __init__(self):
        db_conn = mysql.connector.connect(
            host="localhost",
            user="snm",
            password="snm1234"
        )
        print(db_conn)
