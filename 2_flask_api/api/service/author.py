from model.author import Author

class AuthorService:
    def new(self, data):
        name = data['name']
        if (self.find_by_name(name)):
            print('Author already exists with name', name)
            raise FileExistsError
        author = Author(name)
        print('Creating Author', author.json())
        author.save_to_db()
        return author.json()

    def find_by_name(self, name):
        print('Finding Author by name', name)
        author = list(map(lambda x: x.json(), Author.query.filter_by(name=name).all()))
        if not author:
            print('Author not found with name', name)
            return None
        print(author)
        return author
