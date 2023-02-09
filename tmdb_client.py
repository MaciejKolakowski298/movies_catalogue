import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5NmU2OTBlZTdkMzA0MTc2OGYyMGE4ODFhMmRmN2IyOCIsInN1YiI6IjYzZTE1MDJkYTMxM2I4MDBiYzE2ZjU3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.t5B3vtcizcbM0YVoAdJyQnZNNTDlseOuqdWgo3rzkxM"


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()



def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

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
    return response.json()["cast"][:8]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



