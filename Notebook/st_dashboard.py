import streamlit as st
import pandas as pd 
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static 
from keplergl import KeplerGl
from datetime import datetime as dt 

st.set_page_config(page_title = 'NY Citi Bikes (Jersey City) Strategy Dashboard', layout='wide')

st.title("NY Citi Bikes (Jersey City) Strategy Dashboard")

st.markdown("The dashboard will help with the expansion problems in Jersey City")

top20 = pd.read_csv('top_20.csv', index_col = 0)
df_group = pd.read_csv('daily_rides_and_temperature.csv', index_col = 0)

# ########################### DEFINE THE CHARTS ############################


## Bar chart

fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker={'color': top20['value'],'colorscale': 'PuRd'}))

# Update layout to provide more space for the station names

# Update layout to provide more space for the station names
fig.update_layout(
    title='Top 20 most popular bike stations in Jersey City',
    xaxis_title='Start stations',
    yaxis_title='Sum of trips',
    width=900,  # Adjust the width of the plot
    height=600,  # Adjust the height of the plot
    margin=dict(b=200),  # Increase bottom margin to provide more space for x-axis labels
    xaxis=dict(
        tickangle=-45,  # Rotate x-axis labels for better readability
        automargin=True,  # Automatically adjust margins to fit labels
        tickfont=dict(size=10)  # Adjust font size for x-axis labels
    )
)
st.plotly_chart(fig, use_container_width = True)


## line chart

# Create subplots with a secondary y-axis
fig_2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add the first trace for daily bike rides
fig_2.add_trace(
        go.Scatter(
            x=df_group['date'],
            y=df_group['ride_id'],
            name='Daily Bike Rides',
            marker=dict(color='#e51872'), 
            text=df_group['ride_id'],  # Add tooltips for ride count
            hoverinfo='text+x+y'  # Show text on hover
        ), 
        secondary_y=False
    )

# Add the second trace for daily temperature
fig_2.add_trace(
        go.Scatter(
            x=df_group['date'],
            y=df_group['avgTemp'],
            name='Daily Temperature',
            marker=dict(color='Green'),
            text=df_group['avgTemp'],  # Add tooltips for temperature
            hoverinfo='text+x+y'  # Show text on hover
        ), 
        secondary_y=True
    )

# Update layout with titles and dimensions
# Update layout to provide gridlines and minor ticks

fig_2.update_layout(
        title='Daily Bike Rides and Temperature in Jersey City', 
        xaxis_title='Date',
        yaxis_title='Daily Bike Rides',
        height=500,
        xaxis=dict(
            showgrid=True,  # Show major gridlines
            gridcolor='LightGrey',  # Set gridline color
            gridwidth=0.5,  # Set gridline width
            tickangle=-45,  # Angle the ticks for better readability
            showticklabels=True,  # Ensure tick labels are shown
            tickmode='auto',  # Allow automatic tick placement
            dtick='M1',  # Set the tick frequency (e.g., monthly ticks)
            minor=dict(
                ticklen=5,  # Minor tick length
                showgrid=True,  # Show minor gridlines
                gridcolor='LightGrey',  # Minor gridline color
                gridwidth=0.2  # Minor gridline width
            )
        ),
        yaxis=dict(
            showgrid=True,  # Show major gridlines on the y-axis
            gridcolor='LightGrey',  # Gridline color
            gridwidth=0.5  # Gridline width
        )
    )

# Update secondary y-axis title
fig_2.update_yaxes(title_text='Temperature (°C)', secondary_y=True)

# Calculate min and max for ride counts and temperature
min_ride = df_group['ride_id'].min()
max_ride = df_group['ride_id'].max()
min_temp = df_group['avgTemp'].min()
max_temp = df_group['avgTemp'].max()

# Find the corresponding dates for the min and max values
min_ride_date = df_group.loc[df_group['ride_id'] == min_ride, 'date'].values[0]
max_ride_date = df_group.loc[df_group['ride_id'] == max_ride, 'date'].values[0]
min_temp_date = df_group.loc[df_group['avgTemp'] == min_temp, 'date'].values[0]
max_temp_date = df_group.loc[df_group['avgTemp'] == max_temp, 'date'].values[0]

#Add horizontal lines for min and max bike rides
fig_2.add_trace(
        go.Scatter(
            x=[df_group['date'].min(), df_group['date'].max()],
            y=[min_ride, min_ride],
            mode="lines",
            name=f"Min Daily Bike Rides ({min_ride_date})",
            line=dict(dash="dash", color="red")
        ),
        secondary_y=False
    )
fig_2.add_trace(
        go.Scatter(
            x=[df_group['date'].min(), df_group['date'].max()],
            y=[max_ride, max_ride],
            mode="lines",
            name=f"Max Daily Bike Rides ({max_ride_date})",
            line=dict(dash="dash", color="blue")
        ),
        secondary_y=False
    )

# Add horizontal lines for min and max temperature
fig_2.add_trace(
        go.Scatter(
            x=[df_group['date'].min(), df_group['date'].max()],
            y=[min_temp, min_temp],
            mode="lines",
            name=f"Min Daily Temperature ({min_temp_date})",
            line=dict(dash="dash", color="blue")
        ),
        secondary_y=True
    )
fig_2.add_trace(
        go.Scatter(
            x=[df_group['date'].min(), df_group['date'].max()],
            y=[max_temp, max_temp],
            mode="lines",
            name=f"Max Daily Temperature ({max_temp_date})",
            line=dict(dash="dash", color="red")
        ),
        secondary_y=True
    )

#Example: Add marker annotations for specific key dates
key_dates = ['2022-01-01', '2022-12-01']  # Add dates where bike rides or temperature variations are significant

for date in key_dates:
    fig_2.add_annotation(
            x=date,
            y=df_group.loc[df_group['date'] == date, 'ride_id'].values[0],  # Use the correct y value for the annotation
            text=f"Peak: {date}",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowcolor='red',
            bgcolor='yellow',
            font=dict(size=12, color='black'),
            align='center'
        )

st.plotly_chart(fig_2, use_container_width=True)


### Add the map  ###

# Assign the HTML file name to a variable
file_name = "NYC_Citi_Bikes_Map.html"

# Read file and keep in variable 
with open(file_name, 'r') as f:
    html_data = f.read()

## Show in web page 
st.header("Aggregated Bike Trips in Jersey City")
st.components.v1.html(html_data,height = 1000)

## Kepler map context description
### Kepler Map: Visualizing Bike Ride Locations in Jersey City
#### Three Main Hubs
#### There are three main hubs for bike usage (which are visible by observing the 'route arcs'). 'Hub 1' around in the area of Hoboken Terminal and Yards/Stevens Institute of Technology (parallel to the Meatpacking District in Manhattan); 'Hub 2' south (slightly west of what is labeled Downtown Jersey City); and smaller 'Hub 3' furhter west (near Indian Square). I will focus my insights mostly on Hub 1 and 2. There is also a much smaller Hub 4 in downtown Jersey City, by the water (parallel to Battery City Park in Manhattan).