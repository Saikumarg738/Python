from flask import session,Flask

app=Flask(__name__)

app.secret_key = 'mysecretkey'



@app.route('/set')
def set_session():
    session['user'] = 'Alice'
    return "Session set!"

@app.route('/get')
def get_session():
    return session.get('user', 'Guest')

app.run()