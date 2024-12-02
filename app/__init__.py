import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Email configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "<user email goes here>"
app.config["MAIL_DEFAULT_SENDER"] = "mstcapstonenoreply@gmail.com"

# Eventually, this mailing stuff should be run on a different server so
# that the user doesn't have access to the email that handles the alerts
app.config["MAIL_PASSWORD"] = "wvjz oket sfpm kdcr"
mail = Mail(app)

# Create tables only if the database file does not exist
if not os.path.exists("app.sqlite"):
    with app.app_context():
        db.create_all()

# Import the routes and alert modules
from app import routes, alert, detect