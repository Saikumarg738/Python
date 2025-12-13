from flask import Flask, jsonify,request
from flask_restful import Resource,Api,reqparse,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from flask_migrate import Migrate
import os

basedir=os.path.dirname(__file__)

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///" + os.path.join(basedir,"database.db")

db=SQLAlchemy(app)

Migrate(app,db)

api=Api(app)

class UserModel(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(60),unique=True,nullable=True)

    def __repr__(self):
        return f"User(Name : {self.name} || Email : {self.email}"

user_fields= {
    "id": fields.Integer,
    "name" : fields.String,
    "email" : fields.String
}

parser=reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help="Name cannot be Blank")
parser.add_argument('email',type=str,required=True,help="Email cannot be blank")

class Users(Resource):

    @marshal_with(user_fields)
    def get(self):
        users=UserModel.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args=parser.parse_args()
        user=UserModel(name=args["name"],email=args["email"])
        db.session.add(user)
        db.session.commit()

        users=UserModel.query.all()
        return users

    @marshal_with(user_fields)
    def delete(self):

        data=request.get_json()
        name=data.get("name")
        email=data.get("email")

        user=UserModel.query.filter_by(name=name).first()

        if user:
            db.session.delete(user)
            db.session.commit()

        return UserModel.query.all()

    @marshal_with(user_fields)
    def patch(self):

        data=request.get_json()
        email=data.get("email")
        name=data.get("name")
        user=UserModel.query.filter_by(name=name).first()
        user.email=email
        db.session.commit()

        return UserModel.query.all()

    def put(self):

        data=request.get_json()
        name=data.get("name")
        email=data.get("email")

        quer=update(UserModel).where(UserModel.name==name).values(email=email)
        db.session.execute(quer)
        db.session.commit()

        return UserModel.query.all()

api.add_resource(Users,"/api/users/")

@app.route("/")
def home():
    return "<h1> Hello from Flask Restful API</h1>"

if __name__ == "__main__":
    app.run(debug=True)