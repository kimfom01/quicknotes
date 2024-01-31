# import pytest
# from .conftest import client
# import re


# @pytest.mark.order(1)
# def test_get_signup(client):
#     response = client.get("/sign-up")

#     assert response.status_code == 200


# @pytest.mark.order(2)
# def test_post_signup(client):
#     email = "test@mail.com"
#     first_name = "test"
#     password1 = "P@$$w0rd123"
#     password2 = "P@$$w0rd123"

#     data = {
#         "email": email,
#         "firstName": first_name,
#         "password1": password1,
#         "password2": password2,
#     }

#     with client.application.app_context():
#         response = client.post("/sign-up", data=data)

#     assert (
#         re.search(
#             'You should be redirected automatically to the target URL: <a href="/my-notes">/my-notes</a>. If not, click the link',
#             response.get_data(as_text=True),
#         )
#         is not None
#     )


# @pytest.mark.order(3)
# def test_post_signup_invalid(client):
#     email = "test2@mail.com"
#     first_name = "test2"
#     password1 = "Passw0rd123"
#     password2 = "P@$$w0rd123"

#     data = {
#         "email": email,
#         "firstName": first_name,
#         "password1": password1,
#         "password2": password2,
#     }

#     with client.application.app_context():
#         response = client.post("/sign-up", data=data)

#     assert re.search(
#         "Password and Confirm Password must match", response.get_data(as_text=True)
#     )


# @pytest.mark.order(4)
# def test_get_login(client):
#     response = client.get("/login")

#     assert response.status_code == 200


# @pytest.mark.order(5)
# def test_post_login(client):
#     email = "test@mail.com"
#     password = "P@$$w0rd123"

#     data = {"email": email, "password": password}

#     with client.application.app_context():
#         response = client.post("/login", data=data)

#     assert re.search(
#         'You should be redirected automatically to the target URL: <a href="\/my-notes\?collection_id=\d+">\/my-notes\?collection_id=\d+<\/a>\. If not, click the link',
#         response.get_data(as_text=True),
#     )


# @pytest.mark.order(6)
# def test_post_login_invalid(client):
#     email = "test@mail.com"
#     password = "12345"

#     data = {"email": email, "password": password}

#     with client.application.app_context():
#         response = client.post("/login", data=data)

#     assert re.search(
#         "Password must be greater than 6 characters", response.get_data(as_text=True)
#     )
