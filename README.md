# Databases II 
## Workshop No. 1  
##  AgroClima: A Smart Agro-Climatic Decision Support Platform

---

## Introduction to the Business Model

AgroClima is a smart agro-climatic decision support platform designed to provide advanced climate-based solutions for farmers and agricultural organizations. The core idea is to leverage climate data and artificial intelligence tools to deliver accurate and timely recommendations that enhance agricultural decision-making in the face of adverse weather conditions.

The platform addresses the high vulnerability of the agricultural sector to extreme weather events such as droughts, frosts, and heavy rainfall, which result in substantial crop losses, reduced productivity, and threats to food security. Currently, many farmers lack effective and accessible tools to anticipate and adapt to these challenges.

The final product is a user-friendly web platform adapted for rural areas with limited connectivity. It will deliver personalized alerts, agricultural management recommendations, and optimized resource strategies (water, fertilizers), while providing institutions with access to regional climate risk information.

---

## Business Model Canvas

### Key Partners
- Weather data providers (OpenWeather, Copernicus, IDEAM)
- IoT sensor manufacturers and distributors
- Ministries of Agriculture, NGOs, and government agencies
- Universities and research institutes
- Payment platforms and rural banking services
- Agricultural input distributors

### Key Activities
- Design of forecasting and advisory services
- Awareness and adoption campaigns
- Strategic partnerships with public/private actors
- Platform development and maintenance

### Value Propositions

**For Farmers:**
- Localized and actionable recommendations
- Risk mitigation for drought, frost, and rainfall
- Efficient resource use (water/fertilizers)
- Easy-to-use system

**For Institutions:**
- Access to agro-climatic reports and regional data
- Tools for subsidy planning, insurance, and support
- Support for public policies and climate risk mitigation

### Customer Relationships
- Multichannel technical assistance (chat, phone, email)
- Onboarding and support for low-digitalization regions
- Automated and personalized alerts

### Customer Segments
- Small and medium farmers
- Technified producers with IoT integration
- Local/national governments
- Agribusinesses and climate-risk managers

### Channels
- Web platform adapted for rural connectivity
- APIs for institutional integration
- Implementation via agricultural agencies and cooperatives

### Key Resources
- Strategic alliances in agriculture/climate
- Reliable satellite and climate data
- AI/machine learning for predictive analytics
- Scalable infrastructure for data processing

### Cost Structure
- Operation of partnerships and training
- Processing and storage of satellite/climate data
- Outreach campaigns
- Continuous improvement of the recommendation system
- Technical maintenance and infrastructure

### Revenue Streams
- Monthly or annual farmer subscriptions (tiered)
- Institutional licenses for governments
- Premium services: consulting, data, risk maps
- Freemium model (basic free, advanced paid)
- Sponsored access via insurance or input companies

---

## Functional Requirements

| ID   | Requirement                  | Description                                                                                  | Priority |
|------|------------------------------|----------------------------------------------------------------------------------------------|----------|
| FR1  | User registration            | Allow farmers, technicians, and administrators to register using email or third-party login | High     |
| FR2  | Authentication and access    | Secure login with differentiated access by role                                              | High     |
| FR3  | Continuous data ingestion    | Ingest near real-time data from open or authorized weather sources                           | High     |
| FR4  | Distributed data storage     | Efficient access and storage of data from any location with low latency                      | High     |
| FR5  | Weather data queries         | Query and visualize current/historical weather conditions                                    | High     |
| FR6  | Climate risk prediction      | Predict droughts, frosts, or heavy rainfall                                                  | High     |
| FR7  | Agricultural recommendations | Generate recommendations based on microclimates                                              | Medium   |
| FR8  | Report generation            | Create custom reports for users and institutions                                             | Medium   |
| FR9  | Administrative panel         | Tools to manage users, roles, and system statistics                                          | High     |

---

## Non-Functional Requirements

| ID    | Requirement             | Description                                                                 | Priority |
|-------|-------------------------|-----------------------------------------------------------------------------|----------|
| NFR1  | Performance             | Timely responses to queries and predictions under expected data volumes     | High     |
| NFR2  | Horizontal scalability  | Efficient scaling for growing users and data ingestion                      | High     |
| NFR3  | High availability       | Minimal downtime through automatic recovery                                 | High     |
| NFR4  | Multi-region access     | Consistent performance regardless of user location                          | Medium   |
| NFR5  | Interoperability        | Integration with external data/APIs using standard protocols                | Medium   |
| NFR6  | Usability               | Interface should be intuitive and responsive across devices and networks    | Medium   |
| NFR7  | Maintainability         | Modular, well-documented architecture for scaling and updates               | Medium   |

