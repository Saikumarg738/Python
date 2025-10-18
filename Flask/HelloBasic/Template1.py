from flask import Flask,render_template
import os

web=Flask(__name__)

@web.route("/")
def sleep():
    var=["Sai","Kumar","Gangupamu"]
    return render_template("basic.html",var=var)

if __name__ == "__main__":
    web.run()
