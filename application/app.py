import time
import os
import redis
import socket
from flask import Flask

app = Flask(__name__)

redis_host = os.environ['REDIS_HOST']
cache = redis.Redis(host=redis_host, port=6379)
def get_hits():
    retries = 2
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    host = socket.gethostname()
    count = get_hits()
    return "You reached me: {} so far: {} times\n".format(host, count)
