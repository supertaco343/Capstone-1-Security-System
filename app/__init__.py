from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialize the Flask app
app = Flask(__name__)

# initialize the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

with app.app_context():
    from app.models import Camera, Recording

    # delete the database tables if they already exist
    db.drop_all()
    # create the database tables
    db.create_all()

# import the routes
from app import routes
