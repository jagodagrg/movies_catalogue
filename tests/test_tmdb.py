from main import app
import pytest
from unittest.mock import Mock
import tmdb_client


def test_call_tmdb_api(monkeypatch):
    mock_api_response = {"page": 1, "results": [{"id": 1, "title": "Movie 1"}, {
        "id": 2, "title": "Movie 2"}, {"id": 3, "title": "Movie 3"}]}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_api_response
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    api_response = tmdb_client.call_tmdb_api(endpoint="movie/popular")
    assert api_response == mock_api_response


def test_get_single_movie(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = "Movie 1"
    monkeypatch.setattr("tmdb_client.call_tmdb_api", my_mock)
    movie = tmdb_client.get_single_movie(movie_id=1)
    assert movie == "Movie 1"


def test_get_movie_images(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = ["img1", "img2"]
    monkeypatch.setattr("tmdb_client.call_tmdb_api", my_mock)
    movie_images = tmdb_client.get_movie_images(movie_id=1)
    assert movie_images == ["img1", "img2"]


def test_get_single_movie_cast(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = {"id": 1, "cast": [
        "actor1", "actor2", "actor3", "actor4"]}
    monkeypatch.setattr("tmdb_client.call_tmdb_api", my_mock)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id=1, how_many=3)
    assert movie_cast == ["actor1", "actor2", "actor3"]


@pytest.mark.parametrize('list_type, list_name', (
    ('movie/popular', 'popular'),
    ('movie/now_playing', 'now_playing'),
    ('movie/top_rated', 'top_rated'),
    ('movie/upcoming', 'upcoming'),
    ('trending/movie/day', 'trending_today'),
    ('trending/movie/week', 'trending_this_week')
))
def test_homepage(monkeypatch, list_type, list_name):
    api_mock = Mock(return_value={'results': [
                    'movie1', 'movie2', 'movie3', 'movie4', 'movie5', 'movie6', 'movie7', 'movie8', 'movie9', 'movie10']})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(
            '/', query_string={'list_type': list_name})
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)
