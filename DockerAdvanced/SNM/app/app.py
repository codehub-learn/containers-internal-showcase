from flask import Flask
from db import DB

app = Flask(__name__)



@app.route('/')
def hello():
    return "Hello snm"

@app.route('/testdb')
def start_db():
    mysqldb = DB()
    return mysqldb.get_users()

if __name__ == '__main__':
    app.run()
