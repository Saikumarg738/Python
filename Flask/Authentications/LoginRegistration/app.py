from myproject import db,app,login_manager
from flask import Flask,render_template,url_for,flash,redirect,request,abort
from myproject.forms import login,registation
from myproject.model import User
from flask_login import login_user,logout_user,login_required

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You are logged out now")
    return redirect(url_for('home'))

@app.route("/loginhome",methods=["GET","POST"])
def loginhome():

    loginform = login()

    if loginform.validate_on_submit():
        email=loginform.email.data
        password=loginform.password.data

        emailvalue=User.query.filter_by(email=email).first()

        if emailvalue is not None and emailvalue.check_password(password) :
            login_user(emailvalue)
            flash('You have logged in sucessfully')

        next = request.args.get('next')

        # So let's now check if that next exists, otherwise we'll go to
        # the welcome page.
        if next == None or not next[0] == '/':
            next = url_for('welcome')

        return redirect(next)
    return  render_template("login.html",loginform=loginform)

@app.route("/Register",methods=["GET","POST"])
def register():

    form=registation()

    if form.validate_on_submit():
        email=form.email.data
        username=form.username.data
        password=form.password.data

        user = User(email,username,password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('loginhome'))
    return render_template("register.html",form=form)



if __name__ == '__main__':
    app.run(debug=True)