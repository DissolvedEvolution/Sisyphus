import numpy as np

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - risk_free_rate
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

def calculate_max_drawdown(equity_curve):
    return (equity_curve.cummax() - equity_curve).max()

def calculate_win_rate(trades):
    return sum(trade > 0 for trade in trades) / len(trades)

# Add more performance metrics as needed
