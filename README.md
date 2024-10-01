# Weather Prediction Using Prophet

This project uses historical weather data from NOAA and Facebook Prophet to predict weather components such as **Precipitation**, **Maximum Temperature (Tmax)**, and **Minimum Temperature (Tmin)**. The application allows users to predict these weather components over a date range and visualize the trends, seasonality, and yearly patterns of the predictions.

## Features
- Select a single date or a date range to predict weather data.
- Predict key weather parameters: 
  - **Precipitation**
  - **Tmax** (Maximum Temperature)
  - **Tmin** (Minimum Temperature)
- Display prediction accuracy using Mean Absolute Error (MAE).
- Visualize seasonal, trend, and weekly components of the predicted data.
- Data and results displayed in a user-friendly dashboard built using **Streamlit**.

## Screenshots

## Prediction Page
![Prediction Page](images/Screenshot%202024-09-30%20182651.png)

## Visualization of Trends
![Trends Visualization](images/Screenshot%202024-09-30%20183001.png)


## Dataset

The dataset used for this project was downloaded from the [National Oceanic and Atmospheric Administration (NOAA)](https://www.noaa.gov/). This dataset contains various weather features such as precipitation, temperature, wind, and snow details.
The data is pre-processed and formatted as required by the Prophet model, using the column `ds` for the date and `y` for the value to be predicted.

## Application Components

1. **Main Application:**
   The application is built with **Streamlit**. The user selects either a single date or a range of dates, and the model predicts and displays weather components. The predictions are displayed in tabular format, and the average predicted values are also calculated over the selected range.

2. **Visualization Tab:**
   The visualization tab allows users to explore the seasonal, trend, and weekly components of Tmax and Tmin, generated using Prophet.


