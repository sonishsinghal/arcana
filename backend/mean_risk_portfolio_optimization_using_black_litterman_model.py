


import numpy as np
import pandas as pd
import yfinance as yf
import warnings
import matplotlib.pyplot as plt 

def_assets=['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 'JPM',
                'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'TMO',
                'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']
def mean_risk_portfolio_optimization(start='2016-01-01',end='2019-12-30',assets=def_assets):
        import matplotlib.pyplot as plt
        start = start
        end = end

        # Tickers of assets
        assets =def_assets
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

        port.alpha = 0.05
        model='Classic' # Could be Classic (historical), BL (Black Litterman) or FM (Factor Model)
        rm = 'MV' # Risk measure used, this time will be variance
        obj = 'Sharpe' # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
        hist = True # Use historical scenarios for risk measures that depend on scenarios
        rf = 0 # Risk free rate
        l = 0 # Risk aversion factor, only useful when obj is 'Utility'

        w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

        plt.figure(figsize=(10,8))
        ax = rp.plot_pie(w=w, title='Sharpe Mean Variance', others=0.05, nrow=25, cmap = "tab20",
                        height=6, width=10, ax=None)
        plt.savefig(f"./images2/plot1.jpg")

        asset_classes = {'Assets': ['JCI','TGT','CMCSA','CPB','MO','APA','MMC','JPM',
                                    'ZION','PSA','BAX','BMY','LUV','PCAR','TXT','TMO',
                                    'DE','MSFT','HPQ','SEE','VZ','CNP','NI','T','BA'], 
                        'Industry': ['Consumer Discretionary','Consumer Discretionary',
                                    'Consumer Discretionary', 'Consumer Staples',
                                    'Consumer Staples','Energy','Financials',
                                    'Financials','Financials','Financials',
                                    'Health Care','Health Care','Industrials','Industrials',
                                    'Industrials','Health care','Industrials',
                                    'Information Technology','Information Technology',
                                    'Materials','Telecommunications Services','Utilities',
                                    'Utilities','Telecommunications Services','Financials']}

        asset_classes = pd.DataFrame(asset_classes)
        asset_classes = asset_classes.sort_values(by=['Assets'])

        views = {'Disabled': [False, False, False],
                'Type': ['Classes', 'Classes', 'Classes'],
                'Set': ['Industry', 'Industry', 'Industry'],
                'Position': ['Energy', 'Consumer Staples', 'Materials'],
                'Sign': ['>=', '>=', '>='],
                'Weight': [0.08, 0.1, 0.09], # Annual terms 
                'Type Relative': ['Classes', 'Classes', 'Classes'],
                'Relative Set': ['Industry', 'Industry', 'Industry'],
                'Relative': ['Financials', 'Utilities', 'Industrials']}

        views = pd.DataFrame(views)


        P, Q = rp.assets_views(views, asset_classes)


        port.blacklitterman_stats(P, Q/252, rf=rf, w=w, delta=None, eq=True)

        # Estimate optimal portfolio:

        model='BL'# Black Litterman
        rm = 'MV' # Risk measure used, this time will be variance
        obj = 'Sharpe' # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
        hist = False # Use historical scenarios for risk measures that depend on scenarios

        w_bl = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

        plt.figure(figsize=(10,8))
        ax = rp.plot_pie(w=w_bl, title='Sharpe Black Litterman', others=0.05, nrow=25,
                        cmap = "tab20", height=6, width=10, ax=None)
        plt.savefig(f"./images2/plot2.jpg")


        """Frontier"""

        points = 50 # Number of points of the frontier

        frontier = port.efficient_frontier(model=model, rm=rm, points=points, rf=rf, hist=hist)


        # Plotting the efficient frontier

        label = 'Max Risk Adjusted Return Portfolio' # Title of point
        mu = port.mu_bl # Expected returns of Black Litterman model
        cov = port.cov_bl # Covariance matrix of Black Litterman model
        returns = port.returns # Returns of the assets

        plt.figure(figsize=(10,8))
        ax = rp.plot_frontier(w_frontier=frontier, mu=mu, cov=cov, returns=returns, rm=rm,
                            rf=rf, alpha=0.05, cmap='viridis', w=w_bl, label=label,
                            marker='*', s=16, c='r', height=6, width=10, ax=None)
        plt.savefig(f"./images2/plot3.jpg")
        plt.figure(figsize=(10,8))
        ax = rp.plot_frontier_area(w_frontier=frontier, cmap="tab20", height=6, width=10, ax=None)
        plt.savefig(f"./images2/plot4.jpg")

        # Risk Measures available:
        #
        # 'MV': Standard Deviation.
        # 'MAD': Mean Absolute Deviation.
        # 'MSV': Semi Standard Deviation.
        # 'FLPM': First Lower Partial Moment (Omega Ratio).
        # 'SLPM': Second Lower Partial Moment (Sortino Ratio).
        # 'CVaR': Conditional Value at Risk.
        # 'EVaR': Entropic Value at Risk.
        # 'WR': Worst Realization (Minimax)
        # 'MDD': Maximum Drawdown of uncompounded cumulative returns (Calmar Ratio).
        # 'ADD': Average Drawdown of uncompounded cumulative returns.
        # 'CDaR': Conditional Drawdown at Risk of uncompounded cumulative returns.
        # 'EDaR': Entropic Drawdown at Risk of uncompounded cumulative returns.
        # 'UCI': Ulcer Index of uncompounded cumulative returns.

        rms = ['MV', 'MAD', 'MSV', 'FLPM', 'SLPM', 'CVaR',
            'EVaR', 'WR', 'MDD', 'ADD', 'CDaR', 'UCI', 'EDaR']

        w_s = pd.DataFrame([])
        port.alpha = 0.05

        for i in rms:
            if i == 'MV':
                hist = False
            else:
                hist = True
            w = port.optimization(model=model, rm=i, obj=obj, rf=rf, l=l, hist=hist)
            w_s = pd.concat([w_s, w], axis=1)
            
        w_s.columns = rms

        w_s.style.format("{:.2%}").background_gradient(cmap='YlGn')

        import matplotlib.pyplot as plt

        # Plotting a comparison of assets weights for each portfolio
        plt.figure(figsize=(10,8))
        fig = plt.gcf()
        fig.set_figwidth(14)
        fig.set_figheight(6)
        ax = fig.subplots(nrows=1, ncols=1)

        w_s.plot.bar(ax=ax)
        plt.savefig(f"./images2/plot5.jpg")

