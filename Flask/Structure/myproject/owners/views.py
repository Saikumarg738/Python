from flask import Flask,render_template,redirect,url_for,Blueprint
from myproject import db
from myproject.models import College
from myproject.owners.forms import AddForm

blueprint_owner=Blueprint('owners',__name__,template_folder='templates/owners')

@blueprint_owner.route("/addowner",methods=["GET","POST"])
def AddOwner():

    fm=AddForm()

    if fm.validate_on_submit():

        cname=fm.CName.data
        sname=fm.SName.data

        clg=College(cname,sname)
        db.session.add(clg)
        db.session.commit()

        return redirect(url_for('puppies.List'))

    return render_template("AddOwner.html",fm=fm)