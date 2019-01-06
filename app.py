from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    }
]

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "user not found", 404

api.add_resource(HelloWorld, "/")
api.add_resource(User, "/user/<string:name>")

if __name__ == '__main__':
    app.run()
