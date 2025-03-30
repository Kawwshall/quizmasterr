from flask import Flask , render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/admin")
def admin():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)