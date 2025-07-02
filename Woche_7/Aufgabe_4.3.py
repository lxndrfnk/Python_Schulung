import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
import pytz

# Function to fetch earthquake data
@st.cache_data(ttl=120)
def fetch_earthquake_data(url):
    response = requests.get(url)
    data = response.json()
    
    # Parse the data
    features = data['features']
    earthquakes = []
    for feature in features:
        properties = feature['properties']
        geometry = feature['geometry']
        utc_time = pd.to_datetime(properties['time'], unit='ms')
        local_time = utc_time.tz_localize('UTC').tz_convert(pytz.timezone('America/Los_Angeles'))  # Convert to local timezone
        earthquakes.append({
            "place": properties['place'],
            "magnitude": properties['mag'],
            "time_utc": utc_time,
            "time_local": local_time,
            "latitude": geometry['coordinates'][1],
            "longitude": geometry['coordinates'][0]
        })
    
    return pd.DataFrame(earthquakes)

# Fetch real-time earthquake data
realtime_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
df = fetch_earthquake_data(realtime_url)

st.title("🌍 Erdbeben Visualisierung")

st.write(f"In den letzten 30 Tagen gab es insgesamt {len(df)} Erdbeben.")

# Datumsauswahl
min_date = df['time_utc'].min().date()
max_date = df['time_utc'].max().date()

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Von", min_date, min_value=min_date, max_value=max_date)
with col2:
    end_date = st.date_input("Bis", max_date, min_value=min_date, max_value=max_date)

# Filterung nach Datum
mask = (df['time_utc'].dt.date >= start_date) & (df['time_utc'].dt.date <= end_date)
filtered_df = df.loc[mask]

# Anzeige der Anzahl
st.subheader("Erdbeben im Zeitraum")
st.metric(label="", value=len(filtered_df))

# Gruppierung: Anzahl pro Tag
daily_counts = filtered_df.groupby(filtered_df['time_utc'].dt.date).size().reset_index(name='count')

# Balkendiagramm
fig = px.bar(daily_counts, x='time_utc', y='count',
             labels={'time_utc': 'Datum', 'count': 'Anzahl Erdbeben'},
             title='📊 Einträge pro Tag')

st.plotly_chart(fig, use_container_width=True)