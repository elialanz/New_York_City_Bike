# NYC Citi Bike Dashboard - Data Analysis (2022)

View the deployed [NYC Citi Bike data analysis dashboard](https://citibike.elialanz.com/) built with Python and Streamlit.

Read the full [Citi Bike data analysis case study](https://www.elialanz.com/case-study-citibike/) on my portfolio website.

Explore more projects on my [data analyst portfolio](https://www.elialanz.com/) or learn more about my [business dashboard services](https://www.elialanz.com/dashboard-service/).

---

## NYC CityBike Dashboard - Data Analysis (2022)

This project is part of the Data Visualization with Python module, where the goal is to build a strategic, data-driven dashboard to help a bike-sharing company understand rider behavior, identify logistical issues, and discover opportunities for system expansion across New York City.

The analysis is based on **Citi Bike’s open-source trip data for 2022**, enriched with **weather data from NOAA’s API**. The final dashboard is created in **Python using Streamlit**, and it visualizes key operational patterns such as station demand, popular routes, seasonal trends, bike type usage, and geographic distribution.

The project was developed as a practical urban mobility analytics case study, showing how raw transport data can be cleaned, analyzed, visualized, and turned into useful insights for operational decision-making.

---

### Project Goals

- Diagnose where Citi Bike distribution problems may be occurring.
- Understand usage patterns across stations, routes, time periods, and bike types.
- Enrich the core dataset with external weather data to analyze seasonal effects.
- Communicate insights through a clean, interactive Python dashboard.
- Support the business strategy team with actionable, data-driven recommendations.

These goals reflect the project requirements outlined in the project brief.

---

### Business Questions

This Citi Bike analysis focuses on practical business questions such as:

- Which Citi Bike stations generate the highest trip activity?
- Which routes show the strongest demand across New York City?
- How does bike usage change by hour, season, and temperature?
- Are there station-level patterns that suggest bike availability or redistribution issues?
- How can geographic trip data support better station planning and service optimization?

---

### Data Sources

**Citi Bike Trip Data (2022)**

Publicly available at → https://citibikenyc.com/system-data

Used for:

- Trip counts
- Station popularity
- Route patterns
- Bike type usage
- Hourly and seasonal trends
- Geographic distribution

**NOAA Weather Data (2022)**

API endpoint → https://www.ncdc.noaa.gov/cdo-web/api/v2/data

Collected using:

- Dataset: GHCND
- Datatype: TAVG (Average Temperature)
- Station: LaGuardia Airport (USW00014732)
- Year: 2022

Used to examine the relationship between weather and bike usage.

---

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

- kepler.gl

**Dashboard Development**

- streamlit

---

### Summary of Analysis

The descriptive analysis focuses on identifying the factors that affect demand and operational strain across New York City’s bike-sharing system.

**Key elements explored include:**

- Most popular Citi Bike stations
- Most frequent bike routes
- Seasonal patterns and weather impact
- Bike type preferences
- Peak operational hours
- Station distribution across New York City
- Geographic trip movement between start and end stations

These insights directly support strategic decisions around station placement, fleet balancing, bike redistribution, and resource allocation.

---

### Key Findings

The analysis identified several important usage patterns:

- High trip density was observed in central Manhattan and commuter-heavy zones.
- Peak usage occurs during morning and evening commute hours.
- Popular routes connect business districts, transport hubs, and high-traffic urban areas.
- Weekday usage exceeds weekend usage, suggesting strong commuter-driven demand.
- Certain stations show signs of imbalance between departures and arrivals.
- Weather conditions appear to influence trip frequency and duration.
- Geographic filtering helps highlight critical high-demand routes that may need operational optimization.

---

### Final Dashboard

The final [NYC Citi Bike data analysis dashboard](https://citibike.elialanz.com/) is built with Streamlit and integrates multiple plots and geospatial visualizations to present insights clearly and interactively.

The dashboard includes:

- A bar chart showing the top 20 most popular Citi Bike stations in New York.
- A line chart comparing daily bike trips with average daily temperature.
- A geospatial trip map showing aggregated bike movements across New York City.
- Route-level visualization using start and end station coordinates.

---

### Full Case Study

A complete project breakdown is available in the [Citi Bike data analysis case study](https://www.elialanz.com/case-study-citibike/), where I explain the project background, data preparation process, dashboard design, key insights, and business value.

---

### Business Value

This project demonstrates how urban mobility data can be transformed into operational insight.

A bike-sharing company could use this type of analysis to:

- Monitor high-demand stations.
- Identify peak usage periods.
- Improve bike redistribution planning.
- Understand how weather affects demand.
- Detect popular commuter routes.
- Support station expansion decisions.
- Communicate system performance through a clear dashboard.

This type of Python dashboard helps move from raw trip records to practical business insight, making it easier for decision-makers to understand where service improvements may be needed.

---

### Project Files

This repository includes project files related to:

- Citi Bike data cleaning
- Weather data integration
- Exploratory data analysis
- Station and route aggregation
- Geospatial visualization
- Streamlit dashboard development
- Final dashboard deployment

---

### About Me

I'm Elia Lanzuise, a Melbourne-based data analyst focused on transforming raw data into clear, actionable insights using Python, SQL, Tableau, Power BI, Excel, and dashboard development.

My work focuses on business performance analysis, data visualization, customer behavior, operational insights, and turning complex datasets into practical decisions.

I'm specialised in [data analytics for transport and logistics](https://www.elialanz.com/dashboard-service/), retail, transport, booking based services, and e-commerce.

[See how I work with clients →](https://www.elialanz.com/dashboard-service/) · [Other data services I offer →](https://www.elialanz.com/hire-me/) · [elialanz.com](https://www.elialanz.com)

