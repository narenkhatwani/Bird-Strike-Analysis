import seaborn as sns 
import numpy as np
from sklearn.decomposition import PCA
import math
import datetime
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data_naren=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")

data_naren['Installs']=data_naren['Installs'].map(lambda x:x.rstrip('+'))
data_naren['Installs']=data_naren['Installs'].map(lambda x:''.join(x.split(',')))


data_naren['quarter_year'] = pd.to_datetime(data_naren['Last Updated']).dt.to_period('Q')
plt.xticks(rotation=90)
sns.countplot(data_naren['Category'],hue=data_naren['quarter_year'])
























x10=data_naren.loc[(data_naren['Installs']=='500000')&(data_naren['quarter_year']=='2018Q3'),['Installs','App']]

print(x10)
