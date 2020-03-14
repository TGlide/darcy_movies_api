from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier', read_only=True)
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class MovieDto:
    api = Namespace('movie', description='movie related operations')
    movie = api.model('movie', {
        'id': fields.String(readonly=True, description='Movie id'),
        'title': fields.String(required=True, description='Movie title'),
        'imdb_title': fields.String(description='Movie title on IMDb'),
        'catalogue_entry': fields.String(required=True, description='Movie entry on Darcy original catalogue'),
        'rating': fields.Float(description='Movie rating on IMDb'),
        'cover': fields.String(description='Movie cover on IMDb'),
        'registered_on': fields.String(readonly=True, description='Movie registration date and time on API'),
    })
