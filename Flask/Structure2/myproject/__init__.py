from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir=os.path.dirname(__file__)

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///" + os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACT_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="SAIKUMAR"

db=SQLAlchemy(app)

Migrate(app,db)

from myproject.Department.views import bp_dept
from myproject.Employee.views import bp_emp

app.register_blueprint(bp_dept)
app.register_blueprint(bp_emp)

