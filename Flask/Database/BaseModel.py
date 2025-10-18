import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

web=Flask(__name__)

basedir=os.path.dirname(__file__)

# Connects our flask to Database

web.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,"data.sqlite")
web.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# Creating DB instance

db=SQLAlchemy(web)

# Creating first model, model is a table in DB
# Inheriting from db.model class

class mydb(db.Model):

    # By default the class names becomes table name

    # If table name needs to be overwritten

    __tablename__="EMP"

    # Creating column

    EID=db.Column(db.Integer,primary_key=True)

    Name=db.Column(db.String(50),nullable=False)

    BU=db.Column(db.String(50),nullable=False)

    # Define constructor

    def __init__(self,EID,Name,BU):
        self.EID=EID
        self.Name=Name
        self.BU=BU

    def __repr__(self):
        return f"{self.Name} has employee id {self.EID} in {self.BU}"




