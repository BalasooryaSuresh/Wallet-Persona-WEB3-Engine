# 🧠 Wallet Persona Web App

A full-stack Ethereum wallet intelligence app that generates a persona for any Ethereum address using FastAPI and TailwindCSS. It calculates wallet health, recommends dApps/NFTs, visualizes wallet journeys, and more — all without needing a login.

---

## 🚀 Features

* 🔍 Validate and analyze Ethereum wallet addresses
* 💰 Get wallet balance and transaction count
* 📈 Visualize wallet journey with Chart.js
* 🧠 AI-generated wallet bios (offline heuristic based)
* 💡 Recommend dApps or NFTs based on activity
* ⚡ FastAPI backend with Web3.py
* 🎨 Responsive UI with TailwindCSS

---

## 📦 Installation

```bash
# 1. Clone the repository
$ git clone https://github.com/yourusername/wallet-persona.git
$ cd wallet-persona

# 2. Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run the FastAPI server
$ uvicorn main:app --reload
```

---

## 📁 Project Structure

```
wallet/
├── index.html
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoint

### `POST /persona`

Send an Ethereum wallet address and receive its persona:

#### Request Body

```json
{
  "address": "0xabc123..."
}
```

#### Response

```json
{
  "address": "0xabc123...",
  "balance": "1.2345 ETH",
  "txCount": 42,
  "healthScore": "Moderate",
  "bio": "Active DeFi user with interest in stablecoins.",
  "recommendations": ["Uniswap", "Zapper", "Rarible"]
}
```

---

## 🛠 Built With

* FastAPI 🔥
* Web3.py 🌐
* TailwindCSS 🎨
* Chart.js 📊
* Vanilla JS

---

## 🗺️ Roadmap

* [x] Wallet validation & persona engine
* [x] Basic frontend UI
* [x] Chart.js wallet journey visualization
* [x] Offline AI-generated wallet bios
* [x] Heuristic dApp/NFT recommendations
* [ ] ENS address resolution
* [ ] Dark mode toggle
* [ ] Deploy on Vercel or Render
* [ ] Expand risk scoring model
* [ ] Add wallet clustering insights
* [ ] Introduce user session saving (client-only)

---

## 📄 License

This project is not licensed under the any means jut made for a competition.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. 🍴 Fork the repo
2. 🛠️ Create your feature branch: `git checkout -b feature/my-feature`
3. 📦 Commit your changes: `git commit -am 'Add cool feature'`
4. 🚀 Push to the branch: `git push origin feature/my-feature`
5. 🔁 Open a pull request