---

## Prioritization Strategy

Requirements were prioritized using the following criteria:
- **Impact on the end user**
- **Operational dependency**
- **Expected frequency of use**
- **Strategic value**
- **Effort vs. complexity**

High and medium priorities were assigned collaboratively with developers and pilot users.

---

## Performance and Capacity Analysis

### System Assumptions
- 2,000 users in Year 1
- 500 peak concurrent users (25%)
- 1,200 sensors (1 record/minute → 1.7M records/day)
- Rural bandwidth: 2–5 Mbps, with unstable latency
- Peak usage: 5–8 AM and 6–9 PM

### Performance Targets

| Metric                  | Target                         | Source of Estimate                                       |
|------------------------|---------------------------------|----------------------------------------------------------|
| Response latency (p95) | ≤ 3 seconds                     | Based on UI/load tests over rural bandwidth              |
| Response latency (p99) | ≤ 5 seconds                     | Ensures UX even in edge cases                           |
| Data update delay      | ≤ 2 minutes                     | 1 min emission + 1 min ingestion                         |
| Ingestion throughput   | 2,000 reg/s (6,000 peak)        | 1.7M records/day × safety factor (×3–5)                 |
| Availability           | ≥ 99.5% uptime                  | Balanced for mid-tier infrastructure                    |
| Payload size           | ≤ 150 KB                        | Suitable for 3G/4G loading under 0.5s                   |
| Scalability            | Double throughput in < 1 hour   | Based on pilot auto-scaling results                     |

**Source**: User interviews (n=50), field bandwidth tests, simulated workloads.

---

## User Stories

| Role          | Story                                                                                       |
|---------------|----------------------------------------------------------------------------------------------|
| Farmer        | As a farmer, I want personalized alerts for my field so I can take timely preventive action |
| Farmer        | I want tailored irrigation and fertilization advice based on the crop and location          |
| Analyst       | I want access to weather data and predictions to monitor risks across different zones       |
| Administrator | I want to manage system users and roles for secure access control                           |
| Administrator | I want to view system usage statistics and generate global reports                          |

---

## Initial Database Architecture

The system was modeled using a 10-step methodology to design entities, attributes, and relationships.

### Main Entities
- `User`, `Agriculture_Field`, `Crop`, `Location`, `Prediction`, `Alert`, `Recommendation`, `Weather_Station`, `Weather_Data`, `Event_Type`, `Severity_Level`, `Model`, `Data_Source`

### Relationships
- 1:N — User → Fields, Alerts  
- 1:N — Prediction → Alerts, Recommendations  
- N:M — Weather Station ↔ Data Source (handled via associative entity)

### Key Features
- Role-based access
- Geographic linkage of fields and weather stations
- Trackable predictions and alerts
- Modular and scalable schema

