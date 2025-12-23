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
  ["Introduction","Weather and Bike Trips",
   "Most Popular Stations",
    "Interactive Map with Bike Trips", "Recommendations"])

########################### CREATING A DROPDOWN MENU ############################################################################

df = pd.read_csv('reduced_data_to_plot_small.csv')
df['date'] = pd.to_datetime(df['date'])
top20_csv = pd.read_csv('top20.csv')
temp_trips = pd.read_csv('temp_trips.csv')
temp_trips['trip_date'] = pd.to_datetime(temp_trips['trip_date'])

######################################### DEFINE THE PAGES #####################################################################


################################################## INTRO PAGE ##################################################

if page == "Introduction":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Divvy Bikes currently faces.")
    st.markdown("This chart shows the relationship between daily Divvy bike rides and average daily temperature throughout 2022. A clear seasonal pattern is visible across the year.Bike usage increases steadily from winter into spring, reaching its highest levels during the summer months (June–August), when temperatures are consistently warmer. This suggests a strong positive relationship between temperature and bike ridership, with favorable weather encouraging more cycling activity. From September onwards, both temperature and bike trips begin to decline, with the sharpest drops occurring during late autumn and winter. Occasional dips in ridership during warmer months may be explained by short-term factors such as heavy rain, extreme heat, or operational disruptions. Overall, the chart highlights temperature as a key driver of bike demand, reinforcing the importance of seasonal planning for bike availability, maintenance, and staffing. The dashboard is separated into 4 sections:")
    st.markdown("- Most Popular Stations")
    st.markdown("- Weather and Bike Trips")
    st.markdown("- Interactive Map with Bike Trips")
    st.markdown("- Recommendations")
    st.markdown("The dropdown menu on the left 'Aspect Selector' will take you to the different aspects of the analysis our team looked at.")

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
    st.markdown("There is an obvious correlation between the rise and drop of temperatures and their relationship with the frequency of bike trips taken daily. As temperatures plunge, so does bike usage. This insight indicates that the shortage problem may be prevalent merely in the warmer months, approximately from May to October.")

################################################## THIRD PAGE POPULAR STATIONS ##################################################

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
    st.markdown("From the bar chart it is clear that there are some start stations that are more popular than others - in the top 3 we can see Streeter Drive/Grand Avenue, Canal Street/Adams Streat as well as Clinton Street/Madison Street. There is a big jump between the highest and lowest bars of the plot, indicating some clear preferences for the leading stations. This is a finding that we could cross reference with the interactive map that you can access through the side bar select box.")

################################################## FOURTH PAGE INTERACTIVE MAP ##################################################

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
    st.markdown("#### Using the filter on the left hand side of the map we can check whether the most popular start stations also appear in the most popular trips.")
    st.markdown("The most popular start stations are:")
    st.markdown("Streeter Drive/Grand Avenue, Canal Street/Adams Street as well as Clinton Street/Madison Street. While having the aggregated bike trips filter enabled, we can see that even though Clinton Street/Madison Street is a popular start stations, it doesn't account for the most commonly taken trips.")
    st.markdown("The most common routes (>2,000) are between Theater on the Lake, Streeter Dr/Grand Avenue, Millenium Park, Columbus Dr/Randolph Street, Shedd Aquarium, Michigan Avenue/Oak Street, Canal Street/Adams Street, which are predominantly located along the water.")

################################################## FIFTH PAGE RECCOMENDATIONS ##################################################

else:
    
    st.header("Conclusions and recommendations")
    bikes = Image.open("recs_page.png")
    st.image(bikes)
    st.markdown("### Our analysis has shown that Divvy Bikes should focus on the following objectives moving forward:")
    st.markdown("- Add more stations to the locations around the water line, such as heater on the Lake, Streeter Dr/Grand Avenue, Millenium Park, Columbus Dr/Randolph Street, Shedd Aquarium, Michigan Avenue/Oak Street, Canal Street/Adams Street")
    st.markdown("- Ensure that bikes are fully stocked in all these stations during the warmer months in order to meet the higher demand, but provide a lower supply in winter and late autumn to reduce logistics costs")