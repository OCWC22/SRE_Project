from flask import Flask, request, make_response, g
from redis import Redis
import os

import json


REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_DB = os.getenv("REDIS_DB", 0)

app = Flask(__name__)

def get_redis():
    if not hasattr(g, "redis"):
        g.redis = Redis(host=REDIS_HOST, db=REDIS_DB, socket_timeout=5)
    return g.redis

@app.route("/<key>", methods=["GET"])
def home(key):
    if not key:
        return make_response("Key not supplied", 500)
    try:
        redis = get_redis()
        result = redis.get(key)
        if not result:
            return make_response("Key not found", 404)
        return result
    except Exception as e:
        return make_response(f"Error: {str(e)}", 500)

@app.route("/", methods=["POST"])
def post_data():
    try:
        redis = get_redis()
        payload = request.json
        redis.set(payload["key"], payload["value"])
        return make_response(f"Data saved Successfully", 200)
    except Exception as e:
        return make_response(f"Error: {str(e)}", 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True, threaded=True)

