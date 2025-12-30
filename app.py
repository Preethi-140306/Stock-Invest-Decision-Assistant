import streamlit as st
from model_utils import train_predict_decide

st.set_page_config(page_title="Investment Advisor", layout="centered")

st.title("📊 Stock Investment Decision Assistant")

ticker = st.text_input("Stock Ticker (AAPL, TSLA, INFY, RELIANCE.NS)", "AAPL")
start = st.date_input("Start Date")
end = st.date_input("End Date")

if st.button("Analyze Investment"):
    with st.spinner("Analyzing stock..."):
        result = train_predict_decide(ticker, start, end)

    
    if result is None:
        st.error("Not enough data to analyze this stock.")
    else:
        st.metric("Current Price", f"${result['current_price']:.2f}")
        st.metric("Predicted Price", f"${result['predicted_price']:.2f}")
        st.metric("Expected Return", f"{result['expected_return']:.2f}%")
        st.write("📈 Trend:", result["ma_trend"])
        st.write("📊 RSI:", round(result["rsi"], 2))
        st.subheader(result["decision"])
