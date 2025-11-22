from Singleton_db import singleton_db
from flask import Flask


app=Flask(__name__)

@app.route("/")
def home():
    d1=singleton_db()
    d2=singleton_db()

    return f"Is instance same?{d1 is d2}"

app.run()