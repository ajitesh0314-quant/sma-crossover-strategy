# IMPORTS
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# DATA
data = yf.download("ITBEES.NS", start="2020-01-01", end="2025-01-01")


# MOVING AVERAGES
data["SMA_20"] = data["Close"].rolling(20).mean()
data["SMA_50"] = data["Close"].rolling(50).mean()

# SIGNALS
data["Signal"] = 0
data.loc[data["SMA_20"] > data["SMA_50"], "Signal"] = 1
data = data[data["SMA_50"].notna()]

# RETURNS
data["Market_Returns"] = data["Close"].pct_change()
data["Strategy_Returns"] = data["Market_Returns"] * data["Signal"].shift(1)
data = data.dropna()

# PERFORMANCE
data["Cumulative_Strategy"] = (1 + data["Strategy_Returns"]).cumprod()
data["Cumulative_Market"] = (1 + data["Market_Returns"]).cumprod()

# SHARPE RATIO
sharpe = (data["Strategy_Returns"].mean() / data["Strategy_Returns"].std()) * (252 ** 0.5)

# MAX DRAWDOWN
cum_max = data["Cumulative_Strategy"].cummax()
drawdown = data["Cumulative_Strategy"] / cum_max - 1
max_drawdown = drawdown.min()

print("Sharpe Ratio:", sharpe)
print("Max Drawdown:", max_drawdown)

# PRICE PLOT
plt.figure()
plt.plot(data["Close"], label="Price")
plt.plot(data["SMA_20"], label="SMA 20")
plt.plot(data["SMA_50"], label="SMA 50")
plt.legend()
plt.title("Price with SMA Crossover")
plt.show()

# PERFORMANCE PLOT
plt.figure()
plt.plot(data["Cumulative_Strategy"], label="Strategy")
plt.plot(data["Cumulative_Market"], label="Market")
plt.legend()
plt.title("Strategy vs Market Returns")
plt.show()