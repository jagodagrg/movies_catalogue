import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTQzNGJiYjJjYTE1YThhMjJlMzMxNDMzNWVmYzkzYyIsInN1YiI6IjYzNzc3NDBjMTU2Y2M3MDA3NjMxMGQyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RXUlsdR3Qsx-y5PlKI8kocGgtqrR1XDvSBCby3lrx2w"


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        endpoint = "https://api.themoviedb.org/3/movie/popular"
        response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_trending_movies_list(time_window):
    return call_tmdb_api(f"trending/movie/{time_window}")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type='popular'):
    if list_type == 'trending_today':
        data = get_trending_movies_list(time_window='day')
    elif list_type == 'trending_this_week':
        data = get_trending_movies_list(time_window='week')
    else:
        data = get_movies_list(list_type)
    return random.sample(data['results'], how_many)


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id, how_many):
    return call_tmdb_api(f"movie/{movie_id}/credits")['cast'][:how_many]


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")
