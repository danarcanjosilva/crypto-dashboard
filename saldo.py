from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_SECRET_KEY")
)

account = client.get_account()

print("\n=== TODOS OS SALDOS ===\n")

for asset in account["balances"]:
    print(
        asset["asset"],
        "Livre:", asset["free"],
        "Bloqueado:", asset["locked"]
    )
