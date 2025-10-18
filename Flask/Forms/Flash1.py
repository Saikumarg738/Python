from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Needed for flashing messages

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    if not username:
        flash('Username is required!', 'error')
        return redirect(url_for('index'))
    flash('Form submitted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('Flash1.html')

app.run()
