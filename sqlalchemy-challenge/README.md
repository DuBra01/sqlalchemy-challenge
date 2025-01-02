# sqlalchemy-challenge
# Hawaii Climate Analysis and Flask API

## Project Overview
This project involves analyzing climate data for Hawaii and creating a Flask API to make the analysis results accessible. The project uses:
- **Jupyter Notebook** for initial exploratory data analysis.
- **Visual Studio Code** for designing and deploying the Flask API.

---

## Table of Contents
1. [Data Overview](#data-overview)
2. [Tools and Libraries](#tools-and-libraries)
3. [Jupyter Notebook Analysis](#jupyter-notebook-analysis)
4. [Flask API](#flask-api)
5. [Setup and Execution](#setup-and-execution)
6. [API Endpoints](#api-endpoints)

---

## Data Overview
The dataset includes:
1. `hawaii_measurements.csv`: Contains precipitation and temperature observations.
2. `hawaii_stations.csv`: Lists weather stations.
3. `hawaii.sqlite`: A SQLite database consolidating the data from the CSV files.

---

## Tools and Libraries
### Python Libraries
- **SQLAlchemy**: For interacting with the SQLite database.
- **Flask**: To create the API.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For visualizations.
- **datetime**: For working with date objects.

### Tools
- **Jupyter Notebook**: For exploratory data analysis.
- **Visual Studio Code**: For API development.

---

## Jupyter Notebook Analysis
The exploratory analysis in Jupyter Notebook includes:
1. **Precipitation Analysis**:
   - Queried and plotted the last 12 months of precipitation data.
   - Calculated summary statistics for the precipitation dataset.

2. **Station Analysis**:
   - Identified the most active weather station.
   - Queried the lowest, highest, and average temperatures recorded at the most active station.
   - Queried and plotted the last 12 months of temperature observations for the most active station.

---

## Flask API
The Flask API makes the analysis results accessible via HTTP endpoints.

### Features
- **Homepage**: Lists all available routes.
- **Precipitation Data**: Returns the last 12 months of precipitation data as JSON.
- **Station Data**: Returns a list of all weather stations as JSON.
- **Temperature Observations**: Returns the last 12 months of temperature data for the most active station.
- **Temperature Statistics**: Calculates and returns min, avg, and max temperatures for specified date ranges.

---
