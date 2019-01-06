from flask import Flask
from flask_restful import Api, Resource, reqparse
# from resources.user import User

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200


api.add_resource(HelloWorld, "/")
# api.add_resource(User, "/user/<string:name>")

if __name__ == '__main__':
    app.run()
