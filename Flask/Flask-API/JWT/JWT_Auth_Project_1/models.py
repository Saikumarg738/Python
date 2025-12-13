from extensions import db
from werkzeug.security import generate_password_hash,check_password_hash

class UserModel(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    password=db.Column(db.String(40),nullable=False)

    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=generate_password_hash(password)

    def __repr__(self):
        return f"User is {self.username}"

    @classmethod
    def get_username(cls,username):
        return cls.query.filter_by(username=username).first()

    def check_password(self,password):
        return check_password_hash(self.password,password)
