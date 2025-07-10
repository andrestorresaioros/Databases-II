
import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    port="26322",
    database="railway",
    user="postgres",
    password="QTKQKzFpfyrovjAhipitJCATMPXgWpkQ"
)

st.set_page_config(page_title="Weather Predictios", layout="wide")
st.title("🌦️ Dashboard for Weather Predictions and Recommendations")

query = """
SELECT 
    p.prediction_id,
    p.timestamp,
    l.name AS location,
    et.event_name,
    p.probability,
    r.recommen_descrip
FROM Prediction p
JOIN Location l ON p.location_id = l.location_id
JOIN Event_type et ON p.event_type_id = et.event_type_id
LEFT JOIN Recommendation r ON p.prediction_id = r.prediction_id
ORDER BY p.timestamp DESC;
"""

df = pd.read_sql_query(query, conn)

st.dataframe(df, use_container_width=True)

st.sidebar.header("Filters")
location_filter = st.sidebar.multiselect("Location", df["location"].unique())
event_filter = st.sidebar.multiselect("Event Type", df["event_name"].unique())

filtered_df = df.copy()
if location_filter:
    filtered_df = filtered_df[filtered_df["location"].isin(location_filter)]
if event_filter:
    filtered_df = filtered_df[filtered_df["event_name"].isin(event_filter)]

st.subheader("📋 Filter Results")
st.dataframe(filtered_df, use_container_width=True)

conn.close()
