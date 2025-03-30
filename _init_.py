import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')  # Use environment variable or fallback

    db.init_app(app)

    with app.app_context():
        # Import models to register them with SQLAlchemy
        from .models import User, Subject, Chapter, Quiz, Question, Score, create_admin
        db.create_all()  # Create database tables if they don't exist
        create_admin()  # Ensure admin user is created

    return app