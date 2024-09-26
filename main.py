import streamlit as st

#from web_functions import load_data

from Tabs import home,data,predict,visualize,about

st.set_page_config(
    page_title = 'AI for Climate Resilience',
    layout='wide',
    initial_sidebar_state='auto'
)

Tabs = {
    "Home": home,
    "About":about,
    "Data Info": data,
    "Prediction": predict,
    "Visualize" : visualize
}

st.sidebar.title("Navigate")

page = st.sidebar.radio("Pages", list(Tabs.keys()))

if page in ["Home","About"]:
    Tabs[page].app()