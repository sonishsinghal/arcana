# -*- coding: utf-8 -*-
"""Portfolio_optimisation_2_Ulcer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g5RNwDXmvaPt3aBKcUNioqnbAzL8hVVD
"""




import numpy as np
import pandas as pd
import yfinance as yf
import warnings
import matplotlib.pyplot as plt 

def_assets=['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 'JPM',
                'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'TMO',
                'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']
def portfolio_optimisation_2_ulcer(start='2016-01-01',end='2019-12-30',assets=def_assets):

    import matplotlib.pyplot as plt
    start = start
    end =end

    # Tickers of assets
    assets = def_assets
    assets.sort()

    # Downloading data
    data = yf.download(assets, start = start, end = end)
    data = data.loc[:,('Adj Close', slice(None))]
    data.columns = assets

    Y = data[assets].pct_change().dropna()

  
    import riskfolio as rp

    # Building the portfolio object
    port = rp.Portfolio(returns=Y)

    # Calculating optimal portfolio

    # Select method and estimate input parameters:

    method_mu='hist' # Method to estimate expected returns based on historical data.
    method_cov='hist' # Method to estimate covariance matrix based on historical data.

    port.assets_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

    # Estimate optimal portfolio:

    model='Classic' # Could be Classic (historical), BL (Black Litterman) or FM (Factor Model)
    rm = 'UCI' # Risk measure used, this time will be variance
    obj = 'Sharpe' # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
    hist = True # Use historical scenarios for risk measures that depend on scenarios
    rf = 0 # Risk free rate
    l = 0 # Risk aversion factor, only useful when obj is 'Utility'

    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

  
    plt.figure(figsize=(10,8))
    ax = rp.plot_pie(w=w, title='Sharpe Mean Ulcer Index', others=0.05, nrow=25, cmap = "tab20",
                    height=6, width=10, ax=None)
    plt.savefig(f"./images3/plot1.jpg")

    points = 40 # Number of points of the frontier

    frontier = port.efficient_frontier(model=model, rm=rm, points=points, rf=rf, hist=hist)

    

    label = 'Max Risk Adjusted Return Portfolio' # Title of point
    mu = port.mu # Expected returns
    cov = port.cov # Covariance matrix
    returns = port.returns # Returns of the assets

    plt.figure(figsize=(10,8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                        rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                        marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images3/plot2.jpg")

    plt.figure(figsize=(10,8))
    ax = rp.plot_frontier_area(w_frontier=frontier, cmap="tab20", height=6, width=10, ax=None)
    plt.savefig(f"./images3/plot3.jpg")

    b = None # Risk contribution constraints vector

    w_rp = port.rp_optimization(model=model, rm=rm, rf=rf, b=b, hist=hist)

    plt.figure(figsize=(10,8))
    ax = rp.plot_pie(w=w_rp, title='Risk Parity Ulcer Index', others=0.05, nrow=25, cmap = "tab20",
                    height=6, width=10, ax=None)
    plt.savefig(f"./images3/plot4.jpg")

    plt.figure(figsize=(10,8))
    ax = rp.plot_risk_con(w_rp, cov=port.cov, returns=port.returns, rm=rm, rf=0, alpha=0.01,
                        color="tab:blue", height=6, width=10, ax=None)
    plt.savefig(f"./images3/plot5.jpg")

