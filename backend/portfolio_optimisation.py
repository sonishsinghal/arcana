import numpy as np
import pandas as pd
import yfinance as yf
import warnings
import riskfolio as rp
import matplotlib.pyplot as plt

# Date range
def_assets = ['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 'JPM',
              'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'TMO',
              'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']


def portfolio_optimisation(start='2016-01-01', end='2019-12-30', assets=def_assets):

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
    plt.savefig(f"./images1/plot1.jpg")

    points = 50  # Number of points of the frontier

    frontier = port.efficient_frontier(
        model=model, rm=rm, points=points, rf=rf, hist=hist)

    label = 'Max Risk Adjusted Return Portfolio'  # Title of point
    mu = port.mu  # Expected returns
    cov = port.cov  # Covariance matrix
    returns = port.returns  # Returns of the assets

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images1/plot2.jpg")

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier_area(
        w_frontier=frontier, cmap="tab20", height=6, width=10, ax=None)
    plt.savefig(f"./images1/plot3.jpg")
    rm = 'CVaR'  # Risk measure

    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

    plt.figure(figsize=(10, 8))
    ax = rp.plot_pie(w=w, title='Sharpe Mean CVaR', others=0.05, nrow=25, cmap="tab20",
                     height=6, width=10, ax=None)
    label = 'Max Risk Adjusted Return Portfolio'  # Title of point
    plt.savefig(f"./images1/plot4.jpg")

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                          rf=rf, alpha=0.05, cmap='viridis', w=w, label=label,
                          marker='*', s=16, c='r', height=6, width=10, ax=None)
    plt.savefig(f"./images1/plot5.jpg")

    plt.figure(figsize=(10, 8))
    ax = rp.plot_frontier_area(
        w_frontier=frontier, cmap="tab20", height=6, width=10, ax=None)
    plt.savefig(f"./images1/plot.jpg")
    rms = ['MV', 'MAD', 'MSV', 'FLPM', 'SLPM', 'CVaR']

    w_s = pd.DataFrame([])

    for i in rms:
        w = port.optimization(model=model, rm=i, obj=obj,
                              rf=rf, l=l, hist=hist)
        w_s = pd.concat([w_s, w], axis=1)

    w_s.columns = rms

    w_s.style.format("{:.2%}").background_gradient(cmap='YlGn')
    import matplotlib.pyplot as plt

    # Plotting a comparison of assets weights for each portfolio
    plt.figure(figsize=(10, 8))
    fig = plt.gcf()
    fig.set_figwidth(14)
    fig.set_figheight(6)

    ax = fig.subplots(nrows=1, ncols=1)

    w_s.plot.bar(ax=ax)
    plt.savefig(f"./images1/plot6.jpg")
