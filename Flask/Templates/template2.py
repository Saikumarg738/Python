from flask import Flask,render_template

webins=Flask(__name__)

@webins.route("/")
def contact():
    names=["Sai","Kumar","Gangupamu"]
    return render_template("basic2.html",names=names)

webins.run(debug=True)
