import pandas as pd


data_naren=pd.read_csv("bird.csv")  
species=data_naren['Wildlife: Species']

rows = data_naren['Wildlife: Species']

result = []

for r in rows:
    key = r
    if key not in result:
        result.append(r)


print(len(result))