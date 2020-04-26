from typing import Dict, List

from app.adapters.movies import Ghibli


def test_get_all(mocker):
    mocker.patch.object(Ghibli, '_get_movies', new=_mock_get_movies)
    mocker.patch.object(Ghibli, '_get_characters', new=_mock_get_characters)
    under_test = Ghibli()
    expected = [
        {
            'id': 'movie-1',
            'title': 'Movie 1',
            'description': 'Desc 1',
            'director': 'Dir 1',
            'producer': 'Prod 1',
            'release_date': '2001',
            'rt_score': '91',
            'characters': [
                {
                    'id': 'char-1',
                    'name': 'Char 1',
                    'gender': 'Male',
                    'age': '31',
                    'eye_color': 'Black',
                    'hair_color': 'Black'
                }
            ]
        },
        {
            'id': 'movie-2',
            'title': 'Movie 2',
            'description': 'Desc 2',
            'director': 'Dir 2',
            'producer': 'Prod 2',
            'release_date': '2002',
            'rt_score': '92',
            'characters': [
                {
                    'id': 'char-1',
                    'name': 'Char 1',
                    'gender': 'Male',
                    'age': '31',
                    'eye_color': 'Black',
                    'hair_color': 'Black'
                },
                {
                    'id': 'char-2',
                    'name': 'Char 2',
                    'gender': 'Female',
                    'age': '32',
                    'eye_color': 'Brown',
                    'hair_color': 'Brown'
                }
            ]
        }

    ]

    assert list(under_test.get_all()) == expected


def _mock_get_movies(_) -> List[Dict]:
    return [
        {
            'id': 'movie-1',
            'title': 'Movie 1',
            'description': 'Desc 1',
            'director': 'Dir 1',
            'producer': 'Prod 1',
            'release_date': '2001',
            'rt_score': '91'
        },
        {
            'id': 'movie-2',
            'title': 'Movie 2',
            'description': 'Desc 2',
            'director': 'Dir 2',
            'producer': 'Prod 2',
            'release_date': '2002',
            'rt_score': '92'
        }
    ]


def _mock_get_characters(_) -> List[Dict]:
    return [
        {
            'id': 'char-1',
            'name': 'Char 1',
            'gender': 'Male',
            'age': '31',
            'eye_color': 'Black',
            'hair_color': 'Black',
            'films': [
                'https://ghibliapi.herokuapp.com/films/movie-1',
                'https://ghibliapi.herokuapp.com/films/movie-2'
            ]
        },
        {
            'id': 'char-2',
            'name': 'Char 2',
            'gender': 'Female',
            'age': '32',
            'eye_color': 'Brown',
            'hair_color': 'Brown',
            'films': [
                'https://ghibliapi.herokuapp.com/films/movie-2'
            ]
        }
    ]
