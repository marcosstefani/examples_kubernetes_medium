import os
from enum import Enum

class Variable(Enum):
    API_ENV = 'dev'
    API_HOST_MUSIC = '0.0.0.0'
    API_PORT_MUSIC = '8080'
    DATABASE_URI = 'sqlite:///dev.db'
    DATABASE_TRACK = 'True'

def _find(env):
    try:
        return os.environ[env.name]
    except KeyError:
        print('Environment {name} not found, the default value is {value}'.format(name=env.name, value=env.value))
    return env.value

def _db_uri():
    try:
        db_name = os.environ['POSTGRES_DB']
        db_user = os.environ['POSTGRES_USER']
        db_pass = os.environ['POSTGRES_PASSWORD']
        return 'postgresql://{username}:{password}@postgres/{database}'.format(username=db_user, password=db_pass, database=db_name)
    except KeyError:
        print('Database Environment not found')
    return _find(Variable.DATABASE_URI)

class Env:
    def __init__(self):
        self.name = _find(Variable.API_ENV)
        self.host = _find(Variable.API_HOST_MUSIC)
        self.port = _find(Variable.API_PORT_MUSIC)
        self.dburi = _db_uri()
        self.track = _find(Variable.DATABASE_TRACK)
    
    def debug(self):
        return self.name == Variable.API_ENV.value
