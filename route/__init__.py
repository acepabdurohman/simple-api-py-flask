from flask import Blueprint
from flask_restplus import Api
from .person_api import api as person_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Testing API Documentation', 
    version='v1', description='Simple API example using flask')

api.add_namespace(person_api, '/person')