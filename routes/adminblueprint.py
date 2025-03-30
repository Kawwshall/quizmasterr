from flask import Blueprint, render_template, request, redirect, url_for, session, flash  # Reintroduced werkzeug.security
from models import db, User, Subject, Chapter, Quiz, Question  # Changed to absolute import

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/adminlogin", methods=["GET", "POST"])
# def admin_login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         admin = User.query.filter_by(username=username, role="admin").first()
#         if admin and admin.check_password(password):
#             session["admin"] = admin.username
#             return redirect(url_for("admin.admin_dashboard"))
#         else:
#             flash("Invalid credentials", "danger")
#     return render_template("admin/login.html")

@admin_bp.route("/adminlogout")
def admin_logout():
    session.pop("admin", None)
    flash("Logged out successfully", "success")
    return redirect(url_for("admin.admin_login"))

@admin_bp.route("/admindashboard")
def admin_dashboard():
    if "admin" not in session:
        return redirect(url_for("admin.admin_login"))
    subjects = Subject.query.all()
    return render_template("admin/dashboard.html", subjects=subjects)

@admin_bp.route("/subject/edit/<int:subject_id>", methods=["GET", "POST"])
def edit_subject(subject_id):
    if "admin" not in session:
        return redirect(url_for("admin.admin_login"))
    subject = Subject.query.get_or_404(subject_id)
    if request.method == "POST":
        subject.name = request.form.get("name")
        subject.description = request.form.get("description")
        db.session.commit()
        flash("Subject updated successfully", "success")
        return redirect(url_for("admin.admin_dashboard"))
    return render_template("admin/edit_subject.html", subject=subject)

@admin_bp.route("/subject/delete/<int:subject_id>")
def delete_subject(subject_id):
    if "admin" not in session:
        return redirect(url_for("admin.admin_login"))
    subject = Subject.query.get_or_404(subject_id)
    db.session.delete(subject)
    db.session.commit()
    flash("Subject deleted successfully", "success")
    return redirect(url_for("admin.admin_dashboard"))

@admin_bp.route("/a_search", methods=["GET"])
def search():
    if "admin" not in session:
        return redirect(url_for("admin.admin_login"))
    query = request.args.get("query")
    users = User.query.filter(User.username.contains(query)).all()
    subjects = Subject.query.filter(Subject.name.contains(query)).all()
    quizzes = Quiz.query.filter(Quiz.remarks.contains(query)).all()
    return render_template("admin/search_results.html", users=users, subjects=subjects, quizzes=quizzes)
