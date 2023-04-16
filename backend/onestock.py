import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import warnings
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# from sklearn.preprocessing import MinMaxScaler
# from keras.layers import LSTM, Dense, Dropout

# from sklearn.model_selection import TimeSeriesSplit
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib. dates as mandates
# from sklearn.preprocessing import MinMaxScaler
# from sklearn import linear_model
# from keras.models import Sequential
# from keras.layers import Dense
# import keras.backend as K
# from keras.callbacks import EarlyStopping
# from keras.optimizers import Adam
# from keras.models import load_model
# from keras.layers import LSTM
# from keras.utils.vis_utils import plot_model

warnings.filterwarnings("ignore")
pd.options.display.float_format = '{:.4%}'.format

def get_rsi(close, lookback):
    ret = close.diff()
    up = []
    down = []
    for i in range(len(ret)):
        if ret[i] < 0:
            up.append(0)
            down.append(ret[i])
        else:
            up.append(ret[i])
            down.append(0)
    up_series = pd.Series(up)
    down_series = pd.Series(down).abs()
    up_ewm = up_series.ewm(com = lookback - 1, adjust = False).mean()
    down_ewm = down_series.ewm(com = lookback - 1, adjust = False).mean()
    rs = up_ewm/down_ewm
    rsi = 100 - (100 / (1 + rs))
    rsi_df = pd.DataFrame(rsi).rename(columns = {0:'rsi'}).set_index(close.index)
    rsi_df = rsi_df.dropna()
    return rsi_df[3:]


def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 2 # Calculate top band
    bollinger_down = sma - std * 2 # Calculate bottom band
    return bollinger_up, bollinger_down


def plot_generator(start,end,asset):
    start = start
    end = end

    # Tickers of assets
    assets = [asset]
    assets.sort()

    # Downloading data
    data = yf.download(assets, start = start, end = end)
    data['rsi_14'] = get_rsi(data['Close'], 14)


    plt.figure(figsize=(10,8))
    ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 4, colspan = 1)
    ax2 = plt.subplot2grid((10,1), (5,0), rowspan = 4, colspan = 1)
    ax1.plot(data['Close'], linewidth = 2.5)
    ax1.set_title('CLOSE PRICE')
    ax2.plot(data['rsi_14'], color = 'orange', linewidth = 2.5)
    ax2.axhline(30, linestyle = '--', linewidth = 1.5, color = 'grey')
    ax2.axhline(70, linestyle = '--', linewidth = 1.5, color = 'grey')
    ax2.set_title(' RELATIVE STRENGTH INDEX')
    plt.savefig(f"./backend/images/RELATIVE STRENGTH INDEX.jpg")

    plt.figure(figsize=(10,8))
    plt.plot(data['Close'], linewidth = 2.5)
    plt.title("Close_Price")
    plt.savefig(f"./backend/images/Close_Price.jpg")

    plt.figure(figsize=(10,8))
    plt.plot(data['Open'], linewidth = 2.5)
    plt.title("Open_Price")
    plt.savefig(f"./backend/images/Open_Price.jpg")

    plt.figure(figsize=(10,8))
    
    plt.plot(data['High'], linewidth = 2.5)
    plt.title("High_Price")
    plt.savefig(f"./backend/images/High_Price.jpg")

    plt.figure(figsize=(10,8))
    plt.plot(data['Low'], linewidth = 2.5)
    plt.title("Low_Price")
    plt.savefig(f"./backend/images/Low_Price.jpg")


    data["20_SMA"] = data["Close"].rolling(window = 20, min_periods = 1).mean()
    # create 50 days simple moving average column
    data["50_SMA"] = data["Close"].rolling(window = 50, min_periods = 1).mean()

    data['Signal'] = 0.0
    data['Signal'] = np.where(data['20_SMA'] > data['50_SMA'], 1.0, 0.0)

    data["20_SMA"] = data["Close"].rolling(window = 20, min_periods = 1).mean()
    # create 50 days simple moving average column
    data["50_SMA"] = data["Close"].rolling(window = 50, min_periods = 1).mean()
    data["Position"] = data["Signal"].diff()


    plt.figure(figsize = (15,10))
# plot close price, short-term and long-term moving averages 
    data["Close"].plot(color = "k", label= "Close Price") 
    data["20_SMA"].plot(color = "b",label = "20-day SMA") 
    data["50_SMA"].plot(color = "g", label = "50-day SMA")
    # plot ‘buy’ signals
    plt.plot(data[data["Position"] == 1].index, 
            data["20_SMA"][data["Position"] == 1], 
            "^", markersize = 15, color = "g", label = 'buy')
    # plot ‘sell’ signals
    plt.plot(data[data["Position"] == -1].index, 
            data["20_SMA"][data["Position"] == -1], 
            "v", markersize = 15, color = "r", label = 'sell')
    plt.ylabel('Price in Rupees', fontsize = 15 )
    plt.xlabel('Date', fontsize = 15 )
    plt.title('Moving_Avg', fontsize = 20)
    plt.legend()
    plt.grid()
    plt.savefig(f"./backend/images/Moving_avg.jpg") 


    closing_prices = data['Close']

    bollinger_up, bollinger_down = get_bollinger_bands(closing_prices)

    plt.title( ' Bollinger Bands')
    plt.xlabel('Days')
    plt.ylabel('Closing Prices')
    plt.plot(closing_prices, label='Closing Prices')
    plt.plot(bollinger_up, label='Bollinger Up', c='g')
    plt.plot(bollinger_down, label='Bollinger Down', c='r')
    plt.legend()
    plt.savefig(f"./backend/images/Bollinger_Bands.jpg") 

    output_var = pd.DataFrame(data["Adj Close"])
#Selecting the Features
    features = ["Open", "High", "Low", "Volume"]

    # scaler = MinMaxScaler()
    # feature_transform = scaler.fit_transform(data[features])
    # feature_transform= pd.DataFrame(columns=features, data=feature_transform, index=data.index)

    # timesplit= TimeSeriesSplit(n_splits=10)
    # for train_index, test_index in timesplit.split(feature_transform):
    #         X_train, X_test = feature_transform[:len(train_index)], feature_transform[len(train_index): (len(train_index)+len(test_index))]
    #         y_train, y_test = output_var[:len(train_index)].values.ravel(), output_var[len(train_index): (len(train_index)+len(test_index))].values.ravel()

    # trainX =np.array(X_train)
    # testX =np.array(X_test)
    # X_train = trainX.reshape(X_train.shape[0], 1, X_train.shape[1])
    # X_test = testX.reshape(X_test.shape[0], 1, X_test.shape[1])
    # lstm = Sequential()
    # lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation="relu", return_sequences=False))
    # lstm.add(Dense(1))
    # lstm.compile(loss="mean_squared_error", optimizer="adam")
    # history=lstm.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1, shuffle=False)

    # y_pred= lstm.predict(X_test)
    # plt.figure(figsize=(10,8))
    # plt.plot(y_test, label="True Value")
    # plt.plot(y_pred, label="LSTM Value")
    # plt.title("Prediction by AI model of Adjusted close")
    # plt.xlabel("Time Scale")
    # plt.ylabel("Scaled USD")
    # plt.legend()
    # plt.savefig(f"./backend/images/LSTM.jpg")

plot_generator('2016-01-01','2019-12-30',asset="as")
print("asd")