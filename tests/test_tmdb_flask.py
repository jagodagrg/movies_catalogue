from main import app
from unittest.mock import Mock
import tmdb_client
import pytest


@pytest.mark.parametrize('list_type', (
    ('movie/popular'),
    ('movie/now_playing'),
    ('movie/top_rated'),
    ('movie/upcoming'),
    ('trending/movie/day'),
    ('trending/movie/week')
))
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': [
                    'movie1', 'movie2', 'movie3', 'movie4', 'movie5', 'movie6', 'movie7', 'movie8', 'movie9', 'movie10']})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)
