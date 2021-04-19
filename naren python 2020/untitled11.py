import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_numeric
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
data_naren=pd.read_csv("bird1.csv")
data_naren12=pd.read_csv("bird.csv")
data_naren21=pd.read_csv("bird.csv")

chars_to_remove = [',']
cols_to_clean = ['Feet above ground','Cost: Total $']
for col in cols_to_clean:
    for char in chars_to_remove:
        data_naren[col] = data_naren[col].str.replace(char, '')
        data_naren12[col] = data_naren12[col].str.replace(char, '')
        data_naren21[col] = data_naren21[col].str.replace(char, '')
    data_naren[col] = to_numeric(data_naren[col])
    data_naren12[col] = to_numeric(data_naren12[col])
    data_naren21[col] = to_numeric(data_naren21[col])
data_naren.dropna(axis=1)
data_naren12.dropna(axis=1)
data_naren21.dropna(axis=1)


'''
#feature for comparison of incident data and thier damage cost
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data_naren['FlightDate'], y=data_naren['Cost: Total $'], name="COND REF PRESS COMP1",line_color='deepskyblue'))

#fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['COND REF PRESS COMP2'], name="COND REF PRESS COMP2",line_color='dimgray'))

fig1.update_layout(title_text='Time Series with Rangeslider',xaxis_rangeslider_visible=True)
fig1.show()
plot(fig1)


'''
'''
p1=data_naren['Year']

a=0
alist=[]
for i in p1:
    if (i=='2005'):
        alist.append(0)
    else:
        a=0
x1=len(alist)
'''



'''


fig = px.line(data_naren, x='Year', y='Miles from airport')
fig.show()
plot(fig)
'''
p1=data_naren['Year']

a=0
alist=[]
for i in p1:
    if (i==2005):
        alist.append(0)
    else:
        a=0
x1=len(alist)

b=0
blist=[]
for i in p1:
    if (i==2006):
        blist.append(0)
    else:
        b=0
x2=len(blist)

c=0
clist=[]
for i in p1:
    if (i==2007):
        clist.append(0)
    else:
        c=0
x3=len(clist)

d=0
dlist=[]
for i in p1:
    if (i==2008):
        dlist.append(0)
    else:
        d=0
x4=len(dlist)

e=0
elist=[]
for i in p1:
    if (i==2009):
        elist.append(0)
    else:
        e=0
x5=len(elist)

f=0
flist=[]
for i in p1:
    if (i==2010):
        flist.append(0)
    else:
        f=0
x6=len(flist)

g=0
glist=[]
for i in p1:
    if (i==2011):
        glist.append(0)
    else:
        g=0
x7=len(glist)


x = ['2005','2006','2007','2008','2009','2010','2011']
    
popularity = [x1,x2,x3,x4,x5,x6,x7]
x_pos = [i for i, _ in enumerate(x)]
        
fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='b')
plt.xlabel("Years")
plt.title("Count of Birdstrikes")
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


fig = {
    "data": [{"type": "bar",
              "x": ['2005','2006','2007','2008','2009','2010','2011'],
              "y": [x1,x2,x3,x4,x5,x6,x7]}],
    "layout": {"title": {"text": "A Bar Chart"}}
}

# To display the figure defined by this dict, use the low-level plotly.io.show function
import plotly.io as pio
pio.show(fig)
plot(fig)