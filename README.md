# 🌍 Air Quality Prediction and Analysis System

## 📌 Project Overview

This project analyzes air quality sensor readings and predicts Carbon Monoxide (CO) levels using Machine Learning techniques. The dataset contains 10,500+ environmental sensor records including pollutant concentrations, temperature, and humidity measurements.

The project focuses on data preprocessing, exploratory data analysis (EDA), correlation analysis, and predictive modeling using Linear Regression and Random Forest Regression.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

## 📂 Dataset Information

- Total Records: 10,500+
- Features: 11
- Target Variable: CO(GT)

### Dataset Columns

- CO(GT)
- PT08.S1(CO)
- C6H6(GT)
- PT08.S2(NMHC)
- NOx(GT)
- PT08.S3(NOx)
- NO2(GT)
- Temperature
- RH

---

## 🔄 Project Workflow

### 1. Data Cleaning
- Checked missing values
- Replaced invalid values (-200)
- Handled missing data using mean imputation

### 2. Exploratory Data Analysis
- CO Distribution Analysis
- NO2 Distribution Analysis
- Temperature vs CO Analysis
- Correlation Analysis

### 3. Feature Engineering
- Correlation-based feature selection
- Data preprocessing for machine learning

### 4. Machine Learning Models
- Linear Regression
- Random Forest Regression

### 5. Model Evaluation
- RMSE (Root Mean Squared Error)
- R² Score

---

## 📊 Visualizations

### Correlation Matrix
Identified relationships between pollutants and environmental variables.

### CO Distribution
Analyzed the distribution of Carbon Monoxide levels.

### NO2 Distribution
Studied Nitrogen Dioxide concentration patterns.

### Temperature vs CO
Observed the impact of temperature on CO levels.

### Actual vs Predicted CO
Compared machine learning predictions with actual values.

---

## 📈 Results

| Model | RMSE | R² Score |
|--------|--------|--------|
| Linear Regression | 0.2728 | 0.9225 |
| Random Forest | 0.2731 | 0.9223 |

---

## 🔍 Key Insights

- CO(GT) and PT08.S1(CO) show a very strong positive correlation (0.94).
- NOx(GT) and NO2(GT) have a strong relationship (0.93).
- Temperature positively influences CO concentration levels.
- Relative Humidity (RH) has minimal impact on pollutant concentrations.
- Linear Regression achieved the best performance with an R² score of 92%.

---

## 📁 Project Structure

```text
Air-Quality-Prediction-System
│
├── air_quality.py
├── air_quality_sensor_readings.csv
├── README.md
├── requirements.txt
│
└── screenshots
    ├── correlation_matrix.png
    ├── co_distribution.png
    ├── no2_distribution.png
    ├── temperature_vs_co.png
    └── actual_vs_predicted.png
```

---

## 🚀 Future Improvements

- Predict AQI (Air Quality Index)
- Deploy model using Streamlit
- Real-time air quality monitoring dashboard
- Hyperparameter tuning for improved accuracy

---

## 👨‍💻 Author

**Tanish Dabas**

B.Tech (AI & Data Science)  
University School of Automation and Robotics (USAR)
