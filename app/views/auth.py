from flask import Blueprint, render_template, request
from app.controllers.auth_controller import login, logout, register

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login_view():
    if request.method == "POST":
        return login(request.form["username"], request.form["password"])
    return render_template("login.html")

@auth_bp.route("/logout")
def logout_view():
    return logout()

@auth_bp.route("/register", methods=["GET", "POST"])
def register_view():
    if request.method == "POST":
        return register(request.form["username"], request.form["email"], request.form["password"])
    return render_template("register.html")
