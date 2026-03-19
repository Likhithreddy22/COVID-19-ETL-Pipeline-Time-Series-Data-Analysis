# COVID-19 ETL Pipeline & Data Analysis

This project implements an end-to-end ETL (Extract-Transform-Load) pipeline to process global COVID-19 time-series data.

The pipeline ingests raw CSV data, performs data cleaning and feature engineering using Python and Pandas, stores the processed dataset in PostgreSQL, and performs analytical queries with visualization.

## Features
- Data ingestion from raw COVID dataset
- Data cleaning and preprocessing
- Feature engineering (death rate, cases per million, rolling averages)
- Time-series transformation
- Storage in PostgreSQL database
- SQL-based analytical queries
- Visualization using Matplotlib

## Tech Stack
- Python
- Pandas
- NumPy
- SQLAlchemy
- PostgreSQL
- Matplotlib

## Pipeline Workflow
1. Extract raw COVID dataset
2. Transform data (cleaning + feature engineering)
3. Load processed data into PostgreSQL
4. Perform SQL analysis
5. Generate insights and visualizations

## Project Structure
