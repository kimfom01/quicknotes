import json
from flask import Blueprint, request, render_template, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user


from ..repositories.notes_repo import notes_repo
from ..repositories.collection_repo import collection_repo


notes = Blueprint("notes", __name__)


@notes.route("my-notes", methods=["GET"])
@login_required
def my_notes():
    """
    Show list of notes
    """

    collection_id = request.args.get("collection_id")

    response = notes_repo.get_all(collection_id)

    return render_template("my_notes.html", user=current_user, notes=response.body)


@notes.route("/my-collections", methods=["GET"])
@login_required
def my_collections():
    """
    Show collections
    """

    response = collection_repo.get_collections(user_id=current_user.id)

    return render_template(
        "my_collections.html", user=current_user, collection=response.body
    )


@notes.route("/new-note", methods=["GET", "POST"])
@login_required
def new_note():
    """
    Create new note
    """

    response = collection_repo.get_collections(user_id=current_user.id)
    if not response.success:
        flash("Something went wrong, try again", category="error")
        return

    collections = response.body

    if request.method == "POST":
        data = request.form.get("note")
        collection_id: int = request.form.get("collection_id")

        if len(data) < 1:
            flash("Note is too short", category="error")
            return render_template(
                "new_note.html", user=current_user, collections=collections
            )

        response = notes_repo.create_note(
            data=data, user_id=current_user.id, collection_id=collection_id
        )

        if response.success:
            flash("Note saved!", category="success")
            return redirect(url_for("notes.my_notes", collection_id=collection_id))

        flash(response.message, category="error")
        return render_template(
            "new_note.html", user=current_user, collections=collections
        )
    return render_template("new_note.html", user=current_user, collections=collections)


@notes.route("/delete-note", methods=["DELETE"])
@login_required
def delete_note():
    """
    Delete existing note endpoint
    """
    data = json.loads(request.data)
    note_id = data["noteId"]
    collection_id = data["collectionId"]

    response = notes_repo.delete_note(note_id=note_id, collection_id=collection_id)

    if response.success:
        return jsonify({"message": response.message}), 204

    return jsonify({"message": response.message}), 404
