from flask_restplus import Namespace, Resource
from models import Person
from flask import jsonify


api = Namespace('Person', 'Api person')

@api.route('')
@api.response(200, 'Success')
@api.response(401, 'Unauthorized')
@api.response(404, 'Url Not Found')
@api.response(400, 'Bad Request')
@api.response(500, 'Internal Server Error')
@api.response(403, 'Forbidden')
class PersonRoute(Resource):

    def get(self):
        persons = Person.query.all()

        person_responses = []

        for person in persons:
            person_responses.append({'id': person.id, 'name': person.name, 'address': person.address})

        return jsonify(person_responses)


@api.route('/<int:id>')
@api.response(200, 'Success')
@api.response(401, 'Unauthorized')
@api.response(404, 'Url Not Found')
@api.response(400, 'Bad Request')
@api.response(500, 'Internal Server Error')
@api.response(403, 'Forbidden')
class PersonDetailRoute(Resource):

    def get(self, id):

        person = Person.query.filter_by(id=id).first()

        return jsonify({'id': person.id, 'name': person.name, 'address': person.address})