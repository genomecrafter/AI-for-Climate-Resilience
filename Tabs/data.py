import streamlit as st

def app(df,og):
    st.title("Dataset Info")

    st.markdown('<p style="font-size:20px;">Go to <a href="https://www.ncdc.noaa.gov/cdo-web/search" target="_blank">NOAA</a></p>', unsafe_allow_html=True)
    
    st.subheader("View Data")
    
    with st.expander("View Original Data"):
        st.dataframe(og)

    with st.expander("View Preprocessed Data"):
        st.dataframe(df)

    st.subheader("Columns Description:")

    column_descriptions = {
        'STATION': 'Unique identifier for the weather station.',
        'NAME': 'Name or location of the nearest airport',
        'ACMH': 'Average cloudiness midnight to midnight from manual observations (percent)',
        'ACSH': 'Average cloudiness sunrise to sunset from manual observations (percent).',
        'AWND': 'Average daily wind speed ',
        'FMTM': 'Time of fastest mile wind .',
        'PGTM': 'Peak gust time (hours and minutes, i.e., HHMM).',
        'PRCP': 'Precipitation amount recorded during a specified period.',
        'SNOW': 'Total snow accumulation recorded during a specified period.',
        'SNWD': 'Snow depth on the ground at the time of observation.',
        'TAVG': 'Average temperature recorded over a specific period.',
        'TMAX': 'Maximum temperature recorded during a specified period.',
        'TMIN': 'Minimum temperature recorded during a specified period.',
        'TSUN': 'Total sunshine duration recorded during a specified period.',
        'WDF1': 'Direction of fastest 1-minute wind (degrees).',
        'WDF2': 'Direction of fastest 2-minute wind (degrees).',
        'WDF5': 'Direction of fastest 5-second wind (degrees).',
        'WDFG': 'Direction of peak wind gust (degrees).',
        'WDFM': 'Fastest mile wind direction (degrees).',
        'WESD': 'Water equivalent of snow on the ground.',
        'WSF1': 'Fastest 1-minute wind speed.',
        'WSF2': 'Fastest 2-minute wind speed.',
        'WSF5': 'Fastest 5-second wind speed.',
        'WSFG': 'Peak guest wind speed.',
        'WSFM': 'Fastest mile wind speed.',
        'WT01': 'Fog, ice fog, or freezing fog (may include heavy fog)',
        'WT02': 'Heavy fog or heaving freezing fog (not always distinguished from fog)',
        'WV01': 'Weather in the Vicinity whereFog, ice fog, or freezing fog (may include heavy fog).',
        'WV20': 'Weather in the Vicinity where Rain or snow shower.'
    }

    if st.checkbox("Column Names"):
            st.dataframe(df.columns)
    for col, desc in column_descriptions.items():
        st.write(f"**{col}:** {desc}")