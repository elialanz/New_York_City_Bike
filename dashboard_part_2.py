################################################ DIVVY BIKES DASHABOARD #########################################################

import streamlit as st
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
from datetime import datetime as dt
from PIL import Image
from numerize.numerize import numerize

########################### INITIAL SETTINGS FOR THE DASHBOARD ##################################################################

st.set_page_config(page_title = 'Divvy Bikes Strategy Dashboard', layout='wide')
st.title("Divvy Bikes Strategy Dashboard")

### Define side bar ###
st.sidebar.title("Select Page")
page = st.sidebar.selectbox('Select an aspect of the analysis',
  ["Introduction", "Weather and Bike Trips", "Bike Trips By Hours",
   "Most Popular Stations", "Interactive Map with Bike Trips", "Recommendations"])

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            background-color: #e8f5e9;
        }
    </style>
    """,
    unsafe_allow_html=True
)

########################### CREATING A DROPDOWN MENU ############################################################################

df = pd.read_csv('reduced_data_to_plot_small.csv')
df['date'] = pd.to_datetime(df['date'])
top20_csv = pd.read_csv('top20.csv')
temp_trips = pd.read_csv('temp_trips.csv')
temp_trips['trip_date'] = pd.to_datetime(temp_trips['trip_date'])
hourly_trips = pd.read_csv('hourly_trips.csv')

######################################### DEFINE THE PAGES #####################################################################


################################################## INTRO PAGE ##################################################

if page == "Introduction":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Divvy Bikes currently faces.")
    st.markdown("Right now, Divvy bikes runs into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 5 sections:")
    st.markdown("- Weather and Bike Trips")
    st.markdown("- Bike Trips By Hours")
    st.markdown("- Most Popular Stations")
    st.markdown("- Interactive Map with Bike Trips")
    st.markdown("- Recommendations")
    st.markdown("The dropdown menu on the left 'Select Page' will take you to the different aspects of the analysis our team looked at.")

    myImage = Image.open("divvy_bikes.jpg")
    st.image(myImage)

################################################## SECOND PAGE WEATHER/TRIPS ##################################################

elif page == 'Weather and Bike Trips':

    fig_2 = make_subplots(specs = [[{"secondary_y": True}]])

    fig_2.add_trace(
    go.Scatter(
        x=temp_trips['trip_date'],
        y=temp_trips['trip_totals'],
        name='Daily bike rides',
        line=dict(color='green')),
    secondary_y=False)
    
    fig_2.add_trace(
    go.Scatter(
            x=temp_trips['trip_date'],
            y=temp_trips['avg_temp'],
            name='Daily temperature',
            line=dict(color='red')),
    secondary_y=True)

    fig_2.update_layout(
    title = 'Daily bike trips and temperatures in 2022',
    height = 400
    )

    st.plotly_chart(fig_2, use_container_width=True)
    st.markdown("---")
    
    st.markdown("## 📊 Daily Bike Trips vs Temperature (2022)")
    
    st.markdown(
    """
    <div style="font-size:18px; line-height:1.6;">
    
    <strong>Key insight:</strong> Bike ridership closely follows temperature patterns throughout the year, with strong seasonality visible across all months.<br>
    
    Daily bike trips increase steadily from winter into spring and peak during the summer months (June–August), when temperatures are consistently warmer. This highlights a strong positive relationship between weather conditions and cycling activity.<br>
    
    From September onwards, both temperatures and bike usage decline, with the sharpest drops occurring during late autumn and winter. Short-term fluctuations during warmer months may be influenced by external factors such as rainfall, extreme heat, or operational disruptions.<br>
    
    Overall, temperature emerges as a key driver of bike demand, reinforcing the importance of seasonal planning for bike availability, maintenance, and operational staffing.
    
    </div>
    """,
    unsafe_allow_html=True
    )

################################################## THIRD PAGE BIKE TRIPS PER HOUR ##################################################

elif page == "Bike Trips By Hours":

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=hourly_trips["hour"],
            y=hourly_trips["trip_count"],
            mode="lines+markers",
            name="Trips"
        )
    )

    fig.update_layout(
        title="Bike Trips by Hour of Day",
        xaxis_title="Hour (0–23)",
        yaxis_title="Number of Trips",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    
    st.markdown("## ⏱️ Bike Trips by Hour of Day")
    
    st.markdown(
    """
    <div style="font-size:18px; line-height:1.7;">
    
    <strong>Key insight:</strong> Bike usage follows a clear daily rhythm, reflecting commuter behaviour and leisure patterns throughout the day.<br><br>
    
    Trips are lowest during the early morning hours when demand is minimal. Usage begins to rise sharply from around <strong>06:00</strong>, coinciding with morning commuting activity.<br><br>
    
    A sustained increase is visible through the afternoon, with peak demand occurring in the <strong>late afternoon and early evening (16:00–18:00)</strong>. This aligns with return home commutes, recreational riding, and higher urban activity levels.<br><br>
    
    After <strong>19:00</strong>, trip volumes steadily decline as the city transitions into evening and night time hours.<br><br>
    
    <strong>Operational implication:</strong> These patterns suggest that bike availability, rebalancing efforts, and staffing should be prioritised during morning and evening peak hours to reduce shortages and improve service reliability.
    
    </div>
    """,
    unsafe_allow_html=True
    )

################################################## 4TH PAGE POPULAR STATIONS ##################################################

# Create the season variable

elif page == 'Most Popular Stations':
    
    # Create the filter on the side bar
    
    with st.sidebar:
        season_filter = st.multiselect(label= 'Select the season', options=df['season'].unique(),
    default=df['season'].unique())

    df1 = df.query('season in @season_filter').copy()
    
    # Define the total rides
    total_rides = len(df1)   
    st.metric(label = 'Total Bike Rides', value= numerize(total_rides))

    # Bar chart

    df1['value'] = 1 
    df_groupby_bar = df1.groupby('start_station_name', as_index = False).agg({'value': 'sum'})
    top20 = df_groupby_bar.nlargest(20, 'value')
    fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value']))

    fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker={'color':top20['value'],'colorscale': 'Greens'}))
    fig.update_layout(
    title = 'Top 20 most popular bike stations in New York',
    xaxis_title = 'Start stations',
    yaxis_title ='Sum of trips',
    width = 900, height = 600
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    """
    <div style="font-size:18px; line-height:1.6;">
    
    <strong>What this view shows:</strong><br>
    This dashboard highlights the <strong>20 most popular Divvy bike stations</strong>, ranked by total trip volume for the selected seasons.
    
    <br><br>
    
    <strong>Key insight:</strong><br>
    A small group of stations clearly dominates overall usage. In particular, <strong>W 21 St & 6 Ave</strong>, <strong>West St & Chambers St</strong>, <strong>Broadway & W 58 St</strong>, <strong>1 Ave & E 68 St</strong>, and <strong>6 Ave & W 33 St</strong> consistently record the highest number of trips, standing out from the remaining stations.
    
    <br><br>
    
    <strong>Seasonal perspective:</strong><br>
    The season filters on the left allow this ranking to be adjusted dynamically, making it possible to analyse how station popularity changes across <em>spring, summer, fall, and winter</em>, and whether the same locations remain dominant throughout the year.
    
    <br><br>
    
    <strong>Why this matters:</strong><br>
    These high-demand stations should be prioritised for bike availability, rebalancing, and maintenance, while seasonal comparisons support more informed operational and planning decisions.
    
    </div>
    """,
    unsafe_allow_html=True
    )



################################################## 5TH PAGE INTERACTIVE MAP ##################################################

elif page == 'Interactive Map with Bike Trips':

    ### Create the map ###

    st.write("Interactive map showing aggregated bike trips over New York")

    path_to_html = "NY_CitiBike_Trips_Map.html" 

    # Read file and keep in variable
    with open(path_to_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.header("Aggregated Bike Trips in New York")
    st.components.v1.html(html_data, height=425)
    st.markdown("#### This interactive map visualises aggregated bike trips across New York, highlighting the most significant travel routes.")
    st.markdown(
    """
    <div style="font-size:18px; line-height:1.6;">
    
    <strong>Data focus:</strong><br>
    To reduce noise and emphasise meaningful patterns, this map only displays station pairs with <strong>at least 750 total trips</strong> between them. This filtering helps surface the most frequently used routes rather than isolated or infrequent journeys.
    
    <br><br>
    
    <strong>Key insight:</strong><br>
    The densest and most active connections are concentrated in Manhattan, particularly along north south corridors, indicating strong recurring travel patterns in high demand areas. These routes likely represent commuter heavy or consistently popular travel paths.
    
    <br><br>
    
    <strong>Interactivity:</strong><br>
    Additional filters embedded within the map allow this view to be adjusted further, making it possible to explore different thresholds, areas, or patterns of interest and uncover alternative insights beyond the default configuration.
    
    <br><br>
    
    <strong>Why this matters:</strong><br>
    Identifying high volume routes supports more efficient operational decisions, such as bike redistribution, infrastructure planning, and prioritisation of maintenance along the most heavily used corridors.
    
    </div>
    """,
    unsafe_allow_html=True
    )


################################################## 6TH PAGE RECCOMENDATIONS ##################################################

else:
    
    st.header("Conclusions and recommendations")
    bikes = Image.open("recs_page.png")
    st.image(bikes)
    st.markdown("---")
        
    st.markdown(
    """
    <div style="font-size:18px; line-height:1.7;">
    
    <strong>Key insight:</strong> This analysis examined Citi Bikes usage patterns across time, location, and seasonality to identify practical actions that can help reduce bike shortages and support future expansion decisions.<br><br>
    <strong>Seasonal scaling of bike availability (November–April)</strong><br>
    Citi Bikes should scale bike availability down by approximately 30–40% between November and April.<br>
    The analysis shows a strong seasonal relationship between temperature and bike usage. Trip volumes peak during warmer months (June–August) and decline steadily through autumn, reaching their lowest levels in winter. During colder months, demand is consistently lower across most stations and time periods.<br><br>

    <strong>Determining how many new stations to add along waterfront areas</strong><br>
    Future station expansion along the water should be guided by high volume route analysis, rather than evenly spaced station placement.<br>
    The interactive map highlights dense, recurring bike trip corridors concentrated along Manhattan’s waterfront and north south travel routes. These corridors indicate sustained demand rather than isolated trips.<br><br>

    <strong>Ensuring bikes are available at the most popular stations</strong><br>
    Citi Bikes should prioritise dynamic rebalancing and staffing during peak demand hours, particularly morning (06:00–09:00) and late afternoon to early evening (16:00–18:00).<br>
    Bike usage follows a clear daily rhythm, with the highest demand occurring during commuter hours. A small number of stations consistently dominate total trip volume across all seasons, making them especially vulnerable to shortages.<br><br>
    
    </div>
    """,
    unsafe_allow_html=True
    )