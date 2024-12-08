# Mage AI ETL Pipeline for Data Analytics

![Architecture Diagram](https://github.com/user-attachments/assets/4faf5c71-d76a-40f2-9fb0-3b35fcb5b333)

This project implements an ETL (Extract, Transform, Load) pipeline to process data and load it into **Google BigQuery** for analytics in **Looker Studio**. The pipeline is orchestrated using **Mage AI**, runs on **Google Compute Engine**, and leverages **Pandas** for data transformations.

---

## Architecture Overview

The pipeline consists of the following steps:

1. **Extract**  
   Data is extracted from an API or database source and stored in a temporary data frame for processing.
   
2. **Transform**  
   - Data is transformed using **Pandas** to clean, preprocess, and prepare it for analytics.
   - Transformations are orchestrated using **Mage AI**.

3. **Load**  
   The processed data is loaded into **Google BigQuery** for scalable storage and querying.

4. **Analyze**  
   Data in BigQuery is visualized and analyzed using **Looker Studio**.

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

