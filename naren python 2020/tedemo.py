import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_numeric

data_naren=pd.read_csv("bird.csv")
data_naren.dropna(axis=1)
total_rows=len(data_naren.axes[0])
warning=data_naren['Pilot warned of birds or wildlife?']


ylist=[]
for x in warning:
    if (x=='Y'):
        ylist.append(0)
    else:
        y=0
        
county=ylist.count(0)
    
n=0
nlist=[]
for x in warning:
    if (x=='N'):
        nlist.append(0)
    else:
        b=0
        
countn=nlist.count(0)

x1=data_naren.loc[(data_naren['Pilot warned of birds or wildlife?']=='Y'),['Record ID']].count()
x2=data_naren.loc[(data_naren['Pilot warned of birds or wildlife?']=='N'),['Record ID']].count()
x3=total_rows-(countn+county)
y=0



per1=(county/total_rows)*100 #percentage birdstrike in mumbai
print(per1)

per2=(countn/total_rows)*100 #percentage birdstrike in mumbai
print(per2)

per6=((total_rows-(county+countn))/total_rows)*100 #percentage overseas birdstrike
print(per6)

x = ['Yes', 'No', 'No information']
popularity = [x1, x2, x3]
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='g')
plt.xlabel("Pilots Warning Status")
plt.ylabel("Number of Warnings")
plt.title("Pilot Warnings for Bird Strikes")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linewidth='0.5', color='blue')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%f' % float(height),ha='center', va='bottom')
autolabel(rects1)

plt.show()

