import  pandas as pd
import json
class FileHandler :
    @classmethod
    def read_csv(cls,path="./dataset/AppleStore.csv"):
        return pd.read_csv(path)

    @classmethod
    def read_json(cls,path="./dataset/image_url.json"):
        with open(path,'r') as l:
            return json.loads(l.read())





