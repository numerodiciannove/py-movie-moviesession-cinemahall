from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return get_object_or_404(Movie, id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
