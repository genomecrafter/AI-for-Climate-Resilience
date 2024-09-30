import streamlit as st
import pandas as pd
from prophet import plot
from prophet.plot import plot_plotly, plot_components_plotly

def app():
    st.title("Weather Prediction Visualization")

    # Ensure predictions and models are available
    if 'models' not in st.session_state:
        st.warning("No models available. Please run the prediction first.")
        return

    # Retrieve models from session state
    models = st.session_state['models']

    # Plot each model's predictions and components
    for feature in ['PRCP', 'TMAX', 'TMIN']:
        model = models.get(feature)

        if model is None:
            st.error(f"No model found for {feature}. Cannot generate plot.")
            continue

        # Create a DataFrame for future dates for plotting
        future_dates = model.make_future_dataframe(periods=30)  # Adjust the number of periods as needed

        # Get predictions for future dates
        forecast = model.predict(future_dates)

        # Plot the predictions using Plotly
        # st.write(f"### {feature} Predictions")
        # fig = plot_plotly(model, forecast)
        # st.plotly_chart(fig)

        # Plot the forecast components
        st.write(f"### {feature} Forecast Components")
        #fig = model.plot(forecast)
        
        fig_components = plot_components_plotly(model, forecast)
        #st.plotly_chart(fig)
        st.plotly_chart(fig_components)

