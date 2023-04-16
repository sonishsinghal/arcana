
import numpy as np
import pandas as pd
import yfinance as yf
import warnings



import numpy as np
import pandas as pd
import yfinance as yf
import warnings

def_assets=['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 'JPM',
                'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'TMO',
                'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']
def risk_parity_portfolio_optimization(start='2016-01-01',end='2019-12-30',assets=def_assets):

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

    port = rp.Portfolio(returns=Y)

    # Calculating optimal portfolio

    # Select method and estimate input parameters:

    method_mu='hist' # Method to estimate expected returns based on historical data.
    method_cov='hist' # Method to estimate covariance matrix based on historical data.

    port.assets_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

    # Estimate optimal portfolio:

    model='Classic' # Could be Classic (historical), BL (Black Litterman) or FM (Factor Model)
    rm = 'MV' # Risk measure used, this time will be variance
    obj = 'Sharpe' # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
    hist = True # Use historical scenarios for risk measures that depend on scenarios
    rf = 0 # Risk free rate
    l = 0 # Risk aversion factor, only useful when obj is 'Utility'

    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

    # Plotting the composition of the portfolio
    plt.figure(figsize=(10,8))
    ax = rp.plot_pie(w=w, title='Sharpe Mean Variance', others=0.05, nrow=25, cmap = "tab20",
                    height=6, width=10, ax=None)
    plt.savefig(f"./images5/plot1.jpg")

    # Plotting the risk composition of the portfolio
    plt.figure(figsize=(10,8))
    ax = rp.plot_risk_con(w, cov=port.cov, returns=port.returns, rm=rm, rf=0, alpha=0.01,
                        color="tab:blue", height=6, width=10, ax=None)
    plt.savefig(f"./images5/plot2.jpg")

    b = None # Risk contribution constraints vector

    w_rp = port.rp_optimization(model=model, rm=rm, rf=rf, b=b, hist=hist)

    plt.figure(figsize=(10,8))
    ax = rp.plot_risk_con(w_rp, cov=port.cov, returns=port.returns, rm=rm, rf=0, alpha=0.01,
                        color="tab:blue", height=6, width=10, ax=None)
    plt.savefig(f"./images5/plot3.jpg")
    

    # Risk Measures available:
    #
    # 'MV': Standard Deviation.
    # 'MAD': Mean Absolute Deviation.
    # 'MSV': Semi Standard Deviation.
    # 'FLPM': First Lower Partial Moment (Omega Ratio).
    # 'SLPM': Second Lower Partial Moment (Sortino Ratio).
    # 'CVaR': Conditional Value at Risk.
    # 'EVaR': Entropic Value at Risk.
    # 'CDaR': Conditional Drawdown at Risk of uncompounded cumulative returns.
    # 'EDaR': Entropic Drawdown at Risk of uncompounded cumulative returns.
    # 'UCI': Ulcer Index of uncompounded cumulative returns.

    rms = ['MV', 'MAD', 'MSV', 'FLPM', 'SLPM', 'CVaR',
        'EVaR', 'CDaR', 'UCI', 'EDaR']

    w_s = pd.DataFrame([])
    port.solvers = ['MOSEK']

    for i in rms:
        w = port.rp_optimization(model=model, rm=i, rf=rf, b=b, hist=hist)
        w_s = pd.concat([w_s, w], axis=1)
        
    # w_s.columns = rms

    # w_s.style.format("{:.2%}").background_gradient(cmap='YlGn')

    # import matplotlib.pyplot as plt

    # # Plotting a comparison of assets weights for each portfolio
    # plt.figure(figsize=(10,8))
    # fig = plt.gcf()
    # fig.set_figwidth(16)
    # fig.set_figheight(6)
    # ax = fig.subplots(nrows=1, ncols=1)
    # plt.savefig(f"./backend/images5/plot4.jpg")

    # w_s.plot.bar(ax=ax)

