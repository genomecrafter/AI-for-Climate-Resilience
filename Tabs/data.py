import streamlit as st

def app(df):
    st.title("Dataset Info")

    st.mardown("""<p style="font-size:20px;">
                   Go to [NOAA](https://www.ncdc.noaa.gov/cdo-web/search) 
                </p>""", unsafe_allow_html=True)
    
    st.subheader("View Data")

    with st.expander("View Data"):
        st.dataframe(df)

    st.subheader("Columns Description:")

    column_descriptions = {
        'STATION': 'Unique identifier for the weather station.',
        'NAME': 'Name or location of the nearest airport',
        'ACMH': 'Average cloudiness midnight to midnight from manual observations (percent)',
        'ACSH': 'Average daily minimum humidity.',
        'AWND': 'Average wind speed over a specified period.',
        'FMTM': 'Formatted time of the observation.',
        'PGTM': 'Peak gust time (maximum wind speed recorded).',
        'PRCP': 'Precipitation amount recorded during a specified period.',
        'SNOW': 'Total snow accumulation recorded during a specified period.',
        'SNWD': 'Snow depth on the ground at the time of observation.',
        'TAVG': 'Average temperature recorded over a specific period.',
        'TMAX': 'Maximum temperature recorded during a specified period.',
        'TMIN': 'Minimum temperature recorded during a specified period.',
        'TSUN': 'Total sunshine duration recorded during a specified period.',
        'WDF1': 'Wind direction for the first observation.',
        'WDF2': 'Wind direction for the second observation.',
        'WDF5': 'Wind direction for the fifth observation.',
        'WDFG': 'Average wind direction over a specified time.',
        'WDFM': 'Maximum wind direction over a specified time.',
        'WESD': 'Water equivalent of snow on the ground.',
        'WSF1': 'Wind speed for the first observation.',
        'WSF2': 'Wind speed for the second observation.',
        'WSF5': 'Wind speed for the fifth observation.',
        'WSFG': 'Average wind speed over a specified time.',
        'WSFM': 'Maximum wind speed over a specified time.',
        'WT01': 'Weather type code for specific weather conditions.',
        'WT02': 'Weather type code for specific weather conditions.',
        # Add descriptions for all WT and WV codes similarly
        'WV01': 'Wind variable code providing additional wind details.',
        'WV20': 'Wind variable code providing additional wind details.',
        # Continue adding for WT03, WT04, ..., WT22
    }

    if st.checkbox("Column Names"):
            st.dataframe(df.columns)
    for col, desc in column_descriptions.items():
        st.write(f"**{col}:** {desc}")