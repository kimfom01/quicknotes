from os import getenv
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, logout_user, current_user
from dotenv import load_dotenv

from ..services.auth_service import auth_service
from .. import oauth
from ..services.collection_service import collection_service
from ..services.user_service import user_service

auth = Blueprint("auth", __name__)
DEFAULT_COLLECTION = "Default Collection"

load_dotenv()


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Login user with form
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        response = auth_service.login_user(email=email, password=password)

        if response.success:
            flash(response.message, category="success")
            return redirect(url_for("notes.my_notes", collection_id=response.body.id))
        else:
            flash(response.message, category="error")
            return render_template("login.html", user=current_user)

    return render_template("login.html", user=current_user)


@auth.route("/demo-login", methods=["GET"])
def demo_login():
    """
    Demo login for guests and explorers
    """

    email = getenv("DEMO_USERNAME")

    response = auth_service.login_user(email=email, demo=True)

    if not response.success:
        flash(
            "Something is wrong. Try to again or create your account to login",
            category="error",
        )
        return render_template("login.html", user=current_user)

    flash(response.message, category="success")
    return redirect(url_for("notes.my_collections"))


@auth.route("/logout")
@login_required
def logout():
    """
    Logs the user out of the application.
    Clears user session
    """
    session.clear()
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    """
    Sign up with form
    """
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 != password2:
            flash("Password and Confirm Password must match", category="error")
            return render_template("sign_up.html", user=current_user)
        else:
            response = auth_service.sign_up_user(
                email=email, first_name=first_name, password=password1
            )

            if not response.success:
                flash(response.message, category="error")
                return render_template("sign_up.html", user=current_user)

            flash(response.message, category="success")

            user = response.body

            coll_response = collection_service.get_default_collection(user_id=user.id)

            if not coll_response.success:
                flash(coll_response.message, category="error")
                return redirect(url_for("auth.login"))

            default_collection = coll_response.body

            return redirect(
                url_for("notes.my_notes", collection_id=default_collection.id)
            )

    return render_template("sign_up.html", user=current_user)


@auth.route("/google-signin")
def google_signin():
    """
    Redirect to Google sso

    Return: redirects to callback function
    """
    return oauth.notes_app.authorize_redirect(
        url_for("auth.callback_url", _external=True)
    )


@auth.route("/authCallback")
def callback_url():
    """summary_line
    Gets the token from Google oauth and log in the
    user or create a new user if user doesn't have an account

    Return: redirects to the user's notes
    """
    token = oauth.notes_app.authorize_access_token()
    session["user"] = token
    user_info = session["user"].get("userinfo")
    email = user_info.get("email")

    response = auth_service.sign_up_user(
        email=email, first_name=user_info.get("given_name"), google=True
    )

    if response.success:
        user = response.body
        flash("Logged in successfully!", category="success")

        response = collection_service.get_default_collection(user_id=user.id)

        if not response.success:
            flash(response.message, category="error")
            return redirect(url_for("auth.login"))

        default_collection = response.body

        return redirect(url_for("notes.my_notes", collection_id=default_collection.id))

    flash(response.message, category="error")

    return redirect(url_for("auth.login"))
