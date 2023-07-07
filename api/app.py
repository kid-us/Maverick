""" Main app starter module
    file: app.py
    Author: Yaekob Demisse
    Date: June 11 2023 14:41
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from models import db
from config import config

from routes.auth import auth
from routes.referals import referal
from routes.tournament import tournament
from utils.verify_email import send_email, verify_email_token
from flask_mail import Mail

# Initialize the app
app = Flask(__name__)
CORS(app)
JWTManager(app)
app.config["SQLALCHEMY_DATABASE_URI"] = config["db-url"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config["flask-secret"]
app.config["JWT_SECRET_KEY"] = config["jwt-secret"]
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(auth)
app.register_blueprint(referal)
app.register_blueprint(tournament)


@app.route("/api/send-email")
def send_email_verification():
    email = "dawitjuicewrld@gmail.com"
    send_email(email)
    return jsonify({"message": "Email sent"})


@app.route("/api/verify-email")
def verify_email():
    token = request.args.get("token")
    email = verify_email_token(token)
    return jsonify({"message": "Email verified", "email": email})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
