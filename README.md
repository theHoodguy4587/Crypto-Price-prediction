# 📈 Crypto Price Prediction using LSTM

This project predicts **Bitcoin (BTC) prices** using a **Long Short-Term Memory (LSTM)** deep learning model.
It fetches real-time Bitcoin price data from the **CoinGecko API**, processes it, and generates future price predictions through an interactive **Streamlit** web application.

---

## 🚀 Live Demo

🔗 **Streamlit App URL**
👉 *https://thehoodguy4587-crypto-price-prediction-app-ytvra1.streamlit.app/*


---

## 📌 Features

* 📊 Fetches live Bitcoin price data using **CoinGecko API**
* 🧠 Uses a **pre-trained LSTM model** for time-series forecasting
* 🔢 Data scaling using **MinMaxScaler**
* 📈 Visualizes **Actual vs Predicted** prices
* 🔮 Predicts **next-day Bitcoin price**
* 🌐 Deployed using **Streamlit Community Cloud**

---

## 🧠 Model Details

* **Model Type:** LSTM (Long Short-Term Memory)
* **Sequence Length:** 60 days
* **Framework:** TensorFlow / Keras
* **Saved Format:** `.keras`
* **Scaler:** Saved using `pickle` (`scaler.pkl`)

📌 The model was trained separately in **Google Colab** and loaded directly in the Streamlit app for inference (**no retraining during deployment**).

---

## 🗂 Project Structure

```
Crypto-Price-Prediction/
│
├── app.py                         # Streamlit web app
├── bitcoin_lstm_model.keras       # Trained LSTM model
├── scaler.pkl                     # Saved MinMaxScaler
├── requirements.txt               # Python dependencies
├── runtime.txt                    # Python runtime version
├── Crypto_Price_Prediction.ipynb  # Training notebook (Colab)
├── LICENSE
└── README.md
```

---

## ⚙️ Installation (Local)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/theHoodguy4587/Crypto-Price-prediction.git
cd Crypto-Price-prediction
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📦 Requirements

Key libraries used:

* `streamlit`
* `tensorflow`
* `numpy`
* `pandas`
* `scikit-learn`
* `matplotlib`
* `requests`

⚠️ **TensorFlow version** is chosen to be compatible with **Python 3.12** for Streamlit Cloud deployment.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to **GitHub**
2. Go to 👉 [https://share.streamlit.io](https://share.streamlit.io)
3. Select your repository
4. Set:

   * **Main file:** `app.py`
   * **Branch:** `main`
5. Click **Deploy** 🚀

---

## 📊 Data Source

* **API:** CoinGecko
* **Endpoint:**

```
https://api.coingecko.com/api/v3/coins/bitcoin/market_chart
```

* **Currency:** USD
* **Time Range:** Last 90 days

---

## 🔮 How Prediction Works

1. Fetch last **90 days** of BTC prices
2. Scale prices using saved **MinMaxScaler**
3. Create **60-day rolling sequences**
4. Predict next price using **LSTM**
5. Inverse transform to original price scale

---

## 🛠 Future Improvements

* 📅 Multi-day forecasting
* 💾 Database storage
* 📉 Technical indicators (RSI, MACD)
* 📊 Candlestick charts
* 🚀 Docker deployment

---

## 👨‍💻 Author

**Senitha Gunathilaka**
🎓 Data Science Student
🔗 GitHub: [theHoodguy4587](https://github.com/theHoodguy4587)

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute.
