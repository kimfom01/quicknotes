from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Collection
from . import db, oauth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(password) < 7:
            flash("Password must be greater than 6 characters", category="error")
        else:
            user = User.query.filter_by(email=email).first()

            if user:
                if not user.password:
                    flash("You do not have a password!", category="error")
                    flash("Click Sign in with Google to continue",
                          category="error")
                    return render_template("login.html", user=current_user)
                if check_password_hash(user.password, password):
                    flash("Logged in successfully!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for("notes.my_notes"))
                else:
                    flash("Invalid email or password!", category="error")
            else:
                flash("User does not exist!", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exist!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than 6 characters", category="error")
        elif password1 != password2:
            flash("Password and Confirm Password must match", category="error")
        else:
            password_hash = generate_password_hash(password1, method="sha256")
            new_user = User(email=email, first_name=first_name,
                            password=password_hash)
            db.session.add(new_user)
            db.session.commit()

            new_collection = Collection(
                title="Default Collection", user_id=new_user.id)
            db.session.add(new_collection)
            db.session.commit()
            flash("Account created!", category="success")
            login_user(new_user)
            return redirect(url_for("notes.my_notes"))
    return render_template("sign_up.html", user=current_user)


@auth.route("/google-signin")
def google_signin():
    return oauth.notes_app.authorize_redirect(url_for("auth.callback_url", _external=True))


@auth.route("/authCallback")
def callback_url():
    token = oauth.notes_app.authorize_access_token()
    session["user"] = token
    user_info = session["user"].get("userinfo")
    email = user_info.get("email")

    user = User.query.filter_by(email=email).first()

    if user:
        login_user(user)
        flash("Logged in successfully!", category="success")
        return redirect(url_for("notes.my_notes"))
    else:
        google_user = User(first_name=user_info.get("given_name"), email=email)
        db.session.add(google_user)
        db.session.commit()

        new_collection = Collection(title="Default", user_id=google_user.id)
        db.session.add(new_collection)
        db.session.commit()
        flash("Account created!", category="success")
        login_user(google_user)
        return redirect(url_for("notes.my_notes"))
