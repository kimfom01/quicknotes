import json
from flask import Blueprint, request, render_template, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user

from .models.Collection import Collection

from .models.Note import Note
from .repositories.notes_repo import notes_repo


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

    response = notes_repo.get_collections(user_id=current_user.id)

    return render_template(
        "my_collections.html", user=current_user, collection=response.body
    )


@notes.route("/new-note", methods=["GET", "POST"])
@login_required
def new_note():
    """
    Create new note
    """

    collections = Collection.query.filter_by(user_id=current_user.id).all()

    if request.method == "POST":
        data = request.form.get("note")
        collection_id: int = request.form.get("collection_id")

        if len(data) < 1:
            flash("Note is too short", category="error")
            return render_template(
                "new_note.html", user=current_user, collections=collections
            )

        created_note = Note(
            data=data, user_id=current_user.id, collection_id=collection_id
        )

        response = notes_repo.create_note(note=created_note)

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
