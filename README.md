# arcana

## Problem Statment

**Objective**: 

Develop a web application that leverages transcripts, financial fundamental data provided by Arcana here and any publicly available internet data such as social media, news and  to provide insights about market trends & sentiment about stocks. This application will be used by an Investor and it should help in any one or more of the investor job functions such as capital allocation, research & analysis, portfolio management, staying informed & performance monitoring etc., 

**Link to datasets: 
      Transcripts:** [https://storage.googleapis.com/hackmadras/fmp-transcripts.zip](https://storage.googleapis.com/hackmadras/fmp-transcripts.zip)
      Prices: [https://storage.googleapis.com/hackmadras/prices.zip](https://storage.googleapis.com/hackmadras/prices.zip)

**Evaluation criteria**

1. **Analytics:** Functionality of the data science model 
2. **Web:** Complexity of the application/visualizations
3. **Overall:** How both components come together to make a useful product. 

**Submission Rule:** 

1. Host it and send the link or push it to github with setup instructions. 
2. Judges should be able to set it up <2 min and play with the application.

We generated various plots using closing prices and volume.
The RSI plots were generated for the given closing prices and threshold of 70 and 30 are used.
50 day and 20 day Moving averages were plotted and in the intersection points buy and sell positions were indicated in the graph.
Additionally, Boullinger bands were plotted for bounding the price flow. 
AI models were tried and trained on the previous 32 days of the data and tried to fit on the data.


**Portfolio optimisation:**
For a given level of risk, we want to make sure that we are getting as much return as possible. In quantitative finance, risk is viewed like a resource. Exposing your portfolio to risk generates returns over time. In other words, expected return is the compensation that we get paid in return for taking on uncertainty.
The risk and uncertainty around an investment’s return is traditionally proxied by the standard deviation of its historical returns.
There is an approximate and positive relationship between risk and return. The more volatile an asset is, the higher its historical returns have usually been.

**Efficient frontier:**
An efficient frontier is a set of investment portfolios that are expected to provide the highest returns at a given level of risk. A portfolio is said to be efficient if there is no other portfolio that offers higher returns for a lower or equal amount of risk. Where portfolios are located on the efficient frontier depends on the investor’s degree of risk tolerance.

We tried optimising Portfolio using historical data, different models , different risk measures.
The model Could be Classic (historical), BL (Black Litterman) or FM (Factor Model).
The Objective function, could be MinRisk, MaxRet, Utility or Sharpe.
The risk aversion factor is not used here since the objective function is not utility.

We made sentiment analysis for the transcripts available and also used LSTM based architecture for forecasting
