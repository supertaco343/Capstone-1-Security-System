from flask import Flask
from .init_db import init_db

# initialize the Flask app
app = Flask(__name__)

# initialize the database when the app starts
with app.app_context():
    init_db()

# TODO: Write some routes to interact with the database and frontend