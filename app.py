from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():

    symbols = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "ADAUSDT"
    ]

    prices = []

    for symbol in symbols:

        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        response = requests.get(url)
        data = response.json()

        prices.append({
            "symbol": symbol,
            "price": data["lastPrice"],
            "change": float(data["priceChangePercent"])
        })

    return render_template("index.html", prices=prices)

if __name__ == "__main__":
    app.run(debug=True)
