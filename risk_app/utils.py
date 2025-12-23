import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.cluster import KMeans

def analyze_risk(stocks):
    data = yf.download(
        stocks,
        start="2023-01-01",
        end="2025-01-01",
        group_by="ticker",
        auto_adjust=True
    )

    adj_close = pd.DataFrame()
    for stock in stocks:
        adj_close[stock] = data[stock]['Close']

    returns = adj_close.pct_change().dropna()

    mean_returns = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)

    risk_free_rate = 0.03
    sharpe = (mean_returns - risk_free_rate) / volatility

    risk_data = pd.DataFrame({
        "Return": mean_returns,
        "Volatility": volatility,
        "Sharpe": sharpe
    })

    kmeans = KMeans(n_clusters=3, random_state=42)
    risk_data["Cluster"] = kmeans.fit_predict(
        risk_data[["Return", "Volatility"]]
    )

    cluster_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    risk_data["Risk_Level"] = risk_data["Cluster"].map(cluster_map)

    return risk_data.reset_index().to_dict(orient="records")
