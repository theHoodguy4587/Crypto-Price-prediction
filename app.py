import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib
import requests
import matplotlib.pyplot as plt





st.title("📈 Bitcoin Price Predictor(LSTM Model)")
st.write("This app predicts Bitcoin's price using an LSTM model trained on the last 90 days.")

model=load_model("bitcoin_lstm_model.keras")
scaler=joblib.load("scaler.pkl")



st.subheader("🔄 Fetching Latest Bitcoin Price Data...")
url="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params={"vs_currency":"usd","days":120}

response=requests.get(url,params=params).json()
prices=response["prices"]

df=pd.DataFrame(prices,columns=["timestamp","price"])
df["date"]=pd.to_datetime(df["timestamp"],unit="ms")
df.set_index("date",inplace=True)
df=df[["price"]]

st.line_chart(df["price"],use_container_width=True)

st.subheader("📊 Preparing Data...")

scaled_data=scaler.transform(df)
sequence_length=60

X_test=[]
for i in range(sequence_length,len(scaled_data)):
    X_test.append(scaled_data[i-sequence_length:i,0])

X_test=np.array(X_test)
X_test=X_test.reshape((X_test.shape[0],X_test.shape[1],1))


st.subheader("🤖 Predicting...")

predictions_scaled=model.predict(X_test)
predictions=scaler.inverse_transform(predictions_scaled)

actual_prices=df.iloc[len(df)-len(predictions):]["price"].values

st.subheader("📉 Actual vs Predicted")

fig,ax=plt.subplots(figsize=(12,6))
ax.plot(actual_prices,label="Actual Price")
ax.plot(predictions,label="Predicted Price")
ax.legend()
st.pyplot(fig)

st.subheader("🔮 Predict Next Day Bitcoin Price")

last_60=scaled_data[-60:].reshape(1,60,1)
next_day_scaled=model.predict(last_60)
next_day_price=scaler.inverse_transform(next_day_scaled)[0][0]

st.success(f"📌 **Next Day Predicted Price:** ${next_day_price:,.2f}")








