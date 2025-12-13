from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class AddEmp(FlaskForm):
    name=StringField("Enter Emp name")
    dname=StringField("Enter department name")
    Submit=SubmitField("Submit")

