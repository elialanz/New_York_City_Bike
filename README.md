## NYC CityBike Dashboard - Data Analysis (2022)

This project is part of the Data Visualization with Python module, where the goal is to build a strategic, data driven dashboard to help a bike sharing company understand rider behavior, identify logistical issues, and discover opportunities for system expansion across New York City.

The analysis is based on **Citi Bike’s open source trip data for 2022**, enriched with **weather data from NOAA’s API**. The final dashboard is created in **Python using Streamlit**, and it visualizes key operational patterns such as station demand, popular routes, seasonal trends, bike type usage, and geographic distribution.

### Project Goals

- Diagnose where Citi Bike distribution problems may be occurring.
- Understand usage patterns across stations, routes, time periods, and bike types.
- Enrich the core dataset with external weather data to analyze seasonal effects.
- Communicate insights through a clean, interactive Python dashboard.
- Support the business strategy team with actionable, data-driven recommendations.

These goals reflect the project requirements outlined in the Project brief.

### Data Sources

**Citi Bike Trip Data (2022)**

Publicly available at → https://citibikenyc.com/system-data

Used for:
- Trip counts
- Station popularity
- Route patterns
- Bike type usage
- Hourly/seasonal trends
- Geographic distribution

**NOAA Weather Data (2022)**

API endpoint → https://www.ncdc.noaa.gov/cdo-web/api/v2/data

Collected using:
- Dataset: GHCND
- Datatype: TAVG (Average Temperature)
- Station: LaGuardia Airport (USW00014732)
- Year: 2022

Used to examine the relationship between weather and bike usage.

### Python Libraries Used

**Data Handling & Cleaning**

- pandas
- numpy
- os
- json
- requests

**Visualization**

- matplotlib
- seaborn
- plotly

**Geospatial Mapping**

kepler.gl

**Dashboard Development**

streamlit

### Summary of Analysis

The descriptive analysis focuses on identifying the factors that affect demand and operational strain across New York City’s bike sharing system.

**Key elements explored include:**
- Most popular stations
- Most frequent routes
- Seasonal patterns and weather impact
- Bike type preferences (classic vs electric)
- Peak operational hours
- Station distribution across the city

These insights directly support strategic decisions around station placement, fleet balancing, and resource allocation.

### Final Dashboard

The dashboard is built with Streamlit, integrating multiple plots and maps to present insights clearly and interactively.

Dashboard Link → I will insert the dashboard link here once deployed



