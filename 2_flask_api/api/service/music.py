from model.music import Music

class MusicService:
    def new(self, data):
        name = data['name']
        if (self.find_by_name(name)):
            print('Music already exists with name', name)
            raise FileExistsError
        music = Music(name, data['authorId'])
        print("Creating Music", music.json())
        music.save_to_db()
        return music.json()

    def find_by_name(self, name):
        print('Finding Music by name', name)
        music = list(map(lambda x: x.json(), Music.query.filter_by(name=name).all()))
        if not music:
            print('Music not found with name', name)
            return None
        print(music)
        return music
