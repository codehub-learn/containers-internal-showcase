from flask import Flask
from db import DB


app = Flask(__name__)

database = DB()


@app.route('/')
def get_name():  # put application's code here
    return "snm"


if __name__ == '__main__':
    app.run()
