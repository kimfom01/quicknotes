from website import create_app, app_config
from website import oauth


app = create_app()

oauth.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app_config.get("PORT", 5000))
