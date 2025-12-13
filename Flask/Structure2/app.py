from flask import Flask,render_template
from myproject import app


@app.route("/home")
def home():
    return render_template("home.html")

app.run(debug=True)