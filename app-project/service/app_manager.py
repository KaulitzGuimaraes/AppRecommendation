from model.App import App
import  random

class AppManager:
    def __init__(self,csv):
        self.csv = csv
        self.assembly_csv_in_a_dict()

    def assembly_csv_in_a_dict(self):
        app_array = []
        for index, row in self.csv.iterrows() :
            app = App(row.size_bytes,row.price,row.user_rating,row.track_name,row.prime_genre)
            app_array.append(app.get_dict())
        return  app_array[random.randint(0,len(app_array))]


