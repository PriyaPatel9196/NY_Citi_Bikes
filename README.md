# Creating a Strategic Dashboard: NY Citi Bikes in Jersey City
#### This project was completed as a requirement for the course, Data Visualizations with Python, by CareerFoundry as part of their Data Analytics Certificate Program.
## Project Objective
#### You are the lead analyst for a bike-sharing service based in New York City, USA, which also provides service in Jersey City. Your team has been tasked with analyzing user behavior to help the business strategy department assess the current logistics model of bike distribution in Jersey City and identify expansion opportunities.
#### The project’s objective is to conduct a descriptive analysis of existing data and discover actionable insights for the business strategy team to help make informed decisions that will circumvent availability issues and ensure the company’s position as a leader in eco-friendly transportation solutions in the city.
## Context
#### For this project, you’ll be using public data from New York bike-sharing facilities operated by Citi Bike. For context, Citi Bike’s popularity has increased since its launch in 2013. The company’s marketing strategy promotes bike sharing as a sustainable and convenient means of transportation, which has been very successful. Since the Covid–19 pandemic, Jersey City residents have found even more merit in bike sharing, creating higher demand. This has led to distribution problems—such as fewer bikes at popular bike stations or stations full of docked bikes, making it difficult to return a hired bike—and customer complaints.
#### The task is to diagnose where distribution issues stem from and advise higher management on a solution based on your diagnosis of the root of the problem—whether it’s sheer numbers, seasonal demand, or something else. Being in a management position also makes you the bridge between divisions, which requires you to ensure the information is tangible for the business development team. To effectively communicate your analysis to non-analysts, you’ll present your insights in an interactive dashboard depicting the metrics you identify as vital for tackling the distribution issues.
## Tools/Skills Used
#### Skills: Sourcing Data with API Key, Data Visualization with Python, Geospatial Plotting, Creating a Dashboard
#### Python: pandas, numpy, os, beautifulsoup, streamlit, pillow, kepler.gl, matplotlib, seaborn, pyplot, numerize
## Data
#### Open Source Data from Citi Bike's Database: https://s3.amazonaws.com/tripdata/index.html
#### Weather data using NOAA's API Service: https://www.noaa.gov/
##### *The data used for this project was from January 1st, 2022 - December 1st, 2022
## Initial Questions and Plan for Dashboard
#### The following are a list of initial questions to guide the analysis. Any unanswered questions are a potential direction for further research.
##### 1. What are the most popular stations in the city?
##### 2. Which are the months with the most trips taken? Is there a weather component at play?
##### 3. What are the most popular trips between stations?
##### 4. Are the existing stations evenly distributed?
##### 5. Are certain stations more or less popular depending on time of day/week/year?
#### Elements to Include in Dashboard (to answer initial questions)
##### 1. Bar Chart: to show most popular stations
##### 2. Line Chart: number of trips throughout the year
##### 3. Map: to show trips being taken and whether stations are evenly distributed
## Analysis Steps
#### Step 1. Source Data and Merge all Datasets (Notebook 2.2)
##### 1a. Import all files for NY Citi Bike trips (Jersey City only - data for NYC is on a separate file that was not used for this project)
##### 1b. Gather weather data from NOAA using API
##### 1c. Inspect and Explore Data
##### 1d. Merge all dataframes
#### Step 2. Create First Visualizations and Observe Insights (Notebooks 2.3 and 2.4)
#### Step 3. Initiate Map (Notebook 2.5)
#### Step 4. Recreate Charts for Dashboard Using Plotly (Notebook 2.6)
#### Step 5. Execute Python Script to Create Dashboard
#### Step 6. Deploy Dashboard and Record Final Presentation (link below)
## Final Presentation and Dashboard
#### Dashboard: http://localhost:8501/
#### Presentation:
## Insights
### Weather
![daily_bike_rides_jersey_city](https://github.com/user-attachments/assets/ef2402d5-9736-493a-88af-00eb3bc8f53b)


## Recommendations for Further Research
