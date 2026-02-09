import os
import asyncio
from dotenv import load_dotenv
from ib_insync import IB, Stock, util


# Load secrets from .env file
load_dotenv()

async def main():
    ib = IB()

    # Configuration from .env file
    host = os.getenv('IBKR_IP', '127.0.0.1')
    port = int(os.getenv('IBKR_PORT', 7497))
    client_id = int(os.getenv('IBKR_CLIENT_ID', 1))

    print(f"Attempting to connect to {host}:{port}...")

    try:
        # Connect
        await ib.connectAsync(host, port, clientId=client_id)

        # Grab account ID to confirm connection
        account_id = ib.managedAccounts()[0]
        print(f"Success! Connected to account: {account_id}")

    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        ib.disconnect()
        print("Disconnected.")

if __name__ == "__main__":
    asyncio.run(main())
