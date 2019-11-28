from service.app_manager import  AppManager
import  pandas as pd

df = pd.read_csv("./dataset/AppleStore.csv")

# appmmgnt = AppManager(df)
buffer = set()
for i in df["prime_genre"] :
    buffer.add(i)

print(buffer)
print(len(buffer))
