import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn


df = pd.read_csv("C:\\Datasets\\internshipdataset1.csv")

# Draw Plot
def plot_df(df, x, y, title="dd", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

dataset_1 = pd.read_csv('C:\\Datasets\\internshipdataset1.csv')  # First File
dataset_2 = pd.read_csv('C:\\Datasets\\Dataset2.csv')  # Second File
dataset_1 = dataset_1.drop_duplicates()
dataset_1.drop(dataset_1[dataset_1['Installs'] == 'Free'].index, inplace = True)
dataset_1.drop(dataset_1[dataset_1['Category'] == '1.9'].index, inplace = True)
dataset_1['Size'] = dataset_1['Size'].apply(lambda x: str(float(x.replace('k', '')) / 1000) if 'k' in x else x)
dataset_1['Size'] = dataset_1['Size'].replace('Varies with device', nan)
chars_to_remove = ['+', ',', 'M', '$']
cols_to_clean = ['Installs', 'Size', 'Price']
for col in cols_to_clean:
    for char in chars_to_remove:
        dataset_1[col] = dataset_1[col].str.replace(char, '')    
dataset_1[col] = to_numeric(dataset_1[col])

dataset_1 = dataset_1[notnull(dataset_1['Rating'])]
dataset_1 = dataset_1[notnull(dataset_1['Size'])]
dataset_1 = dataset_1[notnull(dataset_1['Android Ver'])]
dataset_2 = dataset_2[notnull(dataset_2['Translated_Review'])]
dataset_2 = dataset_2[notnull(dataset_2['Sentiment'])]
dataset_2 = dataset_2[notnull(dataset_2['Sentiment_Polarity'])]
dataset_2 = dataset_2[notnull(dataset_2['Sentiment_Subjectivity'])]
    





import plotly.express as px

import pandas as pd

fig = px.line(dataset_1, x='Category', y='Last Updated')
fig.show()