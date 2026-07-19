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
uvicorn network_api:app --reload
```
By default, the API will be available at http://127.0.0.1:8000.

---

## 🔗 Example Requests

### 📌 Get Token Information

```bash
GET /v1/prodict/{symbol}
```

Example:

```bash
GET /v1/prodict/BTC
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

---


## 🌎 Get Global Market Data

```bash
GET /api/global
```
### 📤 Response:

```json
{
    "total_market_cap": 2200000000000,
    "total_volume_24h": 150000000000,
    "btc_dominance": 47.5
}
```

---

## 🛠️ Configuration

You can modify the port and other settings in the .env file:

```env
PORT=5000
DEBUG=True
API_KEY=your_api_key
```

---

## 📌 Contribute ❤️

If you have ideas to improve this project, feel free to submit a Pull Request or open an Issue.

📧 Contact Us: j.2528840@gmail.com

---

## 📜 License

This project is licensed under the MIT License. 

Feel free to use it! 🚀


