# import re
# from .conftest import client_logged_in


# # instead of using collection_id: 1, get the currently logged in user's default collection_id and use it to run the test
# # this will fix the crash when github is runing the test


# def test_get_my_notes(client_logged_in):
#     data = {"collection_id": 1}

#     response = client_logged_in.get("/my-notes", data=data)

#     assert re.search("Demo's Notes", response.get_data(as_text=True)) is not None


# def test_get_my_collections(client_logged_in):
#     response = client_logged_in.get("/my-collections")

#     assert re.search("Demo's Collections", response.get_data(as_text=True)) is not None


# def test_get_new_note(client_logged_in):
#     response = client_logged_in.get("/new-note")

#     assert re.search("Choose a Collection", response.get_data(as_text=True)) is not None


# def test_post_new_note_valid(client_logged_in):
#     data = {"note": "test note data", "collection_id": 1}

#     response = client_logged_in.post("/new-note", data=data)

#     assert (
#         re.search(
#             'You should be redirected automatically to the target URL: <a href="\/my-notes\?collection_id=1">\/my-notes\?collection_id=1<\/a>\. If not, click the link',
#             response.get_data(as_text=True),
#         )
#         is not None
#     )


# def test_post_new_note_invalid(client_logged_in):
#     data = {"note": "", "collection_id": 1}

#     response = client_logged_in.post("/new-note", data=data)

#     assert (
#         re.search(
#             "Note is too short",
#             response.get_data(as_text=True),
#         )
#         is not None
#     )


# def test_delete_note_valid():
#     pass
