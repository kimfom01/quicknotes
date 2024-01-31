from website import create_app
from website import oauth


app = create_app()

oauth.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
