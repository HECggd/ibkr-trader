# ibkr-trader
Practice repository for algorithmic trading with Interactive Brokers API, focusing on clean architecture and modern Python tooling.

# IBKR Trader

A modern Python framework for interacting with the Interactive Brokers (IBKR) API. This project focuses on clean code, asynchronous execution, and reproducible environment management.

## 🛠 Tech Stack
- **Language:** Python 3.12+
- **API Wrapper:** [ib_insync](https://github.com/erdewit/ib_insync) (Asynchronous)
- **Data Handling:** Pandas
- **Environment Management:** [uv](https://github.com/astral-sh/uv)
- **Secrets:** python-dotenv

## 🚀 Getting Started

### Prerequisites
- Interactive Brokers **TWS** or **IB Gateway** installed and running.
- API enabled in IBKR settings (Port 7497 for Paper, 7496 for Live).
- [uv](https://docs.astral.sh/uv/) installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ibkr-trader.git](https://github.com/YOUR_USERNAME/ibkr-trader.git)
   cd ibkr-trader
