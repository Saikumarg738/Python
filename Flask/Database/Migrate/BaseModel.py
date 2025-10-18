import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

web=Flask(__name__)

basedir=os.path.dirname(__file__)


web.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
web.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(web)

migrate=Migrate(web,db)

class myform(db.Model):

    ID=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(50),nullable=False)
    Company=db.Column(db.String(50),nullable=False)
    Loc=db.Column(db.String(50))

    def __init__(self,ID,Name,Company,Loc):
        self.ID=ID
        self.Name=Name
        self.Company=Company
        self.Loc=Loc

    def __repr__(self):
        return f"{self.Name} has ID : {self.ID} and is working in company {self.Company} in {self.Loc}"

