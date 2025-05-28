import os, re, threading, webbrowser, random
from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from web3 import Web3, HTTPProvider

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

# ---------- CONFIG ----------
ETH_RPC = os.getenv("ETH_RPC") or "https://eth-mainnet.g.alchemy.com/v2/QmErVMyRN-deHWdCKDpT8dlW4jFh0H5C"
ADDR_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
web3 = Web3(HTTPProvider(ETH_RPC, request_kwargs={"timeout": 15}))
if not web3.is_connected():
    raise RuntimeError("Ethereum RPC not reachable")
# ----------------------------

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# ---------- DATA ----------
wallet_db: dict[str, dict] = {}   # address -> {"balance": float, "tx": int, ...}
kmeans: KMeans | None = None

# ---------- HELPERS ----------
def heuristic_bio(balance, tx):
    if balance > 10 and tx > 100:
        return "High-volume whale active across DeFi & NFTs."
    if tx > 100:
        return "DeFi power-user with frequent trades."
    if balance > 5:
        return "Long-term holder with solid stack."
    if tx < 5:
        return "New or dormant wallet."
    return "Casual user exploring the ecosystem."

def recommend(cluster: int | None):
    if cluster == 0:   # light
        return ["OpenSea", "Rainbow", "Lens Protocol"]
    if cluster == 1:   # mid
        return ["Uniswap", "Zapper", "Mirror"]
    if cluster == 2:   # heavy
        return ["Aave", "Blur", "dYdX"]
    return ["Uniswap", "OpenSea"]

def estimate_first_seen(tx):
    if tx == 0:
        return "Unknown"
    days_ago = random.randint(30, 720)
    return (datetime.utcnow() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

def update_clusters():
    global kmeans
    if len(wallet_db) < 3:
        return
    X = np.array([[w["balance"], w["tx"]] for w in wallet_db.values()])
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
    labels = kmeans.fit_predict(X)
    for addr, lbl in zip(wallet_db, labels):
        wallet_db[addr]["cluster"] = int(lbl)

def get_vector(addr: str) -> np.ndarray:
    """Return the 2-dim vector [balance, tx] for an address (zeros if missing)."""
    w = wallet_db.get(addr)
    if not w:
        return np.zeros(2)
    return np.array([w["balance"], w["tx"]])

# ---------- MODELS ----------
class WalletReq(BaseModel):
    address: str
class SimReq(BaseModel):
    address1: str
    address2: str

# ---------- ROUTES ----------
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/persona")
async def persona(req: WalletReq):
    raw = req.address.strip()
    if not ADDR_RE.fullmatch(raw):
        raise HTTPException(400, "Invalid address")

    try:
        addr   = Web3.to_checksum_address(raw)
        balWei = web3.eth.get_balance(addr)
        txCnt  = web3.eth.get_transaction_count(addr)
        balEth = balWei / 1e18

        # store / update
        wallet_db[addr] = {"balance": balEth, "tx": txCnt}
        update_clusters()
        cl = wallet_db[addr].get("cluster")

        return {
            "address": addr,
            "balance": f"{balEth:.4f}",
            "txCount": txCnt,
            "firstSeen": estimate_first_seen(txCnt),
            "gasUsed": txCnt * random.randint(40_000, 80_000),
            "cluster": cl,
            "persona": heuristic_bio(balEth, txCnt),
            "recommendations": recommend(cl)
        }

    except Exception as e:
        raise HTTPException(502, f"RPC error: {e}")

@app.post("/similarity")
async def similarity(req: SimReq):
    a1, a2 = req.address1.strip(), req.address2.strip()
    if not (ADDR_RE.fullmatch(a1) and ADDR_RE.fullmatch(a2)):
        raise HTTPException(400, "Invalid address")

    # identical addresses => perfect similarity
    if a1.lower() == a2.lower():
        return {"similarity": 1.0}

    # ensure both wallets analyzed at least once
    for a in (a1, a2):
        if a not in wallet_db:
            await persona(WalletReq(address=a))

    v1, v2 = get_vector(a1), get_vector(a2)

    # both zero vectors => treat as identical (similarity 1)
    if np.all(v1 == 0) and np.all(v2 == 0):
        sim = 1.0
    else:
        sim = float(cosine_similarity([v1], [v2])[0][0])

    return {"similarity": sim}

# ---------- AUTO-LAUNCH ----------
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000")
if __name__ == "__main__":
    threading.Timer(1.2, open_browser).start()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
