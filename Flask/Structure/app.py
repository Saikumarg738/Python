from flask import Flask,render_template
from myproject import app

@app.route("/")
def Home():
    return render_template("home.html")

if (__name__=="__main__"):
    app.run(debug=True)