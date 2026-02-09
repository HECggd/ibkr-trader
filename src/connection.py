import os
from dotenv import load_dotenv
from ib_insync import IB

load_dotenv()

def get_ib(client_id=1):
    """Connection logic for repo."""
    ib = IB()
    host = os.getenv('IBKR_IP', '127.0.0.1')
    port = int(os.getenv('IBKR_PORT', 7497))

    try:
        ib.connect(host, port, clientId=client_id)
        ib.reqMarketDataType(3)  # Delayed data for paper trading
        return ib
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None
    