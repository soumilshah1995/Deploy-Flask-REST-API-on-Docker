from flask import Flask
from flask_restful import Resource, Api
import sys
import os

app = Flask(__name__)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("You said port is : {} ".format(port))

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world Port : {} '.format(port)}

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)