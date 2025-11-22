from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class AddForm(FlaskForm):
    CName=StringField("Enter College name")
    SName=StringField("Enter Student name")
    Submit=SubmitField("Submit")