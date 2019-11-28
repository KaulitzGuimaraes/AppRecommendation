## TODO : clean and transform the csv
import pandas as pd
import numpy as np


app_dataset = pd.read_csv("dataset/AppleStore.csv")
app_dataset_to_use = app_dataset

del app_dataset_to_use["ver"]
del app_dataset_to_use["vpp_lic"]
del app_dataset_to_use["sup_devices.num"]
del app_dataset_to_use["ipadSc_urls.num"]
del app_dataset_to_use["lang.num"]

prime_genre_values = set()

for track_set in app_dataset_to_use["prime_genre"]    :
    prime_genre_values.add(track_set)
prime_genre_values = list(prime_genre_values)

prime_genres = app_dataset_to_use["prime_genre"]

app_dataset_to_use["prime_genre"] = prime_genres.apply(prime_genre_values.index)