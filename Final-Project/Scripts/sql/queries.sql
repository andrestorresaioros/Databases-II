
-- 1. Verificar usuarios registrados
SELECT * FROM "User";

-- 2. Ver ubicaciones geográficas
SELECT * FROM Location;

-- 3. Ver campos agrícolas de cada usuario
SELECT af.field_id, u.user_name, af.field_type
FROM Agriculture_field af
JOIN "User" u ON af.user_id = u.user_id;

-- 4. Ver cultivos por campo
SELECT c.crop_name, af.field_id, u.user_name
FROM Crop c
JOIN Agriculture_field af ON c.field_id = af.field_id
JOIN "User" u ON af.user_id = u.user_id;

-- 5. Ver estaciones meteorológicas y sus ubicaciones
SELECT ws.station_id, ws.name AS station_name, l.name AS location
FROM Weather_Station ws
JOIN Location l ON ws.location_id = l.location_id;

-- 6. Ver datos meteorológicos
SELECT * FROM Weather_Data ORDER BY timestamp DESC LIMIT 20;

-- 7. Ver relación entre estaciones y fuentes de datos
SELECT ws.name AS station, ds.name AS source, wds.start_date
FROM Weather_data_source wds
JOIN Weather_Station ws ON wds.station_id = ws.station_id
JOIN Data_source ds ON wds.source_id = ds.source_id;

-- 8. Ver predicciones climáticas recientes
SELECT p.prediction_id, p.timestamp, l.name AS location, et.event_name, p.probability
FROM Prediction p
JOIN Location l ON p.location_id = l.location_id
JOIN Event_type et ON p.event_type_id = et.event_type_id
ORDER BY p.timestamp DESC
LIMIT 20;

-- 9. Ver alertas enviadas
SELECT a.alert_id, u.user_name, et.event_name, a.status, a.timestamp_sent
FROM Alert a
JOIN "User" u ON a.user_id = u.user_id
JOIN Prediction p ON a.prediction_id = p.prediction_id
JOIN Event_type et ON p.event_type_id = et.event_type_id
ORDER BY a.timestamp_sent DESC;

-- 10. Ver recomendaciones generadas
SELECT r.recommen_descrip, et.event_name, l.name AS location, p.timestamp
FROM Recommendation r
JOIN Prediction p ON r.prediction_id = p.prediction_id
JOIN Event_type et ON p.event_type_id = et.event_type_id
JOIN Location l ON p.location_id = l.location_id
ORDER BY p.timestamp DESC;

-- 11. Ver predicciones sin recomendaciones aún
SELECT p.*
FROM Prediction p
WHERE NOT EXISTS (
    SELECT 1 FROM Recommendation r WHERE r.prediction_id = p.prediction_id
);

-- 12. Número total de eventos predichos por tipo
SELECT et.event_name, COUNT(*) AS total
FROM Prediction p
JOIN Event_type et ON p.event_type_id = et.event_type_id
GROUP BY et.event_name
ORDER BY total DESC;
