#!/usr/bin/python3
"""
    This is main file for user authentication and authorization
"""


from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from models.users import User
from models import db

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

# Register a new user
@auth.route("/register", methods=["POST"])
def register():
    """
        This function registers a new user
    """

    data = request.get_json()
    if not data:
        return jsonify({
            "status": "error",
            "message":"Invalid payload or content type"
        }), 400
    
    # check for required feilds in the payload
    required = ["username", "email", "password"]
    for field in required:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": "{} is required".format(field)
            }), 400

    # check if the user already exists
    user = User.query.filter_by(username=data["username"]).first()
    if user:
        return jsonify({
            "status": "error",
            "message": "Username already exists"
        }), 400
    
    # check if the email already exists
    user = User.query.filter_by(email=data["email"]).first()
    if user:
        return jsonify({
            "status": "error",
            "message": "Email already exists"
        }), 400
    
    # create the user
    user = User([data["username"], data["email"], generate_password_hash(data["password"])])
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User created successfully"
    }), 201

# Login a user
@auth.route("/login", methods=["POST"])
def login():
    """
        This function logs in a user
    """

    data = request.get_json()
    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid payload or content type"
        }), 400
    
    # check for required feilds in the payload
    required = ["email", "password"]
    for field in required:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": "{} is required".format(field)
            }), 400

    # check if the user exists
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User does not exist"
        }), 400

    # check if the password is correct
    if not check_password_hash(user.password, data["password"]):
        return jsonify({
            "status": "error",
            "message": "Incorrect password"
        }), 400
    
    # create the access token
    expires = timedelta(days=7)
    access_token = create_access_token(identity=user.email, expires_delta=expires)

    return jsonify({
        "status": "success",
        "message": "User logged in successfully",
        "access_token": access_token
    }), 200

# verify user by sending an email
@auth.route("/verify", methods=["POST"])
def verify():
    """"
        This function verifies a user
    """
    user_email = request.args.get("email")
    if not user_email:
        return jsonify({
            "status": "error",
            "message": "Email is required"
        }), 400
    
    # check if the user exists
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User does not exist"
        }), 400
    
    # change is_verified to true
    user.is_verified = True
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User verified successfully"
    }), 200

