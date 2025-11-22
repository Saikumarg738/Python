from flask import Flask
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from myproject.model import User


class login(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Submit')

class registation(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm',message="Password not matched")])
    password_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    Register = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email already exists!')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username already exists')