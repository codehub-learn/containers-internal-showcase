import os
import mysql.connector


class DB:

    def __init__(self):
        self.db_host = os.getenv('DB_HOST')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('DB_NAME')
        self.db_conn = None

    def connect(self):
        self.db_conn = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name
        )

    def get_users(self):
        self.connect()
        cursor = self.db_conn.cursor()
        query = ("select id,name,surname,friends,home_page from users")
        cursor.execute(query)
        response = ""
        for (id,name,surname,friends,home_page) in cursor:
            response = response + f"{id} {name} {surname} {friends} {home_page}\n"
        cursor.close()
        return response

    def get_user_by_id(self, id):
        self.connect()
        cursor = self.db_conn.cursor()
        query = ("select id,name,surname,friends,home_page from users where id = %s")
        cursor.execute(query, [id])
        response = ""
        for (id,name,surname,friends,home_page) in cursor:
            response = response + f"{id} {name} {surname} {friends} {home_page}\n"
        cursor.close()
        return response


