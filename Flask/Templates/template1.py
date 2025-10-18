from flask import Flask,render_template

webins=Flask(__name__)

@webins.route("/")
def contact():
    list=["Sai","Kumar","Gangupamu"]
    return render_template("basic1.html",list=list)



webins.run(debug=True)
