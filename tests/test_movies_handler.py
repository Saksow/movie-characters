import time


def test_movies_index(client):
    response = client.get('/movies', follow_redirects=True)

    assert response.status_code == 200
    assert b'<h1>Mock Studio Movies</h1>' in response.data
    assert b'<b>Title:</b> Castle in the Sky' in response.data
    assert b'<b>Name:</b> Colonel Muska' in response.data


def test_movies_caching(client):
    start_time = time.time()
    client.get('/movies', follow_redirects=True)

    assert time.time() - start_time > 0.3

    start_time = time.time()
    client.get('/movies', follow_redirects=True)

    assert time.time() - start_time < 0.3
