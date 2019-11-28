from model.App import App
from file_handler.handler import FileHandler as ch

class AppManager:
    def __init__(self,csv):
        self.csv = csv
        self.desc_database = ch.read_json("./dataset/desc.json")

    def assembly_csv_in_a_dict(self):
        app_array = []
        for index, row in self.csv.iterrows() :
            app = App(row.size_bytes,row.price,row.user_rating,row.track_name,row.prime_genre,self.desc_database[str(row.id)])
            app_array.append(app.get_dict())
        return  app_array


