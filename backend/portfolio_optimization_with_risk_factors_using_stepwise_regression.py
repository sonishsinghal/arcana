

import numpy as np
import pandas as pd
import yfinance as yf
import warnings

def_assets = ['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 'JPM',
              'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'TMO',
              'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']


def portfolio_optimisation_with_risk_factors(start='2016-01-01', end='2019-12-30', assets=def_assets):

    import matplotlib.pyplot as plt
    start = start
    end = end

    # Tickers of assets
    assets = def_assets
    assets.sort()


# Tickers of factors

    factors = ['MTUM', 'QUAL', 'VLUE', 'SIZE', 'USMV']
    factors.sort()

    tickers = assets + factors
    tickers.sort()

    # Downloading data
    data = yf.download(tickers, start=start, end=end)
    data = data.loc[:, ('Adj Close', slice(None))]
    data.columns = tickers

    X = data[factors].pct_change().dropna()
    Y = data[assets].pct_change().dropna()

    import riskfolio as rp

    step = 'Forward'  # Could be Forward or Backward stepwise regression
    loadings = rp.loadings_matrix(X=X, Y=Y, stepwise=step)

    loadings.style.format("{:.4f}").background_gradient(cmap='RdYlGn')

    port = rp.Portfolio(returns=Y)

    # Calculating optimal portfolio

    # Select method and estimate input parameters:

    # Method to estimate expected returns based on historical data.
    method_mu = 'hist'
    # Method to estimate covariance matrix based on historical data.
    method_cov = 'hist'

    port.assets_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

    port.factors = X
    port.factors_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

    # Estimate optimal portfolio:

    port.alpha = 0.05
    model = 'FM'  # Factor Model
    rm = 'MV'  # Risk measure used, this time will be variance
    obj = 'Sharpe'  # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
    hist = False  # Use historical scenarios for risk measures that depend on scenarios
    rf = 0  # Risk free rate
    l = 0  # Risk aversion factor, only useful when obj is 'Utility'

    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

    plt.figure(figsize=(10, 8))
    x = rp.plot_pie(w=w, title='Sharpe FM Mean Variance', others=0.05, nrow=25, cmap="tab20",
                    height=6, width=10, ax=None)
    plt.savefig(f"/images4/plot1.jpg")

    points = 50  # Number of points of the frontier

    frontier = port.efficient_frontier(
        model=model, rm=rm, points=points, rf=rf, hist=hist)

    label = 'Max Risk Adjusted Return Portfolio'  # Title of point
    mu = port.mu_fm  # Expected returns
    cov = port.cov_fm  # Covariance matrix
    returns = port.returns_fm  # Returns of the assets

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"/images4/plot2.jpg")

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier_area(
        w_frontier=frontier, cmap="tab20", height=6, width=10, ax=None)
    plt.savefig(f"/images4/plot3.jpg")
