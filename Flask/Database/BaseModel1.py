from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from traitlets import Integer

app=Flask(__name__)

basedir=os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,"data1.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

migrate=Migrate(app,db)

class Department(db.Model):
    Dept_id=db.Column(db.Integer,primary_key=True)
    Dept_name=db.Column(db.String(30),nullable=False)

    def __init__(self,name):
        self.Dept_name=name


