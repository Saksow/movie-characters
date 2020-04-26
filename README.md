# movie-characters
A Python/Flask application that displays movies and characters from a given studio.

## Introduction
This application connects to [Studio Ghibli API](https://ghibliapi.herokuapp.com/) to retrieve a
list of movies and characters, then aggregates the data and displays it. A memory cache layer is
added on the UI to minimise network operations and waiting time, it expires after 1 minute.

The design of the code aims to simplify future integrations to other studios and mocking external
calls, which is useful for automated tests.

## Try the app
You can directly try the app on [Heroku](https://movie-characters.herokuapp.com/movies/).

## Run and test the app

### Using Docker Compose
If you have the command `docker-compose` installed, just run:
```shell script
docker-compose up -d
```
It will start a Docker container running on: http://localhost:8000/movies/

To run the automated tests (including code coverage) inside the container:
```shell script
docker-compose exec app pytest -c tests/pytest.ini
```

### Using a virtual environment
If you have `Python 3.6` installed, create a virtual environment and run the app:
```shell script
python3.6 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
It will run the Flask app on: http://localhost:8000/movies/

To run the automated tests (including code coverage) inside the virtual environment:
```shell script
source .venv/bin/activate
pytest -c tests/pytest.ini
```

## And that's it
Thanks for reviewing!
