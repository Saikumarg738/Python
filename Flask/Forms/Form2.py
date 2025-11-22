from flask import Flask,request

app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def login():
    username = request.form['username']
    return f"Welcome {username}"

app.run()