from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

web=Flask(__name__)

basedir=os.path.dirname(__file__)

web.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'datarelation.sqlite')
web.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(web)

Migrate(web,db)

class Puppy(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(40))

    # Create relation

    toy=db.relationship('Toy',lazy='dynamic')

    # Create Owner

    owner=db.relationship('Owner',uselist=False)

    def __init__(self,name):
        self.Name=name

    def __repr__(self):
        if self.owner:
            return f"The puppy name is {self.Name} and owner name is {self.owner.Name}"
        else:
            return f"The puppy name is {self.Name} and it has no owner"

    def distoys(self):
        for i in self.toy:
            print(i.item)

class Toy(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    item=db.Column(db.String(40))
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppy.id'))

    def __init__(self,item,pupid):
        self.item=item
        self.puppy_id=pupid

class Owner(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(40))
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppy.id'))

    def __init__(self,name,pupid):
        self.Name=name
        self.puppy_id=pupid