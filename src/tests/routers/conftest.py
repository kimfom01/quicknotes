# import pytest

# from website import create_app


# @pytest.fixture
# def client():
#     app = create_app()

#     with app.app_context(), app.test_client() as client:
#         yield client


# @pytest.fixture
# def client_logged_in():
#     app = create_app()

#     with app.app_context(), app.test_client() as client:
#         # Login demo user
#         client.get("/demo-login")
#         yield client
