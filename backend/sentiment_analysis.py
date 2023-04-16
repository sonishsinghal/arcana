import pandas as pd


def sentiment_analysis(name):

    df = pd.read_csv("./final1.csv")
    df = df[df["symbol"] == name].sort_values(by='date', ascending=False)

    if df["Sentiment"].iloc[0] == 1:
        word = f"It is safe to invest in the company based on it's analysis from the information available from recent quarter"
    else:
        word = f"It is highly risky invest in the company based on it's analysis from the information available from recent quarter.\nHere are some of the risk factors that we obtained from the meeting for the latest quarter"

    summary = df["Summary"].iloc[0]
    return str(word+df["Negative summary"].iloc[0]), summary
