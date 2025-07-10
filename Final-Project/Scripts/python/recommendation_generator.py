
import psycopg2

conn = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    port="26322",
    database="railway",
    user="postgres",
    password="QTKQKzFpfyrovjAhipitJCATMPXgWpkQ"
)

cur = conn.cursor()


recomendation = {
    'Drought': "Consider irrigation or drought-resistant crops.",
    'Flood': "Prepare drainage systems and avoid planting in low areas.",
    'Landslide': "Avoid field work in sloped areas; reinforce slopes.",
    'Hailstorm': "Install protective nets or delay planting.",
    'Frost': "Use plastic covers or early-harvest strategies for cold-sensitive crops."
}

cur.execute("""
    SELECT p.prediction_id, et.event_name
    FROM Prediction p
    JOIN Event_type et ON p.event_type_id = et.event_type_id
    WHERE NOT EXISTS (
        SELECT 1 FROM Recommendation r WHERE r.prediction_id = p.prediction_id
    );
""")

predicciones = cur.fetchall()           

for prediction_id, event_name in predicciones:
    description = recomendation.get(event_name)
    if description:
        cur.execute("""
            INSERT INTO Recommendation (recommen_descrip, prediction_id)
            VALUES (%s, %s)
        """, (description, prediction_id))
        print(f"Recommendation inserted for {prediction_id}: {event_name}")

conn.commit()
cur.close()
conn.close()
print("Process Completed.")
