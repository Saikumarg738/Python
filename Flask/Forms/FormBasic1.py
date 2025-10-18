from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

web=Flask(__name__)

web.config['SECRET_KEY'] = 'mysecretkey'

class myform(FlaskForm):
    name=StringField('Enter you name')
    submit=SubmitField('Submit')

@web.route("/",methods=["GET","POST"])
def index():
    obj=myform()

    name=obj.name.data

    return render_template("FormBasic1.html",obj=obj,name=name)

web.run(debug=True)