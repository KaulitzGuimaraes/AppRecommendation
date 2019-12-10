from sklearn.cluster import KMeans
class KmeansModel :
    def __init__(self,csv,n_clusters=6):
        self.csv = csv
        self.n_clusters = n_clusters
        self.train_model()

    def train_model(self):
        pass

    def get_clusters(self):
        return  self.kmeans_values
