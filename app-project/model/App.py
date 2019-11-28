class App :
    ## TODO : add the features from CSV as attributes.
    ## TODO :  add the description as attribute.
    ## TODO : add the image flag as attribute
    def __init__(self,size_bytes,price,user_rating,name):
        self.size_bytes = size_bytes
        self.price = price
        self.user_rating = user_rating
        self.name = name
        self.image_url = None
        self.desc = None

