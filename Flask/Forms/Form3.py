from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)

app.config['SECRET_KEY']="MySecret"

class myform(FlaskForm):
    Name = StringField("Enter your name")
    Submit = SubmitField("Submit")

@app.route("/",methods=["GET","POST"])
def home():
    obj=myform()
    return render_template("Form3.html",og=obj)

app.run()