from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app=Flask(__name__)

basedir=os.path.dirname(__file__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'mysecretkey'

db=SQLAlchemy(app)

Migrate(app,db)

from myproject.owners.views import blueprint_owner
from myproject.puppies.views import blueprint_puppy

app.register_blueprint(blueprint_puppy,url_prefix="/puppy")
app.register_blueprint(blueprint_owner,url_prefix="/owner")