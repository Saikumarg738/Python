from flask import Blueprint,jsonify,request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt,current_user


from models import UserModel
from extensions import db

auth_bp=Blueprint('auth_bp',__name__)

@auth_bp.post("/register")
def register():

    data=request.get_json()

    email=data.get('email')
    username=data.get('username')
    password=data.get('password')

    usernm=UserModel.query.filter_by(username=username).first()

    if usernm is not None:
        return jsonify({username : "already exists"}),409

    useremail=UserModel.query.filter_by(email=email).first()
    if useremail is not None:
        return jsonify({email: "already exists"}), 409

    try:
        us = UserModel(username, email, password)
        db.session.add(us)
        db.session.commit()

        return jsonify({username: "has been created"}),201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error" : "Username or email already exists"})

@auth_bp.post("/login")
def login():

    data=request.get_json()

    username=data.get('username')
    password=data.get('password')

    user = UserModel.get_username(username=username)

    if user and user.check_password(password=password):

        access_token=create_access_token(identity=user.username)
        refresh_token=create_refresh_token(identity=user.username)

        return jsonify({
            "message" : "User Exists",
            "tokens" : {
                "Access token" : access_token,
                "Refresh Token" : refresh_token
            }
        }),201

    return jsonify({
        "message" : "Invalid username and password"
    })

@auth_bp.post("/claims")
@jwt_required()
def claims():

    claim_data=get_jwt()
    return claim_data

@auth_bp.get("/userdetails")
@jwt_required()
def userdetails():

    return jsonify({
        "User Details" : {
            "Username" : current_user.username,
            "Email" : current_user.email
        }
    })


