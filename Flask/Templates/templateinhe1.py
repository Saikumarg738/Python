from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    names = ['Sai', 'Reyaz', 'Amit']
    return render_template('templateinh1.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)
