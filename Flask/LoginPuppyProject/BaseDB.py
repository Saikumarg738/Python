from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from Form import AddForm,DelForm

app=Flask(__name__)

basedir=os.path.dirname(__file__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

app.config['SECRET_KEY']="SaiKumar"

Migrate(app,db)

class Student(db.Model):

    Name=db.Column(db.String(20),primary_key=True)

    def __init__(self,name):
        self.Name=name

    def __repr__(self):
        return f"The puppy name is {self.Name}"

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/add",methods=["GET","POST"])
def Add():

    fm=AddForm()

    if fm.validate_on_submit():

        name=fm.Name.data

        stu=Student(name)
        db.session.add(stu)
        db.session.commit()

        return redirect(url_for('List'))

    return render_template("AddForm.html",fm=fm)

@app.route("/delete",methods=["GET","POST"])
def Del():

    fm=DelForm()

    if fm.validate_on_submit():

        name=fm.Name.data
        stu=Student.query.get(name)
        db.session.delete(stu)
        db.session.commit()

        return redirect(url_for('List'))

    return render_template('Delete.html',fm=fm)

@app.route("/list")
def List():

    stu=Student.query.all()

    return render_template('List.html',stu=stu)

if(__name__=="__main__"):
    app.run(debug=True)


