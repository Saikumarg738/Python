from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class AddForm(FlaskForm):

    Name=StringField("Enter Student name")
    Submit=SubmitField("Submit")

class DelForm(FlaskForm):
    Name=StringField("Enter puppy name")
    Submit=SubmitField("Delete")