from flask_restful import Resource, reqparse
from service.music import MusicService

class GetMusicByAuthorController(Resource):
    def get(self, authorId):
        service = MusicService()
        musics = service.find_by_author(authorId)
        if not musics:
            return {'message': 'Music not found'}, 404
        return musics, 200

class PostMusicController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help='Name of Music.'
    )
    parser.add_argument('authorId',
        type=int,
        required=True,
        help='Author Identification.'
    )

    def post(self):
        data = PostMusicController.parser.parse_args()
        service = MusicService()

        if service.find_by_name(data['name']):
            return {'message': 'Music already exists'}, 409
        return service.new(data), 201
