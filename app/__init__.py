# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.movie_controller import api as movie_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Darcy Movies API',
          version='1.0',
          description='API for Darcy Movies App built with Flask RESTPlus and JWT'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(movie_ns, path='/movie')
api.add_namespace(auth_ns)
