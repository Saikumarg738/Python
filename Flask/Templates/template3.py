from flask import Flask,render_template

webins=Flask(__name__)

@webins.route("/")
def contact():
    names={"web":"Html","Backend":"Python","DB":"SQL"}
    return render_template("basic3.html",names=names)

webins.run(debug=True)
