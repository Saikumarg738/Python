from flask import Flask,render_template

webins=Flask(__name__)

@webins.route("/contact")
def contact():
    return render_template("contact.html")

@webins.route("/view")
def view():
    return render_template("view.html")

@webins.route("/about")
def about():
    return render_template("about.html")


webins.run(debug=True)
