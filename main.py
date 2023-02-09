from flask import Flask, render_template, redirect

import tmdb_client ,random

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=50,list_type='popular')
    return render_template("homepage.html", movies=random.sample(movies,8),list_type='popular')

@app.route('/Teraz_w_kinach')
def now_playing():
    movies = tmdb_client.get_movies(how_many=50,list_type='now_playing')
    return render_template("homepage.html", movies=random.sample(movies,8),list_type='now_playing')

@app.route('/Nadchodzace')
def upcoming():
    movies = tmdb_client.get_movies(how_many=50,list_type='upcoming')
    return render_template("homepage.html", movies=random.sample(movies,8),list_type='upcoming')

@app.route('/Najwyzej_oceniane')
def top_rated():
    movies = tmdb_client.get_movies(how_many=50,list_type='top_rated')
    return render_template("homepage.html", movies=random.sample(movies,8),list_type='top_rated')

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(images['backdrops'])
    print(selected_backdrop)
    return render_template("movie_details.html", movie=details, cast=cast, image=selected_backdrop)

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)