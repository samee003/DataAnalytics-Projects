# COVID-19 Global Trends Dashboard using Tableau and SQL

## Project Overview
This project focuses on the exploration and visualization of global COVID-19 data. By leveraging **SQL** for data extraction and transformation and **Tableau** for interactive storytelling, this project provides insights into infection rates, death percentages, and regional impacts across the globe.

The goal is to provide a clear, data-driven perspective on how the pandemic has evolved and to showcase the power of combining database querying with modern BI tools.

---

## Dataset Description
The data used in this project is sourced from **Our World in Data**. It includes comprehensive metrics on:
* **Total Cases:** Cumulative confirmed cases.
* **Total Deaths:** Cumulative confirmed deaths.
* **Population:** Demographic data per country/region.
* **Vaccination Data:** Tracking the global rollout of vaccines.
* **Date Range:** The analysis covers data from the onset of the pandemic through 2023.

---

## Tech Stack
* **Database:** Microsoft SQL Server (SSMS)
* **Visualization:** Tableau Desktop / Tableau Public
* **Data Formatting:** MS Excel / CSV

---

## Key Analysis & SQL Queries
The data was processed using SQL to create specific views for the Tableau dashboard. Key queries include:
1. **Global Numbers:** Calculating the total cases, total deaths, and global death percentage.
2. **Death Count per Continent:** Breaking down total deaths by geographic region.
3. **Percent Population Infected:** Analyzing which countries had the highest infection rates relative to their population size.
4. **Forecasting Data:** Extracting time-series data to allow Tableau to perform trend-line forecasting.

---

## Dashboard Features
The interactive Tableau dashboard consists of four primary visualizations:
* **Global Statistics Card:** High-level summary of total cases and deaths worldwide.
* **Regional Impact Bar Chart:** Comparison of total death counts across continents.
* **Global Infection Map:** A choropleth map visualizing the percentage of the population infected by country.
* **Infection Trend & Forecast:** A line graph showing the progression of cases over time.

---

## How to Run the Project
1. **SQL Setup:**
   - Import the `CovidDeaths.xlsx` and `CovidVaccinations.xlsx` files into your SQL Server.
   - Run the scripts provided in the `.sql` files to generate the required tables.
2. **Tableau Setup:**
   - Open the `.twb` or `.twbx` file in Tableau.
   - Connect the data source to your SQL Server views or the provided Excel files.
3. **Exploration:**
   - Interact with the map and filters to view data for specific countries or timeframes.

---

## Conclusion
This project demonstrates the full data pipeline—from raw data cleaning and SQL exploration to final visualization. It highlights the critical importance of data accuracy in public health reporting and provides a template for analyzing large-scale global datasets.
