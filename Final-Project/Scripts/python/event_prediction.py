
import pandas as pd
import psycopg2
from datetime import datetime
from decimal import Decimal


conn = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    port="26322",
    database="railway",
    user="postgres",
    password="QTKQKzFpfyrovjAhipitJCATMPXgWpkQ"
)


query = """
SELECT wd.timestamp, wd.temperature, wd.humidity, wd.wind_speed, 
       ws.station_id, l.location_id, l.name AS location_name
FROM Weather_Data wd
JOIN Weather_Station ws ON wd.station_id = ws.station_id
JOIN Location l ON ws.location_id = l.location_id
ORDER BY wd.timestamp;
"""

df = pd.read_sql_query(query, conn)
print("consulta hecha")


df['timestamp'] = pd.to_datetime(df['timestamp'])
df['day'] = df['timestamp'].dt.date


agg_df = df.groupby(['location_id', 'day']).agg({
    'temperature': 'mean',
    'humidity': 'mean',
    'wind_speed': 'mean'
}).reset_index()

print("procesamiento de datos")

def classify_event(row):
    temp = row['temperature']
    hum = row['humidity']
    wind = row['wind_speed']

    # Frost
    if temp <= 0 and hum >= 80 and wind < 5:
        severity = (80 - temp) * 0.02 + (hum - 80) * 0.01
        prob = min(1.0, 0.7 + severity)
        print(f"Frost → temp={temp}, hum={hum}, wind={wind}, severity={severity}, prob={prob}")
        return 'Frost', prob

    # Hailstorm
    if wind >= 25 and 0 <= temp <= 15 and 60 <= hum <= 90:
        severity = (wind - 25) * 0.01 + (90 - abs(temp - 10)) * 0.005
        prob = min(1.0, 0.75 + severity)
        print(f"Hailstorm → temp={temp}, hum={hum}, wind={wind}, severity={severity}, prob={prob}")
        return 'Hailstorm', prob

    # Landslide
    if hum > 90 and temp < 15 and wind >= 5:
        severity = (hum - 90) * 0.01 + (15 - temp) * 0.01 + (wind - 5) * 0.005
        prob = min(1.0, 0.65 + severity)
        print(f"Landslide → temp={temp}, hum={hum}, wind={wind}, severity={severity}, prob={prob}")
        return 'Landslide', prob

    # Flood
    if hum > 85 and temp > 5 and wind >= 3:
        severity = (hum - 85) * 0.01 + (wind - 3) * 0.01
        prob = min(1.0, 0.7 + severity)
        print(f"Flood → temp={temp}, hum={hum}, wind={wind}, severity={severity}, prob={prob}")
        return 'Flood', prob

    # Drought
    if temp > 30 and hum < 30 and wind > 5:
        severity = (temp - 30) * 0.02 + (30 - hum) * 0.01 + (wind - 5) * 0.01
        prob = min(1.0, 0.75 + severity)
        print(f"Drought → temp={temp}, hum={hum}, wind={wind}, severity={severity}, prob={prob}")
        return 'Drought', prob

    return None, None

agg_df[['event_name', 'probability']] = agg_df.apply(lambda row: pd.Series(classify_event(row)), axis=1)

print(agg_df[['location_id', 'day', 'temperature', 'humidity', 'wind_speed', 'event_name', 'probability']].head(10))
print("Total filas con eventos predichos:", agg_df['event_name'].notnull().sum())


cur = conn.cursor()

for _, row in agg_df.iterrows():
    if pd.isnull(row['event_name']) or pd.isnull(row['probability']):
        continue

    
    cur.execute("SELECT event_type_id FROM Event_type WHERE event_name = %s", (row['event_name'],))
    result = cur.fetchone()
    if not result:
        continue
    event_type_id = result[0]

    timestamp = datetime.combine(row['day'], datetime.min.time())

    
    print(f"Insertando predicción: fecha={timestamp}, loc_id={row['location_id']}, evento={row['event_name']}, prob={row['probability']}")
    cur.execute("""
        INSERT INTO Prediction (timestamp, location_id, probability, event_type_id)
        VALUES (%s, %s, %s, %s)
    """, (timestamp, int(row['location_id']), Decimal(str(row['probability'])), event_type_id))
    print("Insertando en...")

conn.commit()
cur.close()
conn.close()
print("Predicciones insertadas correctamente.")
