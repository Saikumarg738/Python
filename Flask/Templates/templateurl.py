from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('urlfor.html')

@app.route("/hello")
def hello():
    return "Hello from Sai"

@app.route("/hi/<user>")
def hi(user):
    return f"Hello {user}"

@app.route('/go-to-hello')
def go_to_hello():
    return redirect(url_for('hello'))  # redirects to /hello

if __name__ == '__main__':
    app.run(debug=True)
