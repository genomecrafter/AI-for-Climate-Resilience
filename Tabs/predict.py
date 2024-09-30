import streamlit as st
from datetime import datetime
import pandas as pd
from sklearn.metrics import mean_absolute_error
from web_functions import load_data, train_model, predict

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

            for input_date in dates:
                # Predicted values
                results = predict(models, input_date)
                results['Date'] = input_date.strftime("%Y-%m-%d")
                predictions.append(results)

                # Actual values from the dataset
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

            # Store both predictions and actuals in session state
            st.session_state['pred_df'] = pred_df
            st.session_state['actual_df'] = actual_df  # Store actual values for visualization
            st.session_state['models'] = models
            st.session_state['dates'] = dates
            
            # Calculate MAE for each feature
            if not actual_df.empty and not pred_df.empty:
                mae_prcp = mean_absolute_error(actual_df['Actual_Precipitation'], pred_df['Predicted_Precipitation'])
                mae_tmax = mean_absolute_error(actual_df['Actual_Tmax'], pred_df['Predicted_Tmax'])
                mae_tmin = mean_absolute_error(actual_df['Actual_Tmin'], pred_df['Predicted_Tmin'])

                # Display MAE as the accuracy metric
                st.write(f"Prediction Accuracy (Mean Absolute Error):")
                st.write(f"Precipitation MAE: {mae_prcp:.2f} in")
                st.write(f"Tmax MAE: {mae_tmax:.2f} °F")
                st.write(f"Tmin MAE: {mae_tmin:.2f} °F")

                # Calculate average values over the selected date range
                avg_results = {
                    'Average_Predicted_Precipitation': pred_df['Predicted_Precipitation'].mean(),
                    'Average_Predicted_Tmax': pred_df['Predicted_Tmax'].mean(),
                    'Average_Predicted_Tmin': pred_df['Predicted_Tmin'].mean()
                }
                st.write(f"Average Predicted Values Over Date Range:")
                st.write(avg_results)

            else:
                st.write("No actual data available for comparison to calculate accuracy.")

            # Display predictions in a table
            st.write("Weather Predictions:")
            st.table(pred_df[['Date', 'Predicted_Precipitation', 'Predicted_Tmax', 'Predicted_Tmin']].style.format({
                "Predicted_Precipitation": "{:.2f} in",
                "Predicted_Tmax": "{:.2f} °F",
                "Predicted_Tmin": "{:.2f} °F"
            }))

            st.markdown("Go to visualize tab to see the trends")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
