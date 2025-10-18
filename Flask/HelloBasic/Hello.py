from flask import Flask,render_template
import os

web=Flask(__name__)

@web.route("/")
def hello():
    return "Good afternoon Sai!"

@web.route("/sleep")
def sleep():
    return render_template("index.html")

if __name__ == "__main__":
    web.run(port=6189)
