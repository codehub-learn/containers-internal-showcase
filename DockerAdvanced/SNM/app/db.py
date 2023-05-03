import mysql.connector
class DB:

    def __init__(self):
        self.db_conn = mysql.connector.connect(
            host="172.17.0.3",
            user="snm",
            password="snm1234",
            database="snm"
        )

    def get_users(self):
        cursor = self.db_conn.cursor()
        query = ("select id,name,surname,friends,home_page from users")
        cursor.execute(query)
        response = ""
        for (id,name,surname,friends,home_page) in cursor:
            response = response + f"{id} {name} {surname} {friends} {home_page}\n"
        cursor.close()
        return response

