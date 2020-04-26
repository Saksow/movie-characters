from flask import Blueprint, render_template
from flask_caching import Cache

from app.adapters.movies import Ghibli

movies = Blueprint('movies', __name__, url_prefix='/movies')
cache = Cache(config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 60})


@movies.route('/')
@cache.cached()
def index():
    adapter = Ghibli()
    return render_template('movies/index.html', movies=adapter.get_all())
