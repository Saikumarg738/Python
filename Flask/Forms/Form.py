from flask import Flask,render_template,request

webins=Flask(__name__)


@webins.route("/",methods=["GET","POST"])
def display():
    print(request.method)
    print(request.form)
    if(request.method == "POST"):
        with open("Formoutput.txt","w") as fo:
            fo.write(f"The name is {request.form['name']} and email is {request.form['email']}")
        return render_template("Form.html")
    else:
        return render_template("Form.html")

webins.run(debug=True)