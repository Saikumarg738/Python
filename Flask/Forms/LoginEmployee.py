from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import (StringField,RadioField,
                    BooleanField,SelectField,TextAreaField,SubmitField,DateTimeField)
from wtforms.validators import DataRequired

web=Flask(__name__)

web.config['SECRET_KEY']="SaiKumar"

class myform(FlaskForm):
    Name=StringField("Enter your name",validators=[DataRequired()])
    Look=BooleanField("Are you handsome?")
    Strong=RadioField("How strong are you?",choices=[("Strong","Strong"),("VeryStrong","Very Strong"),("SuperStrong","Super Strong")])
    Food=SelectField("Select your favorite food",choices=[("Chicken","Chicken"),("Fish","Fish"),("Mutton","Mutton")])
    Feedback=TextAreaField()
    Submit=SubmitField("Submit details")


@web.route("/",methods=["GET","POST"])
def login():

    obj=myform()

    if obj.validate_on_submit():

        session['Name']=obj.Name.data
        session['Look']=obj.Look.data
        session['Strong']=obj.Strong.data
        session['Food']=obj.Food.data
        session['Feedback']=obj.Feedback.data

        return redirect(url_for("thank_you"))

    return render_template("LoginEmployee.html",obj=obj)


@web.route("/thankyou")
def thank_you():

    return render_template("LoginEmployeeThankYou.html")

web.run()