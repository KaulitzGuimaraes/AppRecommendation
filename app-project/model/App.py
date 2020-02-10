from file_handler.handler import FileHandler as ch
class App :
    def __init__(self,index,
                          size_bytes,
                          price,
                          user_rating,
                          currency,
                          name,
                          prime_genre,
                          cont_rating,
                           desc):
        self.index = index
        self.size_bytes = size_bytes
        self.price = price
        self.user_rating = user_rating
        self.name = name
        self.currency = currency
        self.user_rating = user_rating
        self.image_url = ch.read_json()[prime_genre]
        self.cont_rating = cont_rating
        self.desc = desc
        self.prime_genre = prime_genre

    def get_dict(self):
        return {
            'index' : self.index,
            'sizeMb': int(int(self.size_bytes)/1000000),
            'price' : self.price,
            'userRating' : self.user_rating,
            'cont_rating' : self.cont_rating,
            'currency' : self.currency,
            'name' : self.name,
            'primeGenre' : self.prime_genre,
            'imageUrl' : self.image_url,
            'desc' : self.desc
        }