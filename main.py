from flask import Flask, render_template
import requests

app = Flask(__name__)


def import_data():
    endpoint = "https://api.themoviedb.org/3/trending/movie/day"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTQzNGJiYjJjYTE1YThhMjJlMzMxNDMzNWVmYzkzYyIsInN1YiI6IjYzNzc3NDBjMTU2Y2M3MDA3NjMxMGQyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RXUlsdR3Qsx-y5PlKI8kocGgtqrR1XDvSBCby3lrx2w"
    headers = {
        "Authorisation": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    all_movies = response.json()['results']
    return all_movies


@ app.route('/')
def homepage():
    movies = []
    all_movies = import_data()
    for i in range(8):
        movies.append(all_movies[i])
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
