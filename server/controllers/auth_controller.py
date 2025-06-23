from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from ..models import db, User

blacklist = set()

class Register(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "All fields are required."}, 400

        if User.query.filter((User.username == username)).first():
            return {"error": "Username already exists."}, 409

        new_user = User(
            username=username
        )
        new_user.password_hash = password
        db.session.add(new_user)
        db.session.commit()

        token = create_access_token(identity=str(new_user.id))
        return {"token": token, "user": new_user.to_dict()}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not user.authenticate(password):
            return {"error": "Invalid username or password."}, 401

        token = create_access_token(identity=str(user.id))
        return {"token": token, "user": user.to_dict()}, 200
    
blacklist = set()

class Logout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        blacklist.add(jti)
        return {"message": "Successfully logged out."}, 200


