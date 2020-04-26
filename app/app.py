from flask import Flask

from app.handlers.movies import cache, movies


def create_app(config: str) -> Flask:
    app = Flask('movie-characters', template_folder='app/templates')

    app.config.from_object(config)
    app.register_blueprint(movies)
    cache.init_app(app)

    return app
