from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"]
)

@app.route("/login")
@limiter.limit("10 per hour")
def login():
    return f"{get_remote_address()}"

@app.route("/data")
def data():
    return "Some Data"

app.run()
