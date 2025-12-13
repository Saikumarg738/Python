from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)

app.config['SECRET_KEY']="SAIKUMAR"

class myform(FlaskForm):
    Name=StringField("Enter your name")
    Submit=SubmitField("Submit")

@app.route("/",methods=["GET","POST"])
def home():
    obj=myform()
    return render_template("Form4login.html",obj=obj)

@app.route("/login",methods=["GET","POST"])
def login():
    name=request.args['Name']
    return render_template("Form4logindisplay.html",peddi=name)
app.run()