-- ========== TABLE: User ==========
CREATE TABLE IF NOT EXISTS "User" (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'analyst', 'client')),
    password_hash VARCHAR(100) NOT NULL
);

-- ========== TABLE: Location ==========
CREATE TABLE IF NOT EXISTS Location (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    latitude DECIMAL NOT NULL CHECK (latitude BETWEEN -90 AND 90),
    longitude DECIMAL NOT NULL CHECK (longitude BETWEEN -180 AND 180),
    type VARCHAR(100) NOT NULL
);

-- ========== TABLE: Agriculture_field ==========
CREATE TABLE IF NOT EXISTS Agriculture_field (
    field_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES "User"(user_id),
    field_type INT NOT NULL
);

-- ========== TABLE: Crop ==========
CREATE TABLE IF NOT EXISTS Crop (
    crop_id SERIAL PRIMARY KEY,
    field_id INT NOT NULL REFERENCES Agriculture_field(field_id),
    crop_name VARCHAR(200) NOT NULL
);

-- ========== TABLE: Weather_Station ==========
CREATE TABLE IF NOT EXISTS Weather_Station (
    station_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    location_id INT NOT NULL REFERENCES Location(location_id)
);

-- ========== TABLE: Weather_Data ==========
CREATE TABLE IF NOT EXISTS Weather_Data (
    data_id SERIAL PRIMARY KEY,
    station_id INT NOT NULL REFERENCES Weather_Station(station_id),
    timestamp TIMESTAMP NOT NULL,
    temperature FLOAT CHECK (temperature BETWEEN -80 AND 60),
    humidity FLOAT CHECK (humidity BETWEEN 0 AND 100),
    wind_speed FLOAT CHECK (wind_speed >= 0)
);

-- ========== TABLE: Data_source ==========
CREATE TABLE IF NOT EXISTS Data_source (
    source_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL,
    url VARCHAR(100)
);

-- ========== TABLE: Weather_data_source ==========
CREATE TABLE IF NOT EXISTS Weather_data_source (
    station_id INT NOT NULL REFERENCES Weather_Station(station_id),
    source_id INT NOT NULL REFERENCES Data_source(source_id),
    start_date TIMESTAMP NOT NULL,
    PRIMARY KEY (station_id, source_id)
);

-- ========== TABLE: Event_type ==========
CREATE TABLE IF NOT EXISTS Event_type (
    event_type_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    event_description VARCHAR(200)
);

-- ========== TABLE: Prediction ==========
CREATE TABLE IF NOT EXISTS Prediction (
    prediction_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    location_id INT NOT NULL REFERENCES Location(location_id),
    probability DECIMAL NOT NULL CHECK (probability BETWEEN 0 AND 1),
    event_type_id INT NOT NULL REFERENCES Event_type(event_type_id)
);

-- ========== TABLE: Alert ==========
CREATE TABLE IF NOT EXISTS Alert (
    alert_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES "User"(user_id),
    prediction_id INT NOT NULL REFERENCES Prediction(prediction_id),
    timestamp_sent TIMESTAMP NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'active', 'resolved'))
);

-- ========== TABLE: Recommendation ==========
CREATE TABLE IF NOT EXISTS Recommendation (
    recommen_id SERIAL PRIMARY KEY,
    recommen_descrip VARCHAR(300) NOT NULL,
    prediction_id INT NOT NULL REFERENCES Prediction(prediction_id)
);
