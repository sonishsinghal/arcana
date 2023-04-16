name=""
import yfinance as yf
def information(name):
    
    tickerSymbol = name
    company = yf.Ticker(tickerSymbol)
    name = company.info['longName']
    print('Company name:', name)
    industry = company.info['industry']
    print('Industry:', industry)
    sector = company.info['sector']
    print('Sector:', sector)
    summary = company.info['longBusinessSummary']
    print('Summary:', summary)

