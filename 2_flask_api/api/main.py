from flask import Flask
from flask_restful import Api

from env import Env

from controller.author import GetAuthorByNameController, PostAuthorController
from controller.music import GetMusicByAuthorController, PostMusicController

# Carrega Variaveis de Ambiente
env = Env()

# Configura Banco de Dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env.dburi
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(env.track)
api = Api(app)

# Na primeira Requisição cria Banco de Dados
@app.before_first_request
def create_tables():
    db.create_all()

# Configura Rotas
api.add_resource(GetAuthorByNameController, '/author/<string:name>')
api.add_resource(PostAuthorController, '/author')
api.add_resource(GetMusicByAuthorController, '/musics/<int:authorId>')
api.add_resource(PostMusicController, '/music')

# Inicializa Banco de Dados e Inicializa Aplicação
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host=env.host, port=env.port, debug=env.debug())