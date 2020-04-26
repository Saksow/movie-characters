from flask import Blueprint, current_app, render_template
from flask_caching import Cache

from app.adapters.movies import MoviesFactory

movies = Blueprint('movies', __name__, url_prefix='/movies')
cache = Cache(config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 60})


@movies.route('/')
@cache.cached()
def index():
    studio = current_app.config['MOVIE_STUDIO']
    adapter = MoviesFactory.get_adapter(studio)
    return render_template('movies/index.html', movies=adapter.get_all(), studio=studio)
