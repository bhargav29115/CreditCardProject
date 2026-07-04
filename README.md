# Credit Card Fraud Detection System

## Project Overview
This project is a Machine Learning-based web application that predicts whether a credit card transaction is **Fraudulent** or **Legitimate**. The trained model is integrated with a Flask web application for real-time predictions.

## Technologies Used
- Python
- Flask
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- HTML & CSS
- Joblib

## Machine Learning Models
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

## Features
- Data preprocessing
- Data visualization
- Model training and evaluation
- Best model selection
- Real-time prediction using Flask

## Project Structure

```
CreditCardProject/
│
├── app.py
├── best_creditcard_model.pkl
├── requirements.txt
├── static/
└── templates/
```

## How to Run

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser:
```
http://127.0.0.1:5000
```

## Outcome
The application predicts whether a credit card transaction is **Fraudulent** or **Legitimate** based on the user input.