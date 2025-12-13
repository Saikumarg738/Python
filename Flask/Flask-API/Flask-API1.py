from flask import Flask,jsonify

app=Flask(__name__)

employees=[{'Name':"Sai",'Position':"SMT",'Exp':"5"},
           {'Name':"Meghna",'Position':"SMT",'Exp':"5"},
           {'Name':"Abhi",'Position':"SMT",'Exp':"4"},
           {'Name':"Teja",'Position':"MT",'Exp':"3"}]

@app.route("/home",methods=["GET"])
def home():
    return jsonify({"emps":employees})

@app.route("/home/<int:Exp>",methods=["GET"])
def exp(Exp):
    return jsonify({"Experience":employees[Exp]})

@app.route("/home",methods=["POST"])
def addcourse():
    employee={'Name':"KK",'Position':"SMT",'Exp':"6"}
    employees.append(employee)
    return jsonify({"Employee":employees})

app.run()