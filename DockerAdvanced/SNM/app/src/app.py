from flask import Flask,request
import socket
from db import DB

app = Flask(__name__)
mysqldb = DB()

@app.route('/')
def hello():
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    return f"Hello Cruel World {hostname} - {ipaddr}"

@app.route('/users')
def get_users():
    return mysqldb.get_users()


@app.route('/user')
def get_user():
    id = request.args.get('id')
    print("ID is ", id)
    return mysqldb.get_user_by_id(id)

if __name__ == '__main__':
    app.run()
