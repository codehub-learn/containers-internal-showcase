import time
import os
import redis
from flask import Flask

app = Flask(__name__)

redis_host = os.environ['REDIS_HOST']
cache = redis.Redis(host=redis_host, port=6379)
def get_hits():
    retries = 5
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
    count = get_hits()
    return "You reached this page {} times\n".format(count)
