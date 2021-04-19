# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:33:26 2020

@author: Admin
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
# Load dataset
df = pd.read_csv("merged_final_TB - merged_final_TB.csv")
df1 = pd.read_csv("tbyearly.csv")

data=df[(df['Year']==2003)]
total = data['Total'].sum()
print(total)

data1=df[(df['Year']==2004)]
total1 = data1['Total'].sum()
print(total1)

data2=df[(df['Year']==2005)]
total2 = data2['Total'].sum()
print(total2)

data3=df[(df['Year']==2006)]
total3 = data3['Total'].sum()
print(total3)

data4=df[(df['Year']==2007)]
total4 = data4['Total'].sum()
print(total4)

data5=df[(df['Year']==2008)]
total5 = data5['Total'].sum()
print(total5)

data6=df[(df['Year']==2009)]
total6 = data6['Total'].sum()
print(total6)

data7=df[(df['Year']==2010)]
total7 = data7['Total'].sum()
print(total7)

data8=df[(df['Year']==2011)]
total8 = data8['Total'].sum()
print(total8)


# Initialize figure
fig = go.Figure()

# Add Traces

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=list(df.Rainfall),
               name="Rainfall",
               line=dict(color="#33CFA5")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=[df.Rainfall.mean()] * len(df.index),
               name="Rainfall Average",
               visible=False,
               line=dict(color="#33CFA5", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(df1.Year),
               y=list(df1.TotalCases),
               name="Total Cases",
               line=dict(color="#F06A6A")))

fig.add_trace(go.Scatter(x=list(df1.Year),y=[df1.TotalCases.mean()] * len(df1.index),name="Total CasesAverage",visible=False,line=dict(color="#F06A6A", dash="dash")))

# Add Annotations and Buttons
high_annotations = [dict(x="2016-03-01",
                         y=df.Rainfall.mean(),
                         xref="x", yref="y",
                         text="High Average:<br> %.2f" % df.Rainfall.mean(),
                         ax=0, ay=-40),
                    dict(x=df.Rainfall.idxmax(),
                         y=df.Rainfall.max(),
                         xref="x", yref="y",
                         text="Rainfall Max:<br> %.2f" % df.Rainfall.max(),
                         ax=0, ay=-40)]
low_annotations = [dict(x="2015-05-01",
                        y=df1.TotalCases.mean(),
                        xref="x", yref="y",
                        text="Total Cases Average:<br> %.2f" % df1.TotalCases.mean(),
                        ax=-40, ay=40),
                   dict(x=df.Rainfall.idxmin(),
                        y=df1.TotalCases.min(),
                        xref="x", yref="y",
                        text="Total Cases Min:<br> %.2f" % df1.TotalCases.min(),
                        ax=0, ay=40)]

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.2,
            buttons=list([
                dict(label="None",
                     method="update",
                     args=[{"visible": [True, False, True, False]},
                           {"title": "Tuberculosis",
                            "annotations": []}]),
                dict(label="Rainfall",
                     method="update",
                     args=[{"visible": [True, True, False, False]},
                           {"title": "Rainfall",
                            "annotations": high_annotations}]),
                dict(label="Total Cases",
                     method="update",
                     args=[{"visible": [False, False, True, True]},
                           {"title": "TotalCases",
                            "annotations": low_annotations}]),
                dict(label="Both",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Both Parameters",
                            "annotations": high_annotations + low_annotations}]),
            ]),
        )
    ])

# Set title
fig.update_layout(
    title_text="Tuberculosis",
    xaxis_domain=[0.05, 1.0]
)

fig.show()
plot(fig)
