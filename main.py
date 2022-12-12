from flask import Flask, render_template, request, url_for
import tmdb_client
import random


app = Flask(__name__)


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    list_types = ['popular', 'now_playing', 'top_rated',
                  'upcoming', 'trending_today', 'trending_this_week']
    return render_template("homepage.html", movies=movies, list_types=list_types, selected_list=selected_list)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id, 8)
    movie_images = tmdb_client.get_movie_images(movie_id)
    backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, movie_cast=movie_cast, backdrop=backdrop)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
