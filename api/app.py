""" Main app starter module
    file: app.py
    Author: Yaekob Demisse
    Date: June 11 2023 14:41
"""

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from models import db
from config import config
from routes.auth import auth
from routes.referals import referals

# Initialize the app
app = Flask(__name__)
CORS(app)
JWTManager(app)
app.config["SQLALCHEMY_DATABASE_URI"] = config["db-url"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config["flask-secret"]
app.config["JWT_SECRET_KEY"] = config["jwt-secret-key"]
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "your_mail@gmail.com"
app.config["MAIL_PASSWORD"] = "your_email_password"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(referals)


if __name__ == "__main__":
    app.run(port=5000, debug=True)