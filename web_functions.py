import numpy as np
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly, plot_cross_validation_metric
import streamlit as st


<<<<<<< HEAD


     
=======
df = pd.read_csv('weather.csv')

threshold = len(df) * 0.9

df.dropna(thresh=len(df) - threshold, axis=1, inplace=True)

>>>>>>> 18e6b1fbee05048a5955ba27431ead3a3160ca9e
