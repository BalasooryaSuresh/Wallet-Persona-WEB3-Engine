# Wallet Persona

Wallet Persona is a FastAPI-based web application that analyzes Ethereum wallet addresses to provide insights into their activity, persona, and recommendations. It uses clustering to categorize wallets and calculates similarity between wallet addresses based on balance and transaction count.

## Features

- **Wallet Analysis**: Enter an Ethereum wallet address to retrieve balance, transaction count, estimated first seen date, gas used, cluster, persona description, and tailored recommendations.
- **Wallet Similarity**: Compare two Ethereum wallet addresses to compute their similarity based on balance and transaction count.
- **Clustering**: Uses KMeans clustering to group wallets into three categories (light, mid, heavy) based on their activity.
- **Responsive Frontend**: A simple HTML interface for inputting wallet addresses and viewing results.

## Requirements

The project dependencies are listed in `requirements.txt`:

- `fastapi`: For building the web API.
- `uvicorn`: ASGI server for running the FastAPI app.
- `web3`: To interact with the Ethereum blockchain via an RPC endpoint.
- `httpx`: For HTTP requests.
- `pydantic`: For data validation and request/response models.
- `numpy`: For numerical computations.
- `sklearn.cluster` and `sklearn.preprocessing`: For KMeans clustering and data processing.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd wallet-persona
   ```

2. **Install Dependencies**: Ensure Python 3.8+ is installed, then create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**: The app uses an Ethereum RPC endpoint. By default, it uses a public Alchemy endpoint, but you can set a custom one:

   ```bash
   export ETH_RPC="https://your-ethereum-rpc-endpoint"
   ```

4. **Directory Structure**: Ensure the `frontend` directory contains `index.html`. The app mounts this directory to serve the frontend.

## Running the Application

1. **Start the Server**: Run the FastAPI application with Uvicorn:

   ```bash
   python main.py
   ```

   The server will start on `http://127.0.0.1:8000`, and a browser window should automatically open to the frontend.

2. **Access the Frontend**:

   - Navigate to `http://127.0.0.1:8000` in your browser.
   - Enter an Ethereum wallet address in the input field and click "Analyze" to view wallet details.
   - To compare two wallets, enter two addresses and click "Compare" to see their similarity score.

## API Endpoints

- **GET /**: Serves the `index.html` frontend.
- **POST /persona**: Analyzes a single wallet address.
  - Request body: `{"address": "0x..."}`
  - Response: JSON with balance, transaction count, first seen date, gas used, cluster, persona, and recommendations.
- **POST /similarity**: Compares two wallet addresses.
  - Request body: `{"address1": "0x...", "address2": "0x..."}`
  - Response: JSON with a similarity score (0.0 to 1.0).

## How It Works

- **Wallet Analysis**: The app queries the Ethereum blockchain via Web3.py to fetch balance and transaction count. It estimates the first seen date based on transaction count and calculates gas used with a randomized estimate.
- **Clustering**: Uses KMeans to cluster wallets into three groups based on balance and transaction count. Clusters are updated dynamically as new wallets are analyzed.
- **Persona**: Assigns a descriptive persona (e.g., "High-volume whale", "DeFi power-user") based on balance and transaction count heuristics.
- **Recommendations**: Suggests dApps (e.g., Uniswap, OpenSea) based on the wallet's cluster.
- **Similarity**: Computes cosine similarity between two wallets' balance and transaction count vectors.

## Notes

- The app uses a public Alchemy RPC endpoint by default. For production, use a dedicated or private RPC endpoint for better performance and reliability.
- The `estimate_first_seen` function uses a random range (30–720 days) for demonstration. In a production environment, you might want to fetch actual first transaction dates.
- The frontend (`index.html`) is minimal and can be enhanced with additional styling or JavaScript for better interactivity.

## License

This project is made for educational purposes so it has no license
