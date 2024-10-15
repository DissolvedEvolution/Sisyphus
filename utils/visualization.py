import matplotlib.pyplot as plt
import seaborn as sns

def plot_equity_curve(equity_curve):
    plt.figure(figsize=(12, 6))
    plt.plot(equity_curve)
    plt.title('Equity Curve')
    plt.xlabel('Time')
    plt.ylabel('Equity')
    plt.show()

def plot_returns_distribution(returns):
    plt.figure(figsize=(12, 6))
    sns.histplot(returns, kde=True)
    plt.title('Returns Distribution')
    plt.xlabel('Returns')
    plt.ylabel('Frequency')
    plt.show()

# Add more visualization functions as needed
