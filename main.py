import streamlit as st

from web_functions import load_data,load_ogdata

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


og = load_ogdata()
df = load_data()

if page in ["Home","About","Prediction"]:
    Tabs[page].app()
elif page in ["Data Info"]:
    Tabs[page].app(df,og)
else:
    Tabs[page].app()