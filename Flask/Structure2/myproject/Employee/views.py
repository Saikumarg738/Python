from flask import Flask, render_template, redirect, url_for, blueprints, Blueprint
from myproject import db
from myproject.models import Employee
from myproject.Employee.forms import AddEmp

bp_emp=Blueprint("employee",__name__,template_folder="templates/employee")


@bp_emp.route("/addemployee")
def Add_Employee():

    fm=AddEmp()

    if fm.validate_on_submit():
        name=fm.name.data
        dname=fm.dname.data

        dpt=Employee(name=name,dept_id=dname)
        db.session.add(dpt)
        db.session.commit()

        return redirect(url_for("employee.List"))


    return render_template("AddEmp.html",fm=fm)

@bp_emp.route("/list")
def List():

    d1=Employee.query.all()

    return render_template("List.html",d1=d1)
