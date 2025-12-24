import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
import uuid

# ------------------ TICKERS ------------------

NSE_TICKERS = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Reliance": "RELIANCE.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS"
}

US_TICKERS = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Google (Alphabet)": "GOOGL",
    "Tesla": "TSLA",
    "Meta": "META"
}

# ------------------ MAIN LOGIC ------------------

def analyze_risk(stocks):
    # Download data
    data = yf.download(
        stocks,
        start="2023-01-01",
        end="2025-01-01",
        group_by="ticker",
        auto_adjust=True
    )

    # Adjusted close prices
    adj_close = pd.DataFrame()
    for stock in stocks:
        adj_close[stock] = data[stock]["Close"]

    # Daily returns
    returns = adj_close.pct_change().dropna()

    # Risk metrics
    mean_returns = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)

    risk_free_rate = 0.03
    sharpe = (mean_returns - risk_free_rate) / volatility

    # Risk DataFrame
    risk_data = pd.DataFrame({
        "Return": mean_returns,
        "Volatility": volatility,
        "Sharpe": sharpe
    })

    # KMeans clustering
    kmeans = KMeans(n_clusters=min(3, len(risk_data)), random_state=42)
    risk_data["Cluster"] = kmeans.fit_predict(
        risk_data[["Return", "Volatility"]]
    )

    cluster_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    risk_data["Risk_Level"] = risk_data["Cluster"].map(cluster_map)

    # Generate chart
    chart_name = generate_risk_chart(risk_data)

    return risk_data.reset_index().to_dict(orient="records"), chart_name


# ------------------ CHART ------------------

def generate_risk_chart(df):
    filename = f"risk_chart_{uuid.uuid4().hex}.png"

    plot_dir = os.path.join("static", "plots")
    os.makedirs(plot_dir, exist_ok=True)  # 🔥 FIX

    file_path = os.path.join(plot_dir, filename)

    plt.figure(figsize=(8, 6))
    plt.scatter(df["Volatility"], df["Return"], s=100)

    for stock in df.index:
        plt.text(
            df.loc[stock, "Volatility"] + 0.002,
            df.loc[stock, "Return"],
            stock
        )

    plt.xlabel("Annualized Volatility")
    plt.ylabel("Annualized Return")
    plt.title("Risk vs Return Analysis")
    plt.grid(True)

    plt.savefig(file_path)
    plt.close()

    return filename
