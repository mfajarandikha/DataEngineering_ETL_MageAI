# Mage AI ETL Pipeline for Data Analytics

## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline for processing and analyzing taxi trip data, orchestrated using **Mage AI** and **Pandas**. The pipeline extracts data from APIs and local files, transforms it into analytical tables, and loads it into Google BigQuery for visualization in Looker Studio.

Key highlights:
- Designed to handle large datasets (1.4 million rows of taxi trip data).
- Built for efficient data processing on a cost-effective Google Compute Engine virtual machine (VM).
- Uses a modular architecture to split pipeline nodes by tables, reducing throughput and cost.

---

## Architecture Overview
![Architecture Diagram](https://github.com/user-attachments/assets/4faf5c71-d76a-40f2-9fb0-3b35fcb5b333)

The ETL process is divided into three main stages:
1. **Extract**: Taxi trip data and location lookup tables are collected from APIs and source files.
2. **Transform**: Data is processed into normalized tables, including:
   - Fact table
   - Dimension tables (Date Time, Drop-off Location, Passenger Count, Payment Type, Trip Distance, Pickup Location, Rate Code).
3. **Load**: Processed tables are loaded into BigQuery for analysis.
---

### Data Processing Strategy

![Data Processing](https://github.com/user-attachments/assets/e572eddf-1813-4f5d-abfd-5eec90aa2703)

Due to the large dataset size (1.4 million rows) and the limitations of a low-cost VM:
- **Pipeline Splitting**: Each table in the transformation step is processed in separate nodes to reduce memory usage and throughput pressure.
- This approach minimizes costs and optimizes performance for scalable ETL processing.

---

## Deployment Details

### Tools & Platforms
- **Mage AI**: Pipeline orchestration.
- **Google Cloud Platform (GCP)**:  
  - **Compute Engine**: For running the pipeline.  
  - **BigQuery**: For data storage and analytics.
  - **Looker Studio**: For data visualization.
- **Pandas**: For transformation.

### Pipeline Flow
1. **VM Compute Engine**: Hosts the pipeline execution.
2. **Mage AI**: Manages the workflow and scheduling of tasks.
3. **BigQuery**: Receives the transformed data for analytics.
4. **Looker Studio**: Connects to BigQuery for visualization and dashboards.
---

## Results
- Data is available in BigQuery for querying.
- Dashboards in Looker Studio provide real-time analytics and insights.
    (https://lookerstudio.google.com/s/pGa41KkFdh4)
---