### Entity-Relationship Diagram (ERD):
![alt text](https://github.com/andrestorresaioros/Databases-II/blob/main/Workshop%20%231/Initial%20Database%20Architecture/MER.png)



## Workshop No. 2
## AgroClima: Data System Architecture and Information Retrieval

---

## System Architecture Overview

AgroClima is designed as a scalable, layered, data-driven platform that supports real-time ingestion, processing, storage, and delivery of agro-climatic intelligence. Its modular design allows continuous integration of external sources, predictive model execution, and responsive user interfaces for decision-making at field and institutional levels.

---

## Architecture Layers

### 1. Data Sources Layer
- **Role**: Entry point for all weather/climate/agricultural data.
- **Components**:
  - External APIs: OpenWeather, NOAA, OpenMeteo
  - Synthetic data via Python (Faker, NumPy, Pandas)
- **Interaction**: Scheduled or real-time data sent to ingestion layer

### 2. Data Ingestion Layer
- **Role**: Normalize, validate, and route data
- **Technology**: Apache Kafka for high-throughput, decoupled streaming
- **Destination**: Structured → PostgreSQL; Semi/unstructured → MongoDB

### 3. Data Storage Layer
- **Role**: Store raw and refined data
- **Technologies**:
  - PostgreSQL (structured: users, predictions, alerts)
  - Optional Data Lake: Amazon S3 or HDFS for bulk historical data

### 4. Data Processing & Intelligence Layer
- **Role**: Execute ML models, detect anomalies, forecast risks
- **Interaction**: Read/write to PostgreSQL via internal scripts

### 5. Business Intelligence (BI) Module
- **Role**: Support strategic decision-making via dashboards
- **Technologies**:
  - SQL queries, materialized views from PostgreSQL
  - Log-based visualizations from MongoDB

### 6. Application & Serving Layer
- **Role**: Expose APIs, manage business logic and sessions
- **Technologies**:
  - FastAPI (REST/GraphQL)
  - Backend access control, Redis (optional cache)

### 7. Frontend / Access Layer
- **Role**: Interface for farmers, analysts, and admins
- **Technology**: Responsive React dashboards

---
### **High-level Architecture Diagram**:
![alt text](https://github.com/andrestorresaioros/Databases-II/blob/main/Workshop%20%232/Data%20System%20Architecture/Arquitectura%20BS2.png)



---

## **Information Requirements**

The platform must support the retrieval and storage of:

- **User Profiles & Roles**: Role-based access, associated fields and preferences.
- **Climate Predictions**: Events, probabilities, severity, timestamps, model IDs.
- **Recommendations**: Linked to predictions, personalized to user and crop.
- **Weather Data**: Timestamped records from stations and locations.
- **Agricultural Fields**: Geolocation, crop type, ownership.
- **Alerts**: Delivery tracking and alert history per user.
- **API Raw Responses**: Stored in MongoDB for debugging and model validation.
- **Interaction Logs**: Logs of usage patterns and feedback for UX and analytics.

---

## **Sample Queries**

### Retrieve Users by Role
```sql
SELECT user_id, user_name, role, email
FROM User
WHERE role = 'Farmer';
```

### Recent Climate Risk Predictions
```sql
SELECT p.prediction_id, e.event_name, l.name AS location, p.probability, s.severity_type, p.timestamp
FROM Prediction p
JOIN Event_type e ON p.event_type_id = e.event_type_id
JOIN Severity_level s ON p.severity_level_type_id = s.severity_level_id
JOIN Location l ON p.location_id = l.location_id
WHERE p.timestamp >= CURRENT_DATE - INTERVAL '7 days';
```

### Personalized Recommendations
```sql
SELECT u.user_name, c.crop_name, af.field_id, r.recommend_descrip, p.timestamp
FROM Recommendation r
JOIN Prediction p ON r.prediction_id = p.prediction_id
JOIN Agriculture_Field af ON r.field_id = af.field_id
JOIN Crop c ON af.crop_id = c.crop_id
JOIN User u ON af.user_id = u.user_id
WHERE u.user_id = 1
ORDER BY p.timestamp DESC;
```

### Last 24h Weather Data
```sql
SELECT wd.timestamp, wd.temperature, wd.humidity, ws.station_name, l.name AS location
FROM Weather_Data wd
JOIN Weather_Station ws ON wd.station_id = ws.station_id
JOIN Location l ON ws.location_id = l.location_id
WHERE wd.timestamp BETWEEN NOW() - INTERVAL '1 DAY' AND NOW();
```

### Alerts Received by User
```sql
SELECT u.user_name, e.event_name, a.status, a.timestamp_sent
FROM Alert a
JOIN User u ON a.user_id = u.user_id
JOIN Prediction p ON a.prediction_id = p.prediction_id
JOIN Event_type e ON p.event_type_id = e.event_type_id
WHERE u.user_id = 1
ORDER BY a.timestamp_sent DESC;
```

### MongoDB - User Interaction Log (Latest 5)
```javascript
db.interaction_logs.find({
  interaction_type: "recommendation_viewed",
  user_id: "u001"
}).sort({ timestamp: -1 }).limit(5);
```

### MongoDB - Raw API Responses
```javascript
db.api_responses.find({
  source: "OpenWeather",
  "location.name": "Cali",
  timestamp: { $gte: ISODate("2025-05-27T00:00:00Z") }
}).sort({ timestamp: -1 }).limit(10);
```
## Final Project
# AgroClima: Climate Monitoring and Agricultural Prediction Platform

AgroClima is a distributed system designed to support climate monitoring and risk prediction for agricultural fields. It integrates real-time weather data ingestion, machine learning-based predictions, and rule-based recommendations to assist farmers and analysts in decision-making.

---

## Project Overview

This platform allows you to:

- Collect real-time weather data from public APIs (e.g., OpenWeather).
- Store data in a structured PostgreSQL database (hosted on Railway).
- Automate data ingestion using schedulers or loops.
- Generate weather-based predictions using basic machine learning rules.
- Issue recommendations and alerts based on predicted climate risks.
- Visualize all information via an interactive dashboard built with Streamlit.

---

## Database Structure (`AgroClimaDB.sql`)

The system uses **PostgreSQL**, deployed on **Railway**, as the main relational database.

### Main Tables:

- **User**: System users (`admin`, `analyst`, `client`).
- **Location**: Geographical areas (name, coordinates, type).
- **Agriculture_field**: Fields linked to users.
- **Crop**: Crop types planted per field.
- **Weather_Station**: Linked to physical locations.
- **Weather_Data**: Temperature, humidity, wind data records.
- **Data_source**: API providers like OpenWeather.
- **Weather_data_source**: Links stations and data sources.
- **Event_type**: Risk events like droughts, floods, etc.
- **Prediction**: Forecasted events with probabilities.
- **Alert**: Notifications sent to users.
- **Recommendation**: Suggested actions per prediction.

### Tools used:

- **Railway** (PostgreSQL hosting)
- **DBeaver** (SQL script execution and schema management)

---

## Tracked Weather Events

The platform models five types of climate events that affect agriculture:

| Event      | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| Drought    | Extended period of low rainfall, affecting crops and water availability     |
| Flood      | Excessive rainfall causing overflow or field saturation                     |
| Landslide  | Slope instability due to intense rain, common in hilly zones                |
| Hailstorm  | Storms with hail that may damage crops and infrastructure                   |
| Frost      | Nighttime cold spells that freeze plants, especially in high-altitude zones |

---

## Python Setup & Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Required libraries:

- `requests`
- `psycopg2`
- `pandas`
- `streamlit`

---

## Weather Data Ingestion (`ingest_openweather.py`)

Fetches live data from OpenWeather and stores it in the database.

### How it works:

1. Calls OpenWeather API for temperature, humidity, wind speed, etc.
2. Ensures the location and station exist in the DB.
3. Inserts a new row in `Weather_Data`.
4. Loops 100 times with 2-second delays to simulate real-time ingestion.

### Run:

```bash
python ingest_openweather.py
```

---

## Event Prediction (`event_prediction.py`)

This script processes aggregated weather data and classifies possible climate events based on predefined conditions using basic rule-based logic.

### How it works:

1. Fetches weather records from the database and aggregates daily means by location.
2. Applies rule-based logic to detect events like Drought, Flood, Frost, etc.
3. Calculates a severity-based probability (between 0 and 1) for each predicted event.
4. Inserts predictions into the `Prediction` table in the database.

### Detected Events:

- **Frost**: Temp ≤ 0°C, Humidity ≥ 80%, Wind < 5
- **Hailstorm**: Wind ≥ 25, Temp 0–15°C, Humidity 60–90%
- **Landslide**: Humidity > 90%, Temp < 15°C, Wind ≥ 5
- **Flood**: Humidity > 85%, Temp > 5°C, Wind ≥ 3
- **Drought**: Temp > 30°C, Humidity < 30%, Wind > 5

### Run:

```bash
python event_prediction.py
```

This will populate the `Prediction` table based on recent weather data.

---

## Recommendation Generator (`recommendation_generator.py`)

Generates tailored advice for predictions that don’t yet have a recommendation.

### Example strategies:

- **Drought** → Consider irrigation or drought-resistant crops.
- **Flood** → Prepare drainage systems and avoid planting in low areas.
- **Landslide** → Avoid field work in sloped areas; reinforce slopes.
- **Hailstorm** → Install protective nets or delay planting.
- **Frost** → Use plastic covers or early-harvest strategies.

### Run:

```bash
python recommendation_generator.py
```

---

## Web Dashboard with Streamlit (`climate_dashboard.py`)

Visualizes predictions and recommendations in a responsive web app.

### Features:

- Displays a complete table of predictions with event types, locations, probabilities, and recommendations.
- Sidebar filters by location and event type.
- Responsive layout using Streamlit.

### Run:

```bash
streamlit run climate_dashboard.py
```

Make sure your database is running and accessible.

---

## Status

- Database schema defined and deployed via Railway  
- Real-time ingestion from OpenWeather API  
- Recommendation logic implemented  
- Interactive dashboard functional  

---
---
## video
https://drive.google.com/file/d/1JC0PaLH88czyGFrcopBVIsWXGEAf6JH1/view?usp=sharing
## **Authors**

- **César Andrés Torres Bernal** (20191020147)
- **Juan David Duarte Ruiz** (20191020159)

This work is done under the **Databases II** course at **Universidad Distrital Francisco José de Caldas**.
