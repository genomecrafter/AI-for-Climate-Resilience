import numpy as np
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly, plot_cross_validation_metric
import streamlit as st

@st.cache()
def load_ogdata():
    og = pd.read_csv('weather.csv')
    return og

@st.cache_data
def load_data():
    df = pd.read_csv('weather.csv')
    threshold = len(df) * 0.9
    df.dropna(thresh=len(df) - threshold, axis=1, inplace=True)
    df.dropna()#changes
    return df

@st.cache_resource()
def train_model(df):
    # Train Prophet models for PRCP, TMAX, and TMIN
    
    # Prepare data for Prophet: for example, let's do it for 'TMAX'
    def prepare_prophet_data(df, target_col):
        return df[['DATE', target_col]].rename(columns={'DATE': 'ds', target_col: 'y'})
    
    # Prophet models for each feature
    models = {}
    
    # # Train for 'PRCP' (Precipitation)
    # prcp_df = prepare_prophet_data(df, 'PRCP')
    # prcp_model = Prophet()
    # prcp_model.fit(prcp_df)
    # models['PRCP'] = prcp_model
    
    # # Train for 'TMAX' (Maximum temperature)
    # tmax_df = prepare_prophet_data(df, 'TMAX')
    # tmax_model = Prophet()
    # tmax_model.fit(tmax_df)
    # models['TMAX'] = tmax_model
    
    # # Train for 'TMIN' (Minimum temperature)
    # tmin_df = prepare_prophet_data(df, 'TMIN')
    # tmin_model = Prophet()
    # tmin_model.fit(tmin_df)
    # models['TMIN'] = tmin_model
    for feature in ['PRCP', 'TMAX', 'TMIN']:
        # Prepare the data for Prophet
        df_prophet = df[['DATE', feature]].rename(columns={'DATE': 'ds', feature: 'y'})
        
        # Initialize and fit the model with seasonality adjustments
        model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
        model.fit(df_prophet)

        models[feature] = model
    
    return models

def predict(models, input_date):
    # Make future dataframe for the input date
    future = pd.DataFrame({'ds': [input_date]})
    
    # Get predictions for each feature
    prcp_forecast = models['PRCP'].predict(future)
    tmax_forecast = models['TMAX'].predict(future)
    tmin_forecast = models['TMIN'].predict(future)
    
    # Collect predictions into a result dictionary
    results = {
        'Predicted_Precipitation': prcp_forecast['yhat'].values[0],
        'Predicted_Tmax': tmax_forecast['yhat'].values[0],
        'Predicted_Tmin': tmin_forecast['yhat'].values[0]
    }
    
    return results