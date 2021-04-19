from tkinter import *
from tkinter import messagebox
import re,pymysql
from tkinter import Tk
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from seaborn import regplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from openpyxl import *
from tkinter import *
from tkinter import messagebox
import re , pymysql
from tkinter import Tk
from PIL import ImageTk, Image 
from matplotlib.pyplot import title
from matplotlib.pyplot import subplots
from matplotlib.pyplot import subplot
from numpy import array
from numpy import mean
from numpy import nan
from pandas import read_csv
from pandas import to_numeric
from pandas import notnull
from fractions import Fraction
from matplotlib.pyplot import bar
from matplotlib.pyplot import ylim
from matplotlib.pyplot import xlabel
from matplotlib.pyplot import ylabel
from matplotlib.pyplot import title
from matplotlib.pyplot import xticks
from matplotlib.pyplot import subplots
from matplotlib.pyplot import subplot
from matplotlib.pyplot import show
from matplotlib.pyplot import scatter
from matplotlib.pyplot import plot
from matplotlib.pyplot import tight_layout
from seaborn import barplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import BOTH
from tkinter import BOTTOM
from tkinter import TOP
from tkinter import Text
from tkinter import END
from tkinter import Label
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter import W
from tkinter import Entry
from csv import writer
from PIL import ImageTk, Image


data_naren=pd.read_csv("C:\\Datasets\\apy.csv")
data_harsh=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
data_priya=pd.read_csv("C:\\Datasets\\Dataset2.csv")
data_naren.sort_values(["Crop_Year"], axis=0,ascending=True, inplace=True)

data_naren.dropna(axis=1)


plt.plot(data_naren['Crop_Year'],data_naren['Production'], color='g')
#plt.plot(year, pop_india, color='orange')
plt.xlabel('Years')
plt.ylabel('Population in million')
plt.title('Production from 1997 to 2015')
plt.show()