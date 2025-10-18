from flask import Flask,render_template,request

webins=Flask(__name__)

@webins.route("/")
def index():
    return render_template('index.html')

@webins.route("/signup")
def signup():
    return render_template('signup.html')

@webins.route("/thankyou",methods=['GET','POST'])
def thank_you():
    print(request.form)
    return render_template('thankyou.html',first=request.form['first'],last=request.form['last'])

webins.run(debug=True)