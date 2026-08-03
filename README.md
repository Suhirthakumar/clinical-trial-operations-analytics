# Clinical Trial Operations Analytics Platform

## Overview

Clinical Trial Operations Analytics is a Python-based analytics platform designed to demonstrate clinical informatics workflows for clinical research operations.

The project simulates clinical trial datasets and applies data engineering, SQL analytics, data quality assessment, and dashboard visualisation techniques to identify operational insights and potential trial risks.

This project was developed as a portfolio project for Clinical Informatics Analyst roles within Clinical Research Organisations (CROs).

---

# Project Objectives

The objectives of this project are:

- Generate synthetic clinical trial operational datasets
- Store clinical trial data in a relational SQLite database
- Perform data quality assessments
- Analyse recruitment and operational performance
- Visualise clinical trial metrics through an interactive dashboard
- Develop predictive models for clinical trial risk assessment

---

# Technologies Used

## Programming

- Python 3.11

## Data Analysis

- Pandas
- NumPy

## Database

- SQLite
- SQL

## Visualisation

- Streamlit
- Plotly
- Matplotlib

## Machine Learning

- Scikit-learn

## Development Environment

- Conda
- VS Code
- GitHub

---

# Project Structure
clinical-trial-operations-analytics/

│
├── data/
│ ├── clinical_trials.csv
│ ├── patients.csv
│ ├── adverse_events.csv
│ └── sites.csv
│
├── database/
│ └── clinical_trial.db
│
├── dashboard/
│ └── app.py
│
├── sql/
│ └── analysis_queries.sql
│
├── src/
│ ├── generate_data.py
│ ├── database_setup.py
│ ├── analytics.py
│ └── quality_checks.py
│
├── notebooks/
│
├── models/
│
├── requirements.txt
│
├── README.md
│
└── LICENSE