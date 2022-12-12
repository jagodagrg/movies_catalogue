import pytest
from unittest.mock import Mock
import tmdb_client


def test_call_tmdb_api():
    movies_list = tmdb_client.call_tmdb_api(endpoint='movie/popular')
    assert movies_list is not None


def test_get_single_movie(monkeypatch):
    mock_movie = ['Movie 1']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie = tmdb_client.get_single_movie(movie_id=1)
    assert movie == mock_movie


def test_get_movie_images(monkeypatch):
    mock_movie_images = {"file_path": "test.jpg"}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_images = tmdb_client.get_movie_images(movie_id=1)
    assert movie_images == mock_movie_images


def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = {"id": 1, "cast": [
        "actor1", "actor2", "actor3", "actor4"]}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id=1, how_many=3)
    assert movie_cast == mock_movie_cast["cast"][:3]
