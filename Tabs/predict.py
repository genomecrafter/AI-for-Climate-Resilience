import streamlit as st
from datetime import datetime
import pandas as pd
from sklearn.metrics import mean_absolute_error
from web_functions import load_data, train_model, predict
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error

def app():
    st.title("Weather Prediction")

    # Let the user select a single date or multiple dates
    date_selection = st.radio("Select date type", ["Single Date", "Date Range"])

    if date_selection == "Single Date":
        single_date = st.date_input("Select a date", value=datetime.today())
        dates = [single_date]

    elif date_selection == "Date Range":
        date_range = st.date_input("Select a date range", [])
        if len(date_range) == 2:
            start_date, end_date = date_range
            dates = pd.date_range(start=start_date, end=end_date).to_list()
        else:
            st.warning("Please select a valid date range.")
            return

    # Button to trigger predictions
    if st.button("Predict Weather"):
        try:
            # Load preprocessed data
            df = load_data()

            # Train Prophet models for PRCP, TMAX, TMIN
            models = train_model(df)

            # Collect predictions for each selected date
            predictions = []
            actuals = []  # To store actual values for accuracy comparison
            for idx, input_date in enumerate(dates):
                # Predicted values
                results = predict(models, input_date)
                results['Sl.No'] = idx + 1
                results['Date'] = input_date.strftime("%Y-%m-%d")
                predictions.append(results)

                # Actual values from the dataset (assuming historical data exists for comparison)
                # Assuming your dataset has 'DATE' as the date column
                actual_row = df[df['DATE'] == input_date.strftime('%Y-%m-%d')]
                if not actual_row.empty:
                    actuals.append({
                        'Date': input_date.strftime("%Y-%m-%d"),
                        'Actual_Precipitation': actual_row['PRCP'].values[0],
                        'Actual_Tmax': actual_row['TMAX'].values[0],
                        'Actual_Tmin': actual_row['TMIN'].values[0]
                    })

            # Convert predictions and actuals into DataFrames for display and calculation
            pred_df = pd.DataFrame(predictions)
            actual_df = pd.DataFrame(actuals)

            # Calculate MAE for each feature
            if not actual_df.empty:
                mae_prcp = mean_absolute_error(actual_df['Actual_Precipitation'], pred_df['Predicted_Precipitation'])
                mae_tmax = mean_absolute_error(actual_df['Actual_Tmax'], pred_df['Predicted_Tmax'])
                mae_tmin = mean_absolute_error(actual_df['Actual_Tmin'], pred_df['Predicted_Tmin'])

                # Display MAE as the accuracy metric
                st.write(f"Prediction Accuracy (Mean Absolute Error):")
                st.write(f"Precipitation MAE: {mae_prcp:.2f} mm")
                st.write(f"Tmax MAE: {mae_tmax:.2f} °C")
                st.write(f"Tmin MAE: {mae_tmin:.2f} °C")

            else:
                st.write("No actual data available for comparison to calculate accuracy.")

            # Display predictions in a table
            st.write("Weather Predictions:")
            st.table(pred_df[['Sl.No', 'Date', 'Predicted_Precipitation', 'Predicted_Tmax', 'Predicted_Tmin']].style.format({
                "Predicted_Precipitation": "{:.2f} mm",
                "Predicted_Tmax": "{:.2f} °C",
                "Predicted_Tmin": "{:.2f} °C"
            }))

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
