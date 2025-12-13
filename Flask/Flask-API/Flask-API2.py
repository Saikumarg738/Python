from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)

api=Api(app)

class Hello(Resource):

    def get(self):
        return {"Handsome":"Sai"}

    def post(self):
        return {"Lucky":"Sai's wife"}

api.add_resource(Hello,"/")

app.run()