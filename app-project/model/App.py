from file_handler.handler import FileHandler as ch
class App :
    def __init__(self,size_bytes,price,user_rating,name,prime_genre,desc):
        self.size_bytes = size_bytes
        self.price = price
        self.user_rating = user_rating
        self.name = name
        self.image_url = ch.read_json()[prime_genre]

        self.desc = desc
        self.prime_genre = prime_genre

    def get_dict(self):
        return {
            'sizeBytes': self.size_bytes,
            'price' : self.price,
            'userRating' : self.user_rating,
            'name' : self.name,
            'primeGenre' : self.prime_genre,
            'imageUrl' : self.image_url,
            'desc' : self.desc
        }