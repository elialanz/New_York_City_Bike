################################################ DIVVY BIKES DASHABOARD #########################################################

import streamlit as st
import pandas as pd 
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static 
from keplergl import KeplerGl
from datetime import datetime as dt

########################### Initial settings for the dashboard ##################################################################

st.set_page_config(page_title = 'Divvy Bikes Strategy Dashboard', layout='wide')
st.title("Divvy Bikes Strategy Dashboard")
st.markdown("The dashboard will help with the expansion problems Divvy currently faces")
st.markdown("Right now, Divvy bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")

########################## Import data ##########################################################################################

import os
import pandas as pd

# Absolute path to the folder where dashboard_01.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to your data folder
DATA_DIR = os.path.join(BASE_DIR, 'CB_Data', 'Prepared Data')

# Load data ONCE, correctly
df = pd.read_csv(os.path.join(DATA_DIR, 'reduced_data_to_plot.csv'), index_col=0)
top20 = pd.read_csv(os.path.join(DATA_DIR, 'top20.csv'), index_col=0)

########################################## DEFINE THE CHARTS ####################################################################

### Bar Chart ###

fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker={'color': top20['value'],'colorscale': 'Greens'}))
fig.update_layout(
    title = 'Top 20 most popular bike stations in New York',
    xaxis_title = 'Start stations',
    yaxis_title ='Sum of trips',
    width = 900, height = 600
)
st.plotly_chart(fig, use_container_width=True)

### Line Chart ### 

from plotly.subplots import make_subplots
import plotly.graph_objects as go

temp_trips = pd.read_csv(os.path.join(DATA_DIR, "temp_trips.csv"))

# Ensure date is datetime
temp_trips["trip_date"] = pd.to_datetime(temp_trips["trip_date"])
temp_trips = temp_trips.sort_values("trip_date")

fig_2 = make_subplots(specs=[[{"secondary_y": True}]])

# Bike trips (left axis)
fig_2.add_trace(
    go.Scatter(
        x=temp_trips["trip_date"],
        y=temp_trips["trip_totals"],
        name="Daily bike trips",
        mode="lines",
        line=dict(color="blue")
    ),
    secondary_y=False
)

# Temperature (right axis)
fig_2.add_trace(
    go.Scatter(
        x=temp_trips["trip_date"],
        y=temp_trips["avg_temp"],
        name="Daily temperature",
        mode="lines",
        line=dict(color="red")
    ),
    secondary_y=True
)

fig_2.update_layout(
    title="Daily bike trips and temperatures",
    height=600,
    xaxis_title="Date"
)

fig_2.update_yaxes(title_text="Bike trips", secondary_y=False)
fig_2.update_yaxes(title_text="Average temperature (°C)", secondary_y=True)

st.plotly_chart(fig_2, use_container_width=True)

### Add The Map ###

path_to_html = os.path.join(DATA_DIR, "NY_CitiBike_Trips_Map.html")

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Aggregated Bike Trips in New York")
st.components.v1.html(html_data,height=1000)