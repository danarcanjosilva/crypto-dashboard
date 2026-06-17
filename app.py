import requests
from flask import Flask, render_template

app = Flask(__name__)

SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT"]

@app.route("/")
def index():
    prices = []

    for symbol in SYMBOLS:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        data = requests.get(url).json()

        prices.append({
            "symbol": symbol,
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"])
        })

    return render_template("index.html", prices=prices)

if __name__ == "__main__":
    app.run(debug=True)
