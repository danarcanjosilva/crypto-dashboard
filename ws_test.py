import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    print("BTC Price:", data['p'])

url = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(url, on_message=on_message)
ws.run_forever()
