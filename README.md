# Flight Price Prediction

A regression-based machine learning project to predict flight prices based on travel and airline-related features.

---

## ➤ Project Summary

- Developed a machine learning model to predict flight ticket prices using historical data.
- Used regression techniques to model the relationship between flight attributes and their prices.
- Handled feature extraction, encoding, and model evaluation from scratch.
- Achieved high prediction accuracy using tree-based models.

---

## ➤ Dataset

- Publicly available flight fare dataset containing:
  - Airline
  - Source & Destination
  - Date of Journey
  - Total Stops
  - Duration
  - Additional Info
- Target variable: Flight Price

---

## ➤ Preprocessing

- Extracted features from dates and durations
- Encoded categorical features using one-hot and label encoding
- Handled missing values and outliers
- Converted duration into numerical format

---

## ➤ Modeling

- Compared various regression models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
- Selected the best model based on R² score and RMSE

---

## ➤ Results

- Best Model: XGBRegressor
- Achieved R² Score: *e.g., 0.83*
---

## ➤ How to Use

1. Clone the repository
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
3.Run the Jupyter notebook:
<pre>
  jupyter notebook Flight_Price_Prediction.ipynb
</pre>

## ➤ Key Learnings
End-to-end regression modeling pipeline.<br>

Data cleaning, feature engineering, and encoding.<br>

Model tuning and evaluation with practical metrics.<br>

Understanding how travel-related features impact price.<br>


---

