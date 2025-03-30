from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from run import app
from models import db

with app.app_context():
        # Import models to register them with SQLAlchemy
        from models import User, Subject, Chapter, Quiz, Question, Score, create_admin  # Changed to absolute import
        db.create_all()  # Create database tables if they don't exist
        create_admin()  # Ensure admin user is created
        print("Database initialized successfully.")