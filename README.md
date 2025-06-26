# Databases-II

# Project Name: Climate Risk Prediction System

## **Project Overview**

This project aims to develop a **Climate Risk Prediction System** designed for agricultural fields. The system leverages **big data**, **machine learning models**, and **real-time weather data** to predict climate-related risks (such as droughts, floods, and storms). The platform provides actionable recommendations to farmers based on the climate predictions, helping them take proactive measures to protect their crops.

The system will utilize satellite data, and historical climate data to provide accurate predictions, and it will offer a **business intelligence** module for management insights.

---

## **Business Model Canvas**

In this section, we define the key elements of the business model for the Climate Risk Prediction System.

- **Key Partners**:  
  - Weather data providers (e.g., OpenWeather, Copernicus)
  - Sensor manufacturers for real-time climate data
  - Cloud providers (e.g., AWS, Google Cloud)
  - Agricultural stakeholders (e.g., farmers, cooperatives)

- **Key Activities**:  
  - Data collection and integration
  - Development of predictive models using machine learning
  - User interface and dashboard creation
  - Implementation of a recommendation system for farmers

- **Value Propositions**:  
  - Real-time climate risk predictions for agricultural fields
  - Personalized recommendations to help farmers protect their crops
  - Business intelligence insights for farm managers

- **Customer Relationships**:  
  - Direct customer support for farmers
  - Regular system updates and notifications

- **Customer Segments**:  
  - Farmers and agricultural field owners
  - Agricultural cooperatives and consultancy firms

- **Channels**:  
  - Mobile app and web platform
  - SMS notifications for emergency alerts

- **Key Resources**:  
  - Machine learning models for climate predictions
  - Weather data sources
  - Cloud infrastructure for data storage and processing

- **Cost Structure**:  
  - Data storage and processing costs
  - Maintenance and development of prediction models
  - Infrastructure and hardware costs (sensors)

- **Revenue Streams**:  
  - Subscription-based service for farmers
  - Licensing of the prediction system to agricultural organizations

---

## **Project Requirements**

### **Functional Requirements**

| Number | Requirement | Description | Priority |
|--------|-------------|-------------|----------|
| FR1 | User registration | Allow registration of farmers, technicians, and managers via email or federated authentication (Google, Microsoft). | High |
| FR2 | Authentication and roles | Provide secure login with role-based access control to customize visible functionality based on user type. | High |
| FR3 | Continuous data ingestion | Integrate data from open weather sources in real time using tools such as Kafka or AWS Kinesis. | High |
| FR4 | Distributed storage | Store weather and agricultural data on a distributed, globally accessible basis with minimal latency. | High |
| FR5 | Weather data queries | Allow users to visualize real-time and historical information about weather conditions in their area. | High |
| FR6 | Predictive analytics | Run machine learning models to predict climate risks such as drought, frost, or heavy rainfall. | High |
| FR7 | Customized recommendations | Issue intelligent suggestions for planting, irrigation, or fertilization based on microclimates and analyzed data. | Medium |
| FR8 | Report generation | Produce customized reports for agricultural and governmental decision makers. | Medium |
| FR9 | Administrative panel | Enable user management and general system statistics by the administrator. | High |

### **Non-Functional Requirements**

| Number | Requirement | Description | Priority |
|--------|-------------|-------------|----------|
| NFR1 | Performance | Process queries with a maximum latency of 5 seconds for weather searches and predictions in agricultural areas. | High |
| NFR2 | Horizontal scalability | Allow adding nodes to handle large volumes of data and increase the number of concurrent users. | High |
| NFR3 | High availability | Guarantee 99.9% uptime with failover and automatic failover mechanisms. | High |
| NFR4 | Multi-location access | Allow access from multiple geographic regions with minimal load times through the use of CDNs or distributed clusters. | Medium |
| NFR5 | Interoperability | Integrate with third-party APIs such as OpenWeather and Copernicus, as well as IoT devices using standard protocols. | Medium |
| NFR6 | Usability | Design a responsive, intuitive, and fast web interface, accessible from different devices with low response times. | Medium |
| NFR7 | Maintainability | Have a modular and well-documented architecture that facilitates system upgrades, corrections, and scaling. | Medium |

---

## **User Stories**

### 1. As a farmer, I want to register using my email account so that I can access climate data and receive tailored recommendations.
### 2. As a farm manager, I want to view real-time and historical weather data for my region so that I can plan activities effectively.
### 3. As a client, I want to receive automatic alerts for upcoming extreme weather events in my area so that I can take preventive actions.
### 4. As an administrator, I want to manage user accounts and assign roles to ensure appropriate access control.
### 5. As an analyst, I want to generate reports about climate conditions and risk trends to support decision-making for stakeholders.

---

## **Initial Database Architecture**

### **Entities**:
1. **User**: Stores information about the users (farmers, administrators).
2. **Alert**: Stores weather alerts related to specific users.
3. **Prediction**: Contains climate predictions for agricultural fields.
4. **Agricultural_Field**: Represents fields associated with users and their geographical locations.
5. **Location**: Stores geographic information for agricultural fields.
6. **Weather_Data**: Represents real-time data collected from weather stations.
7. **Recommendation**: Stores recommendations based on predictions for specific fields.

### **Entity-Relationship Diagram (ERD)**:
![alt text](https://github.com/andrestorresaioros/Databases-II/blob/main/Workshop%20%231/Initial%20Database%20Architecture/MER.png)

---

## **System Architecture**

The AgroClimaIQ platform follows a layered architecture that supports:

- Continuous data ingestion via external APIs and synthetic generators (e.g., OpenWeather, NOAA, Python scripts).
- Real-time and batch processing using Apache Spark and internal scripts.
- Structured data storage in PostgreSQL and semi-structured storage in MongoDB.
- Data lake for raw climate archives (e.g., Amazon S3, HDFS).
- Business Intelligence module using Metabase or Apache Superset.
- REST and GraphQL APIs developed with FastAPI.
- Frontend interfaces built with React and secured via JWT/OAuth2.
- Optional Redis for caching frequent predictions and alerts.
### **High-level Architecture Diagram**:
![alt text](https://github.com/andrestorresaioros/Databases-II/blob/main/Workshop%20%232/Data%20System%20Architecture/Diagram.png)



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

---

## **Authors**

- **César Andrés Torres Bernal** (20191020147)
- **Juan David Duarte Ruiz** (20191020159)

This work is done under the **Databases II** course at **Universidad Distrital Francisco José de Caldas**.
