import  pandas as pd
import json
class FileHandler :
    @classmethod
    def read_csv(cls,path="../dataset/AppleStore.csv"):
        return pd.read_csv(path)

    @classmethod
    def read_json(cls,path="../dataset/image_url.json"):
        with open(path,'r') as l:
            return json.loads(l.read())
    
app_dataset = FileHandler.read_csv()
app_dataset_to_use = app_dataset

del app_dataset_to_use["ver"]
del app_dataset_to_use["vpp_lic"]
del app_dataset_to_use["sup_devices.num"]
del app_dataset_to_use["ipadSc_urls.num"]
del app_dataset_to_use["lang.num"]

prime_genre_values = set()
currency_values = set()

for track_set in app_dataset_to_use["prime_genre"]    :
    prime_genre_values.add(track_set)
prime_genre_values = list(prime_genre_values)

for value_set in app_dataset_to_use["currency"] :
    currency_values.add(value_set)
currency_values = list(currency_values)

prime_genres = app_dataset_to_use["prime_genre"]
original_currency = app_dataset_to_use["currency"]

app_dataset_to_use["prime_genre"] = prime_genres.apply(prime_genre_values.index)
app_dataset_to_use["currency"] = original_currency.apply(currency_values.index)
app_dataset_to_use.to_csv("../dataset/AppleStoreTransformed.csv")