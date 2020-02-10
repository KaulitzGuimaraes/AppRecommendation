from model.App import App
from file_handler.handler import FileHandler as ch


class AppManager:
    def __init__(self, csv):
        self.csv = csv
        self.desc_database = ch.read_json("./dataset/desc.json")

    def assembly_csv_in_a_dict(self, index_array=None):
        app_array = []
        if not index_array:
            for index, row in self.csv.iterrows():
                app = App(index,
                          row.size_bytes,
                          row.price,
                          row.user_rating,
                          row.currency,
                          row.track_name,
                          row.prime_genre,
                          row.cont_rating,
                          self.desc_database[str(row.id)])
                app_array.append(app.get_dict())
        else:
            for index, row in self.csv.iterrows():
                if index in index_array:
                    app = App(index,
                              row.size_bytes,
                              row.price,
                              row.user_rating,
                              row.currency,
                              row.track_name,
                              row.prime_genre,
                              row.cont_rating,
                              self.desc_database[str(row.id)])
                    app_array.append(app.get_dict())
        return app_array
