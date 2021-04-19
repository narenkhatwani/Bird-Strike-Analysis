#import plotly.plotly as pl
import plotly.graph_objs as gobj
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)

#initializing the data variable
data = dict(type = 'choropleth',
            locations = ['india','nepal','china','pakistan','Bangladesh','bhutan','myanmar','srilanka','maharashtra'],
            locationmode = 'country names',
            colorscale= 'Portland',
            text= ['IND','NEP','CHI','PAK','BAN','BHU', 'MYN','SLK','MAH'],
            z=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
            colorbar = {'title':'Country Colours', 'len':200,'lenmode':'pixels' })

layout = dict(geo = {'scope':'asia'})

col_map = gobj.Figure(data = [data],layout = layout)

plot(col_map)