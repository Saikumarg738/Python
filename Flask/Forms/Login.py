from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

web=Flask(__name__)

web.config['SECRET_KEY']='SaiKumar'
class myform(FlaskForm):
    username=StringField("Enter username: ")
    password=PasswordField("Enter password: ")
    submit=SubmitField("Login")

@web.route("/",methods=["GET","POST"])
def index():
    obj=myform()
    return render_template("Login.html",obj=obj)

@web.route("/loginhome",methods=["GET","POST"])
def loginhome():
    name=request.form['username']
    return render_template("LoginHome.html",name=name)

web.run(debug=True)