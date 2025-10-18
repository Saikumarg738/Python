from flask import Flask,render_template
import os

web=Flask(__name__)

@web.route("/user/<name>")
def hello(name):
    return f"<h1>Good {name} afternoon, 10th latter of your name is {name[10]}</h1>"

if __name__ == "__main__":
    web.run(debug=True)
