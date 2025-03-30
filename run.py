from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes.adminblueprint import admin_bp
from routes.userblueprint import user_bp
from models import db
import os  # Added to generate a random secret key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Set a secure random secret key
db.init_app(app)

# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

@app.route("/")
def main_page():
    return render_template("main.html")

if __name__ == "__main__": 
   app.run(host="0.0.0.0", port=5000, debug=True)