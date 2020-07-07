from flask_restful import Resource, reqparse
from service.author import AuthorService

class GetAuthorByNameController(Resource):
    def get(self, name):
        service = AuthorService()
        author = service.find_by_name(name)
        if not author:
            return {'message': 'Author not found'}, 404
        return author, 200

class PostAuthorController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help='Name of Author.'
    )

    def post(self):
        data = PostAuthorController.parser.parse_args()
        service = AuthorService()

        if service.find_by_name(data['name']):
            return {'message': 'Author already exists'}, 409
        return service.new(data), 201
