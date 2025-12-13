from flask import Flask, render_template, redirect, url_for, blueprints, Blueprint
from myproject import db
from myproject.models import Department
from myproject.Department.forms import AddDept

bp_dept=Blueprint('dept',__name__,template_folder='templates/dept')


@bp_dept.route("/Department")
def Add_Department():

    fm=AddDept()

    if fm.validate_on_submit():
        name=fm.name.data

        dpt=Department(name="BRCC")
        db.session.add(dpt)
        db.session.commit()

        return redirect(url_for("employee.List"))


    return render_template("AddDept.html",fm=fm)