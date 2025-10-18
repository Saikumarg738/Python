from flask import Flask,render_template

webins=Flask(__name__)

@webins.route("/")
def stacmeth():
    return render_template("static.html")

webins.run(debug=True)