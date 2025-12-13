from flask import Flask,render_template,url_for,session,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY']="SAIKUMAR"

class myform(FlaskForm):
    Name=StringField("Enter your name",validators=[DataRequired()])
    Excite=BooleanField("Are you excited to join JPM?")
    Role=RadioField("What role you want?",choices=[("Python","Python"),("AWS","AWS")])
    Worktype=SelectField("What skills do you have?",choices=[("Python","Python"),("AWS","AWS")])
    Feedback=TextAreaField()
    Submit=SubmitField("Submit")

@app.route("/home",methods=["GET","POST"])
def home():
    oj=myform()
    if(oj.validate_on_submit()):
        session['Name']=oj.Name.data
        session['Excite']=oj.Excite.data
        session['Role']=oj.Role.data
        session['Worktype']=oj.Role.data
        session['Feedback']=oj.Feedback.data

        return redirect(url_for("thank_you"))
    return render_template("LoginJPM.html",obj=oj)

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou_jpm.html")


app.run()
