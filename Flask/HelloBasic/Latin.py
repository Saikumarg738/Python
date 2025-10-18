from flask import Flask,render_template
import os

web=Flask(__name__)
lname=""
@web.route("/user/<name>")
def hello(name):
    if (name[len(name)-1].lower()=="y"): # [-1]
        lname = name.replace(name[len(name)-1],"ful") # Use [:-1]
    else:
        lname=name+"y"

    return f"<h1>Latin name of {name} is {lname}</h1>"

if __name__ == "__main__":
    web.run()
