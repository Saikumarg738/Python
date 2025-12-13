from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir=os.path.dirname(__file__)

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'Relation1.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Department(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))

    employees=db.relationship("Employee",backref="department")

class Employee(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    department_id=db.Column(db.Integer,db.ForeignKey('department.id'))