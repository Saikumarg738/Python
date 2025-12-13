from flask import Blueprint,request,jsonify
from models import UserModel
from schema import UserSchema
from flask_jwt_extended import jwt_required,get_jwt

users_bp=Blueprint('users',__name__)

@users_bp.get("/users")
@jwt_required()
def getusers():

    claims = get_jwt()
    if claims.get('role') == "Parents":

        page = request.args.get('page',default=1,type=int)

        per_page = request.args.get('per_page',default=3,type=int)

        pageobj = UserModel.query.paginate(page=page,per_page=per_page)

        userdata=UserSchema().dump(pageobj,many=True)



        # users = [{
        #     "id" : u.id,
        #     "name" : u.username,
        #     "email" : u.email
        # } for u in pageobj.items]

        return jsonify({
            "users" : userdata
        })

    return jsonify({
        "message" : "You don't have permission"
    }),409


