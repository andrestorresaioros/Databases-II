import requests
import psycopg2
from datetime import datetime
from datetime import timezone
import time


API_KEY = "d1fdc78d3bf810323096fcf866f183f9"  # ← reemplaza por tu API KEY real
CITY_NAME = "Bogotá"

DB_CONFIG = {
    "host": "turntable.proxy.rlwy.net",
    "port": "26322",
    "database": "railway",
    "user": "postgres",
    "password": "QTKQKzFpfyrovjAhipitJCATMPXgWpkQ"  # ← cambia por tu clave real
}

def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "station_name": data["name"],
            "timestamp": datetime.fromtimestamp(data["dt"], tz=timezone.utc)
        }
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

def insert_weather_data(weather):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    
    cur.execute("""
        INSERT INTO Location (name, latitude, longitude, type)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING;
    """, (CITY_NAME, weather["latitude"], weather["longitude"], "urban"))

    cur.execute("SELECT location_id FROM Location WHERE name = %s;", (CITY_NAME,))
    location_id = cur.fetchone()[0]

    
    cur.execute("""
        INSERT INTO Weather_Station (name, location_id)
        VALUES (%s, %s)
        ON CONFLICT (name) DO NOTHING;
    """, (weather["station_name"], location_id))

    cur.execute("SELECT station_id FROM Weather_Station WHERE name = %s;", (weather["station_name"],))
    station_id = cur.fetchone()[0]

    
    cur.execute("""
        INSERT INTO Weather_Data (station_id, timestamp, temperature, humidity, wind_speed)
        VALUES (%s, %s, %s, %s, %s);
    """, (station_id, weather["timestamp"], weather["temperature"], weather["humidity"], weather["wind_speed"]))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✔ Data inserted at {weather['timestamp']}")



MAX_CALLS = 100
DELAY_SECONDS = 2  

if __name__ == "__main__":
    for i in range(1, MAX_CALLS + 1):
        try:
            weather = fetch_weather_data(CITY_NAME)
            insert_weather_data(weather)
            print(f"📊 {i}/{MAX_CALLS} records stored.")
        except Exception as e:
            print(f"❌ Error on call {i}: {e}")
        time.sleep(DELAY_SECONDS)

    print("✅ API call loop completed (100 calls). Script finished.")
