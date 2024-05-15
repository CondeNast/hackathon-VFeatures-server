# app/__init__.py
from flask import Flask
from routes import routes_blueprint

# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint with the Flask application instance
app.register_blueprint(routes_blueprint)
