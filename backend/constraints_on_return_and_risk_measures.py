
import numpy as np
import pandas as pd
import yfinance as yf
import warnings
def_assets = ['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 'JPM',
              'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'TMO',
              'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']


def constraints_on_return_and_risk_measures(start='2016-01-01', end='2019-12-30', assets=def_assets):
    import matplotlib.pyplot as plt
    start = start
    end = end

    # Tickers of assets
    assets = def_assets
    assets.sort()


# Downloading data
    data = yf.download(assets, start=start, end=end)
    data = data.loc[:, ('Adj Close', slice(None))]
    data.columns = assets

    Y = data[assets].pct_change().dropna()

    import riskfolio as rp

    # Building the portfolio object
    port = rp.Portfolio(returns=Y)

    # Calculating optimal portfolio

    # Select method and estimate input parameters:

    # Method to estimate expected returns based on historical data.
    method_mu = 'hist'
    # Method to estimate covariance matrix based on historical data.
    method_cov = 'hist'

    port.assets_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

    # Estimate optimal portfolio:

    # Could be Classic (historical), BL (Black Litterman) or FM (Factor Model)
    model = 'Classic'
    rm = 'MV'  # Risk measure used, this time will be variance
    obj = 'Sharpe'  # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
    hist = True  # Use historical scenarios for risk measures that depend on scenarios
    rf = 0  # Risk free rate
    l = 0  # Risk aversion factor, only useful when obj is 'Utility'

    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

    plt.figure(figsize=(10, 8))
    ax = rp.plot_pie(w=w, title='Sharpe Mean Variance', others=0.05, nrow=25, cmap="tab20",
                     height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot1.jpg")
    points = 50  # Number of points of the frontier

    frontier = port.efficient_frontier(
        model=model, rm=rm, points=points, rf=rf, hist=hist)

    # Plotting the efficient frontier in Std. Dev. dimension

    label = 'Max Risk Adjusted Return Portfolio'  # Title of point
    mu = port.mu  # Expected returns
    cov = port.cov  # Covariance matrix
    returns = port.returns  # Returns of the assets

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot2.jpg")
    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm='CVaR',
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot3.jpg")
    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm='MDD',
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot4.jpg")

    risk = ['MV', 'CVaR', 'MDD']
    label = ['Std. Dev.', 'CVaR', 'Max Drawdown']
    alpha = 0.05

    for i in range(3):
        limits = port.frontier_limits(
            model=model, rm=risk[i], rf=rf, hist=hist)
        risk_min = rp.Sharpe_Risk(
            limits['w_min'], cov=cov, returns=returns, rm=risk[i], rf=rf, alpha=alpha)
        risk_max = rp.Sharpe_Risk(
            limits['w_max'], cov=cov, returns=returns, rm=risk[i], rf=rf, alpha=alpha)

        if 'Drawdown' in label[i]:
            factor = 1
        else:
            factor = 252**0.5

    rm = 'MV'  # Risk measure

    # Constraint on minimum Return
    port.lowerret = 0.16/252  # We transform annual return to daily return

    # Constraint on maximum CVaR
    port.upperCVaR = 0.26/252**0.5  # We transform annual CVaR to daily CVaR

    # Constraint on maximum Max Drawdown
    port.uppermdd = 0.131  # We don't need to transform drawdowns risk measures

    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

    plt.figure(figsize=(10, 8))
    ax = rp.plot_pie(w=w, title='Sharpe Mean CVaR', others=0.05, nrow=25, cmap="tab20",
                     height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot5.jpg")

    points = 50  # Number of points of the frontier

    frontier = port.efficient_frontier(
        model=model, rm=rm, points=points, rf=rf, hist=hist)

    label = 'Max Risk Adjusted Return Portfolio'  # Title of point
    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot6.jpg")

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm='CVaR',
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot7.jpg")
    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm='MDD',
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images6/plot8.jpg")
