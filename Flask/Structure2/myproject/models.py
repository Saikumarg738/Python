from myproject import db
from sqlalchemy.orm import backref


class Department(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    employees=db.relationship("Employee",backref="department")


class Employee(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    dept_id=db.Column(db.Integer,db.ForeignKey("department.id"))