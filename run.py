import sys
from quizmaster import create_app
from quizmaster.routes.adminblueprint import admin_bp
from quizmaster.routes.userblueprint import user_bp

app = create_app()

# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "initdb":
        with app.app_context():
            from quizmaster.models import db, create_admin
            db.create_all()  # Create database tables
            create_admin()  # Ensure admin user is created
            print("Database initialized successfully.")
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)