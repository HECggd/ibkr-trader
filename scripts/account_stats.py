print("!! DEBUG: Script is starting...")

from src.connection import get_ib

print("!! DEBUG: Imports successful...")

def show_portfolio_stats():
    ib = get_ib(client_id=2)  # Use a different unique client ID for stats
    if not ib:
        print("Could not connect to IBKR.")
        return
    
    print("Connected. Requesting summary...")
    # Request summary of account values
    summary = ib.accountSummary()

    if not summary:
        print("Summary is empty. Waiting 2 seconds...")
        ib.sleep(2)  # Wait a moment for data to arrive
        summary = ib.accountSummary()

    # Filter for key metrics
    stats = {item.tag: item.value for item in summary}

    metrics = [
        'NetLiquidation',      # Total account value
        'TotalCashValue',      # Cash on hand
        'GrossPositionValue',  # Value of all holdings
        'BuyingPower'          # Available margin
    ]

    for m in metrics:
        val = stats.get(m, "N/A")
        print(f"{m:20}: {val}")

    # Show current positions
    print("\n--- Current Positions ---")
    positions = ib.positions()
    if not positions:
        print("No open positions found.")
    else:
        for p in positions:
            print(f"Symbol: {p.contract.symbol:6} | Shares: {p.position:4} | Avg Cost: {p.avgCost}")

    ib.disconnect()

if __name__ == "__main__":
    show_portfolio_stats()
