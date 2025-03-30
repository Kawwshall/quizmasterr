from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from ..models import db, User, Subject, Quiz, Score

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, role="user").first()
        if user and user.check_password(password):
            session["user"] = user.username
            return redirect(url_for("user.user_dashboard"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("user/login.html")

@user_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "success")
    return redirect(url_for("user.login"))

@user_bp.route("/dashboard")
def user_dashboard():
    if "user" not in session:
        return redirect(url_for("user.login"))
    user = User.query.filter_by(username=session["user"]).first()
    subjects = Subject.query.all()
    return render_template("user/dashboard.html", user=user, subjects=subjects)

@user_bp.route("/scores")
def view_scores():
    if "user" not in session:
        return redirect(url_for("user.login"))
    user = User.query.filter_by(username=session["user"]).first()
    scores = Score.query.filter_by(user_id=user.id).all()
    return render_template("user/scores.html", scores=scores)

@user_bp.route("/summary")
def summary_charts():
    if "user" not in session:
        return redirect(url_for("user.login"))
    user = User.query.filter_by(username=session["user"]).first()
    scores = Score.query.filter_by(user_id=user.id).all()
    return render_template("user/summary.html", scores=scores)
