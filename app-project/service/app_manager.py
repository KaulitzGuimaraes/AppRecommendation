from model.App import App


class AppManager:
    def __init__(self,csv):
        self.csv = csv
        self.apps = dict()
        self.assembly_csv_in_a_dict()

    def assembly_csv_in_a_dict(self):
        for index, row in self.csv.iterrows() :
            app = App(row.size_bytes,row.price,row.user_rating,row.track_name)
            self.apps[row.track_name] = app

