# SMA Crossover Strategy

## Overview
This project implements a simple moving average (SMA) crossover trading strategy using 20-day and 50-day SMAs on ITBEES.NS.

## Strategy Logic
- Buy when 20-day SMA crosses above 50-day SMA
- Stay out of the market otherwise (long-only)
- Signals are shifted to avoid lookahead bias

## Performance Metrics
- Sharpe Ratio: ~0.813
- Max Drawdown: ~-38%

## Key Insights
- Strategy underperforms in sideways markets due to whipsaws
- Long-only approach improves risk-adjusted returns
- Demonstrates importance of avoiding overtrading

## Tools Used
- Python
- Pandas
- yFinance
- Matplotlib
