from flask import Flask, request, jsonify
from flask_restful import Resource,Api,reqparse,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///" + os.path.join(basedir,"database.db")

db=SQLAlchemy(app)

Migrate(app,db)

api=Api(app)

class UserModel(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),nullable=False)
    age=db.Column(db.Integer,nullable=False)

    def tojson(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age
        }

usermarshal = {
        "id": fields.Integer,
        "name": fields.String,
        "age": fields.String
    }

parser=reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help="Name cannot be empty")
parser.add_argument('age',type=int,required=True,help="Age cannot be empty")

class Users(Resource):

    @marshal_with(usermarshal)
    def get(self):

        user=UserModel.query.all()
        return user

    def post(self):

        args=parser.parse_args()
        user=UserModel(name=args['name'],age=args['age'])
        db.session.add(user)
        db.session.commit()

        user=UserModel.query.all()
        return jsonify([u.tojson() for u in user])


api.add_resource(Users,"/hello")

@app.route("/")
def home():
    return "<h1> Welcome to home page <h1>"

app.run()
