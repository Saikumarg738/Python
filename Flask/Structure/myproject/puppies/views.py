from flask import Flask,render_template,redirect,url_for,Blueprint
from myproject import db
from myproject.models import Student
from myproject.puppies.forms import AddForm,DelForm

blueprint_puppy=Blueprint('puppies',__name__,template_folder='templates/puppies')

@blueprint_puppy.route("/add",methods=["GET","POST"])
def Add():

    fm=AddForm()

    if fm.validate_on_submit():

        name=fm.Name.data

        stu=Student(name)
        db.session.add(stu)
        db.session.commit()

        return redirect(url_for('puppies.List'))

    return render_template("AddForm.html",fm=fm)

@blueprint_puppy.route("/del",methods=["GET","POST"])
def Del():

    fm=DelForm()

    if fm.validate_on_submit():

        name=fm.Name.data
        stu=Student.query.get(name)
        db.session.delete(stu)
        db.session.commit()

        return redirect(url_for('puppies.List'))

    return render_template('Delete.html',fm=fm)

@blueprint_puppy.route("/list")
def List():

    stu=Student.query.all()

    return render_template('List.html',stu=stu)