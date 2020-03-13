from ..service.movie_service import save_new_movie, get_all_movies, get_a_movie, delete_a_movie
from ..util.dto import MovieDto
from ..util.decorator import token_required, admin_token_required

from flask_restplus import Resource
from flask import request


api = MovieDto.api
_movie = MovieDto.movie


@api.route('/')
@api.param('rating_order', 'Order by rating, asc or dsc')
@api.param('title', 'Search by title')
class MovieList(Resource):
    @api.doc('list_of_registered_movies')
    @api.marshal_list_with(_movie, envelope='data')
    def get(self):
        """List all registered movies"""
        return get_all_movies(request.args)

    @api.response(201, 'Movie successfully created.')
    @api.doc('create a new movie')
    @api.expect(_movie, validate=True)
    @admin_token_required
    def post(self):
        """Creates a new Movie """
        data = request.json
        return save_new_movie(data=data)


@api.route('/<id>')
@api.param('id', 'The Movie identifier')
@api.response(404, 'Movie not found.')
class Movie(Resource):
    @api.doc('get a movie')
    @api.marshal_with(_movie)
    def get(self, id):
        """get a movie given its identifier"""
        movie = get_a_movie(id)
        if not movie:
            api.abort(404)
        else:
            return movie

    @api.doc('delete a movie')
    @admin_token_required
    def delete(self, id):
        """delete a movie given its identifier"""
        movie = get_a_movie(id)
        if not movie:
            api.abort(404)
        else:
            return delete_a_movie(movie)
