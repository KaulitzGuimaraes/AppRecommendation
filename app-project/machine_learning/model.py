from sklearn.cluster import KMeans

from file_handler.handler import FileHandler as ch

class KmeansModel :
    def __init__(self,csv_raw, csv_t,n_clusters=6):
        self.csv_raw = csv_raw
        self.csv_t = self.delete_values(csv_t)
        self.n_clusters = n_clusters
        self.train_model()
        self.get_clusters()

    def delete_values(self,svc):
        del svc['track_name']
        del svc['id']
        del svc['cont_rating']
        return  svc
    def train_model(self):
        self.kmeans = KMeans(n_clusters=self.n_clusters)
        print(self.csv_t.values.shape)
        self.kmeans.fit(self.csv_t.values)
        self.kmeans_values = self.kmeans.predict(self.csv_t.values)
    def get_clusters(self):
        l = []
        for i in range(self.n_clusters) :
            l.append([])
        i = 0
        for k in self.kmeans_values :
            l[k].append(i)
            i+=1
        self.l = l

    def get_cluster(self,index):
        try:
            index = int(index)
            values = self.csv_t.values[index].reshape(1, -1)
            cluster = self.kmeans.predict(values)
            return self.l[cluster[0]]
        except Exception as e :
            print(str(e))







