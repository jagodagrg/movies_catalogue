import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTQzNGJiYjJjYTE1YThhMjJlMzMxNDMzNWVmYzkzYyIsInN1YiI6IjYzNzc3NDBjMTU2Y2M3MDA3NjMxMGQyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RXUlsdR3Qsx-y5PlKI8kocGgtqrR1XDvSBCby3lrx2w"


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        endpoint = "https://api.themoviedb.org/3/movie/popular"
        response = requests.get(endpoint, headers=headers)
    return response.json()


def get_trending_movies_list(time_window):
    endpoint = f"https://api.themoviedb.org/3/trending/movie/{time_window}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

# ta funkcja jest do zrobienia w zadaniu, ale potem jest już zbędna moim zdaniem
# def get_movie_info():
#    movies = get_movies()['results']
#    for movie in movies:
#        movie_info[movie['title']] = movie['poster_path']
#    return movie_info


def get_movies(how_many, list_type='popular'):
    if list_type == 'trending_today':
        data = get_trending_movies_list(time_window='day')['results']
    elif list_type == 'trending_this_week':
        data = get_trending_movies_list(time_window='week')['results']
    else:
        data = get_movies_list(list_type)['results']
    return random.sample(data, how_many)


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
