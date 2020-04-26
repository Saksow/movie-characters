import time
import urllib.parse
from abc import ABC, abstractmethod
from typing import Dict, List, ValuesView

import requests


class Movies(ABC):
    """ Base class for movies adapters

    This defines an interface for all movies adapters, so we can easily connect the app with new
    movie studios or mock any external dependency during tests.
    """

    @property
    def base_url(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Dict]:
        """ Get all movies with their respective characters from a studio

        Returns:
          Movies as a list of dict
        """
        pass


class Ghibli(Movies):
    base_url = 'https://ghibliapi.herokuapp.com'
    limit = 250  # Ghibli API does not offer pagination so let's use the max limit

    def get_all(self) -> ValuesView:
        movies = {movie['id']: movie for movie in self._get_movies()}

        for char in self._get_characters():
            char_movies = char['films']
            del char['films']  # Not needed anymore
            for movie in char_movies:
                movie_id = self._extract_movie_id(movie)
                movies[movie_id].setdefault('characters', []).append(char)

        return movies.values()

    def _get_movies(self) -> List[Dict]:
        fields = ['id', 'title', 'description', 'director', 'producer', 'release_date', 'rt_score']
        response = requests.get(url=urllib.parse.urljoin(self.base_url, '/films'),
                                params={'limit': self.limit, 'fields': ','.join(fields)})
        return response.json()

    def _get_characters(self) -> List[Dict]:
        fields = ['id', 'name', 'gender', 'age', 'eye_color', 'hair_color', 'films']
        response = requests.get(url=urllib.parse.urljoin(self.base_url, '/people'),
                                params={'limit': self.limit, 'fields': ','.join(fields)})
        return response.json()

    @staticmethod
    def _extract_movie_id(movie_url: str) -> str:
        return movie_url.split('/')[-1]


class Mock(Movies):
    base_url = None

    def get_all(self) -> List[Dict]:
        time.sleep(0.3)  # Simulate some delay in order to test views caching
        return [
            {
                'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe',
                'title': 'Castle in the Sky',
                'description': 'The orphan Sheeta inherited a mysterious crystal ...',
                'director': 'Hayao Miyazaki',
                'producer': 'Isao Takahata',
                'release_date': '1986',
                'rt_score': '95',
                'characters': [
                    {
                        'id': '40c005ce-3725-4f15-8409-3e1b1b14b583',
                        'name': 'Colonel Muska',
                        'gender': 'Male',
                        'age': '33',
                        'eye_color': 'Grey',
                        'hair_color': 'Brown'
                    }
                ]
            }
        ]


class MoviesFactory:

    @staticmethod
    def get_adapter(studio: str) -> Movies:
        if studio == 'ghibli':
            return Ghibli()
        elif studio == 'mock':
            return Mock()
        else:
            raise NotImplementedError(f'Studio "{studio}" is not implemented!')
