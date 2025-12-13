from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app=Flask(__name__)

basedir=os.path.dirname(__file__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,"emp1.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

migrate=Migrate(app,db)

class Employee(db.Model):
    EMPID=db.Column(db.Integer,primary_key=True)
    EMPNAME=db.Column(db.String(50),nullable=False)
    EMPEMAIL=db.Column(db.String(100),nullable=False,unique=True)
    EMPSAL=db.Column(db.Integer)
    EMPROLE=db.Column(db.String(10))

    def __repr__(self):
        return f"Employee name is {self.EMPNAME}, Employee email is {self.EMPEMAIL} and Salary is {self.EMPSAL} and role is {self.EMPROLE}"
