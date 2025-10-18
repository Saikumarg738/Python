from flask import Flask,render_template,request
from requests.compat import numeric_types
from win32gui import FlashWindowEx

report=""
web=Flask(__name__)

@web.route("/")
def index():
    return render_template("projectindex.html")

@web.route("/report")
def report():
    report=False
    num_end=False
    upper=False
    lower=False
    username=request.args.get('username')
    num_end=username[-1].isdigit()
    for i in username:
        if(i.islower()==True):
            lower=True
            break
    for i in username:
        if(i.isupper()==True):
            upper=True
            break
    if( num_end & upper & lower):
        report=True
    else:
        report=False

    return render_template("projectreport.html",report=report,num_end=num_end,lower=lower,upper=upper)

web.run()