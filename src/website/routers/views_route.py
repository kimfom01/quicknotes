from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    """
    Render the homepage
    """
    if request.method == "POST":
        return redirect(url_for("notes.new_note"))
    return render_template("home.html", user=current_user)
