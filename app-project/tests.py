from service.app_manager import  AppManager
import  pandas as pd
import  random
import  json
from machine_learning.Kmeans import KmeansModel
df = pd.read_csv("./dataset/AppleStore.csv")
del df['Unnamed: 0']
del df['id']
del df['track_name']
del df['prime_genre']
del df['cont_rating']
del df['currency']
del df['sup_devices.num']
del  df['ver']
km = KmeansModel(df)
b = km.get_clusters()
a ={}


df = pd.read_csv("./dataset/appleStore_description.csv")
for i in df.values :
    a[i[0]] = i[-1]


with open("./dataset/desc.json","w") as l :
        l.write(json.dumps(a,indent=4))

# # appmmgnt = AppManager(df)
# buffer = set()
# for i in df["prime_genre"] :
#     buffer.add(i)
#
# buffer2 ={}
# for i in buffer :
#     buffer2[i] = ""
#
# a = json.dumps(buffer2,indent=4)
#
# #
# for i in df.values[0] :
#     if type(i) == type('oi') :
#         print(i)
#
# print(df.head())

# # print (random.randint(1,101))
#
# with open("./dataset/image_url.json","w") as l :
#     l.write(a)

# print()