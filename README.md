 # 📈 Stock Market Prediction & Investment Recommendation System

A machine learning–based stock market analysis web application that predicts the **next day stock price** and provides an **investment recommendation** (Good to Invest / Hold / Not Good to Invest) using historical stock data and technical indicators.

Built using **Python, LSTM neural networks, and Streamlit**, with real-time data fetched from **Yahoo Finance**.

---

## Features

- Fetches real stock market data using Yahoo Finance  
- Predicts next-day stock price using **LSTM (Long Short-Term Memory)**  
- Calculates technical indicators:
  - 50-day Moving Average
  - 200-day Moving Average
  - RSI (Relative Strength Index)
-  Generates investment recommendations:
  - 🟢 Good to Invest
  - 🟡 Wait / Hold
  - 🔴 Not Good to Invest
- 🌐 Interactive **Streamlit web interface**
- 🕒 User-selectable company and date range

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- TensorFlow / Keras  
- Pandas  
- NumPy  
- Scikit-learn  
- yFinance  

---

## How It Works

1. User selects a stock ticker and date range
2. Historical stock prices are downloaded from Yahoo Finance
3. Data is scaled and converted into LSTM sequences
4. LSTM model predicts the next day closing price
5. Technical indicators (Moving Averages, RSI) are calculated
6. Decision logic evaluates trend, momentum, and expected return
7. Results are displayed on the web interface

---

## 📊 Investment Decision Logic

IF expected return > 3%
AND 50-day MA > 200-day MA
AND RSI between 40 and 70
→ 🟢 GOOD TO INVEST

ELSE IF expected return > 0
→ 🟡 WAIT / HOLD

ELSE
→ 🔴 NOT GOOD TO INVEST

---
## 📁 Project Structure

stock_prediction/
│
├── app.py # Streamlit frontend
├── model_utils.py # ML model & prediction logic
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---
## ⚙️ Installation & Setup

### 1️. Clone the Repository
```bash
git clone https://github.com/your-username/stock-market-prediction.git
cd stock-market-prediction

### 2. Install Dependencies
bash
pip install -r requirements.txt

### 3. Run the Application
bash
streamlit run app.py

### 4.Open in browser:
http://localhost:8501

📌 Requirements
Python 3.9+
Internet connection
At least 2 years of historical stock data recommended for best results

⚠️ Disclaimer
This project is for educational purposes only and not financial advice.
Stock market investments involve risk.


### Author
Preethi
Machine Learning & Data Science Enthusiast



