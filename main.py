from flask import Flask
from flask_restful import Api, Resource
import random
import os
import time
tortl_list = os.listdir("/var/www/example.com/tortls")
app = Flask(__name__)
api = Api(app)
class RandomTortl(Resource):
  def get(self):
    return {"image": f"http://bogdikon.ru/tortls/{random.choice(tortl_list)}", "timestamp": int(time.time())}
class MakeMeACoffee(Resource):
  def get(self):
    return "I am a teapot!", 418
  def post(self):
    return "I am a teapot!", 418
api.add_resource(RandomTortl, "/api/randomtortl")
api.add_resource(MakeMeACoffee, "/api/makemeacoffee")
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
