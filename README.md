# Bogor Women Violence Analytics

A data analytics dashboard for analyzing patterns of violence against women in Bogor City, West Java, Indonesia (2017-2022). This project combines exploratory data analysis, K-Means clustering, and an interactive Streamlit dashboard to help stakeholders identify high risk areas and improve case handling.

This project is a rebuilt and extended version of my bachelor's thesis titled **"Implementasi Algoritma K-Means Untuk Clustering Jumlah Korban Kekerasan Terhadap Perempuan Di Kota Bogor"** (2024). The original thesis focused solely on K-Means clustering. This project expands it into a full analytics pipeline with exploratory data analysis and an interactive dashboard.

---

## Problem Statement

Violence against women remains a significant social issue in Bogor City. This project aims to help government agencies and NGOs better understand the patterns of violence cases. Including which districts are most affected, what types of violence are most common, and how effectively cases are being handled. So that resources can be allocated more strategically.

---

## Features

- **Exploratory Data Analysis (EDA)** — trends by year, district, and type of violence
- **K-Means Clustering** — grouping districts by violence severity level (Low, Medium, High)
- **Interactive Dashboard** — filter by year, district, and violence type
- **Case Handling Analysis** — overview of case resolution status

---

## Tech Stack

Python 
Pandas : Data manipulation and analysis
Seaborn & Matplotlib : Data visualization
Scikit-learn : K-Means clustering 
Streamlit : Interactive web dashboard 

---

## Project Structure

bogor-women-violence-analytics/
├── app.py               # Main Streamlit dashboard
├── utils/
│   └── analysis.py      # Data loading, preprocessing, and analysis functions
├── data/                # Dataset (not included, see note below)
└── README.md

---

## Dataset

The dataset contains records of violence against women in Bogor City from 2017 to 2022, sourced from local government data used in my bachelor's thesis research.

**Note:** The dataset is not included in this repository to protect the privacy of victims. The dataset contains the following fields:

- District (Kecamatan)
- Type of violence
- Month and year
- Case status
- Case handling information

---

## Installation

# Clone the repository
git clone https://github.com/yourusername/bogor-women-violence-analytics.git
cd bogor-women-violence-analytics

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pandas streamlit seaborn scikit-learn matplotlib openpyxl

---

## How to Run

streamlit run app.py

---

## Key Insights

- Districts with the highest number of cases were identified and clustered into risk levels
- Certain types of violence showed significant increases in specific years
- Case handling rates varied significantly across districts