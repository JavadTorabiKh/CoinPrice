# 🌍 Crypto Token Info API 🚀

A fast and simple API to retrieve token information, metadata, global prices, and market data for cryptocurrencies! 📊  

## ✨ Features

✅ Get detailed token information  
✅ Real-time global prices  
✅ Complete token metadata  
✅ Fast, lightweight, and scalable  

---

## 🚀 How to Use

### 1️⃣ Install Dependencies
Ensure you have Python and `pip` installed, then run:

```bash
pip install -r requirements.txt
```


### 2️⃣ Run the API
To start the API, simply run:

```bash
python app.py
```
By default, the API will be available at http://127.0.0.1:5000.

## 🔗 Example Requests

### 📌 Get Token Information

```bash
GET /api/token/{symbol}
```
Example:

```bash
GET /api/token/BTC
```
### 📤 Response:

```json
{
    "symbol": "BTC",
    "name": "Bitcoin",
    "price_usd": 45000.23,
    "market_cap": 850000000000,
    "volume_24h": 32000000000
}
```

## 🌎 Get Global Market Data