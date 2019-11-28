from service.app_manager import  AppManager
import  pandas as pd
import  random
import  json
df = pd.read_csv("./dataset/AppleStore.csv")

# appmmgnt = AppManager(df)
buffer = set()
for i in df["prime_genre"] :
    buffer.add(i)

buffer2 ={}
for i in buffer :
    buffer2[i] = ""

a = json.dumps(buffer2,indent=4)

#
# print(df.columns)

# print (random.randint(1,101))

with open("./dataset/image_url.json","w") as l :
    l.write(a)