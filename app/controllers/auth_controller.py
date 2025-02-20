from flask import redirect, url_for, flash
from flask_login import login_user, logout_user
from app.models.user import User
from app.extensions import db

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return redirect(url_for("views.dashboard"))
    flash("Credenciales inválidas", "danger")
    return redirect(url_for("views.login"))

def logout():
    logout_user()
    return redirect(url_for("views.login"))

def register(username, email, password):
    if User.query.filter_by(username=username).first():
        flash("Usuario ya existe", "danger")
        return redirect(url_for("views.register"))

    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    flash("Registro exitoso", "success")
    return redirect(url_for("views.login"))
