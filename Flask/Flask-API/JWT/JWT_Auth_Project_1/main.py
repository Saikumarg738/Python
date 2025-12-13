from flask import Flask,jsonify

from extensions import db,jwt
from flask_migrate import Migrate
from auth import auth_bp
from users import users_bp
import os
from datetime import timedelta
from models import UserModel

app=Flask(__name__)

basedir=os.path.dirname(__file__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'database.db')
app.config['JWT_SECRET_KEY']='a6da2adda2859adceac3b7d6d75d0656d36d5b835636b7eff9a0fff1ce4f0ab0'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=40)

db.init_app(app)

jwt.init_app(app)

Migrate(app,db)

app.register_blueprint(auth_bp,url_prefix="/auth")
app.register_blueprint(users_bp,url_prefix="/all")

@jwt.user_lookup_loader
def load_user(jwt_header,jwt_data):
    identity = jwt_data['sub']

    return UserModel.query.filter_by(username=identity).one()

@jwt.additional_claims_loader
def add_claim(identity):
    if identity == "Sam2":
        return {"role" : "child"}
    return {"role" : "Parents"}

@jwt.expired_token_loader
def expired_token_call(jwt_header,jwt_data):
    return jsonify({
        "message" : "sorry raaa....token time ayipoyindi"
    }),401

@jwt.invalid_token_loader
def invalid_token(error):
    return jsonify({
        "message" : "Token tappu raa pulka"
    }),401

@jwt.unauthorized_loader
def unauthorized(error):
    return jsonify({
        "message" : "asalu token edi raaaa"
    }),401

@app.route("/")
def hello():
    return "<h1> Hello Sai </h1>"

if __name__ == "__main__":
    app.run(port=5020)
