from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class AddDept(FlaskForm):
    name=StringField("Enter Dept name")
    Submit=SubmitField("Submit")

