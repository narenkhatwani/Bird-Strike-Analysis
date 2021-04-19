import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_numeric

data_naren=pd.read_csv("bird.csv")



p1=data_naren['When: Phase of flight']

p=0
p1list=[]
for i in p1:
    if (i=='Climb'):
        p1list.append(0)
    else:
        p=0
x1=len(p1list)



q=0
p2list=[]
for j in p1:
    if (j=='Take-off run'):
        p2list.append(0)
    else:
        q=0

x2=len(p2list)


r=0
p3list=[]
for k in p1:
    if (k=='Landing Roll'):
        p3list.append(0)
    else:
        r=0

x3=len(p3list)

s=0
p4list=[]
for k in p1:
    if (k=='Approach'):
        p4list.append(0)
    else:
        s=0
x4=len(p4list)

t=0
p5list=[]
for k in p1:
    if (k=='Taxi'):
        p5list.append(0)
    else:
        t=0
x5=len(p5list)

total_rows=len(data_naren.axes[0])

unknown=(total_rows-(x1+x2+x3+x4+x5))

x = ['Climb','Take-off run','Landing Roll','Approach','Taxi','Unknown']

popularity = [x1,x2,x3,x4,x5,unknown]
x_pos = [i for i, _ in enumerate(x)]
    
fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='b')
plt.xlabel("Phase of Flight")
plt.title("Count of Birdstrikes as per Phases of Flight")
plt.xticks(x_pos, x)
    # Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linewidth='0.5', color='red')
    # Customize the minor grid
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % float(height),ha='center', va='bottom')
autolabel(rects1)

plt.show()