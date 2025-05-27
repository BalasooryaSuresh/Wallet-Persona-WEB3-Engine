# Wallet Persona Engine

An Ethereum wallet persona explorer that uses AI to analyze a wallet's on-chain behavior and visualize key metrics. It offers:

* Persona summaries based on transaction patterns.
* KMeans clustering of wallet behaviors.
* Wallet-to-wallet similarity via vector embeddings.
* Charts of balance vs transaction activity.
* Dark mode UI.
* Recommendations for dApps and NFTs.

---

## 🔧 Features

* **Address Input**: Enter any Ethereum address for analysis.
* **Persona Summary**: AI-generated summary based on balance, gas usage, tx count, etc.
* **Cluster Detection**: Groups wallet behavior using KMeans clustering.
* **Similarity Check**: Compare two wallet addresses with cosine similarity.
* **Chart.js Visuals**: Display tx count and balance bar charts.
* **dApp/NFT Recommendations**: Suggested based on clustering.
* **Dark Mode**: Toggle between light/dark themes.

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/wallet-persona-engine.git
cd wallet-persona-engine
```

### 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the app

```bash
python main.py
```

This will auto-open your browser to `http://localhost:8000`.

---

## 🧠 How It Works

1. **main.py** uses FastAPI to expose:

   * `/persona`: Accepts a wallet address and returns persona data + recommendations.
   * `/similarity`: Accepts two wallet addresses and returns cosine similarity.

2. **index.html** is a responsive UI that lets users:

   * Analyze a wallet
   * See visual metrics
   * Get dApp/NFT recommendations
   * Compare wallet similarity

3. **Clustering & Similarity**:

   * Feature vector: balance, tx count, gas used.
   * KMeans (k=4) to group wallets.
   * Cosine similarity between feature vectors.

---

## 📁 Files

* `main.py` - FastAPI backend with clustering and AI logic.
* `index.html` - Tailwind-based frontend UI with Chart.js and dark mode toggle.
* `requirements.txt` - Python dependencies.
* `README.md` - This file.

---

## 📦 Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* scikit-learn
* numpy
* webbrowser

---

## 💡 Notes

* No actual web3 or blockchain call — the app uses placeholder logic. Integrate Etherscan API or Alchemy for real on-chain data.
* Models and embeddings are local/simulated. For production, consider vector databases and actual ML inference pipelines.

---

## 📜 License

None

---

## 🙋‍♂️ Acknowledgements

* Tailwind CSS for rapid styling
* Chart.js for data visualizations
* scikit-learn for clustering

Enjoy exploring wallet personas!
