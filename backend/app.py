from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS, cross_origin
import base64
import json
import os
from onestock import plot_generator
from information import information
from constraints_on_return_and_risk_measures import constraints_on_return_and_risk_measures
from mean_risk_portfolio_optimization_using_black_litterman_model import mean_risk_portfolio_optimization
from portfolio_optimisation import portfolio_optimisation
from portfolio_optimisation_2_ulcer import portfolio_optimisation_2_ulcer
from portfolio_optimization_with_risk_factors_using_stepwise_regression import portfolio_optimisation_with_risk_factors
from risk_parity_portfolio_optimization import risk_parity_portfolio_optimization
from sentiment_analysis import sentiment_analysis

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def hello_world():
    return "<h1>hello</h1>"


@app.route('/image', methods=['POST'])
@cross_origin()
def getImage():
    data = json.loads(request.data)
    print(data["company"])
    print(data["start"])

    print(data["end"])

    word, summ = sentiment_analysis(data["company"])
    plot_generator(data["start"], data["end"], data["company"])
    with open("./images/Open_Price.jpg", "rb") as img_file:
        b64_string1 = base64.b64encode(img_file.read())
    with open("./images/Close_Price.jpg", "rb") as img_file:
        b64_string2 = base64.b64encode(img_file.read())
    with open("./images/High_Price.jpg", "rb") as img_file:
        b64_string3 = base64.b64encode(img_file.read())
    with open("./images/Low_Price.jpg", "rb") as img_file:
        b64_string4 = base64.b64encode(img_file.read())
    with open("./images/Relative_Strength_Index.jpg", "rb") as img_file:
        b64_string5 = base64.b64encode(img_file.read())
    with open("./images/Moving_avg.jpg", "rb") as img_file:
        b64_string6 = base64.b64encode(img_file.read())
    with open("./images/Bollinger_Bands.jpg", "rb") as img_file:
        b64_string7 = base64.b64encode(img_file.read())
    with open("./images/LSTM.jpg", "rb") as img_file:
        b64_string8 = base64.b64encode(img_file.read())

    name, industry, sector, summary = information(data["company"])
    data = jsonify(
        name=name,
        industry=industry,
        sector=sector,
        summary=summary,
        word=word,
        summ=summ,
        plot1=str(b64_string1, 'UTF-8'),
        plot2=str(b64_string2, 'UTF-8'),
        plot3=str(b64_string3, 'UTF-8'),
        plot4=str(b64_string4, 'UTF-8'),

        plot5=str(b64_string5, 'UTF-8'),
        plot6=str(b64_string6, 'UTF-8'),
        plot7=str(b64_string7, 'UTF-8'),
        plot8=str(b64_string8, 'UTF-8'),
    )
    return data


@app.route("/optimizer", methods=['POST'])
@cross_origin()
def optimizer():
    data = json.loads(request.data)
    print(data["assets"])
    # constraints_on_return_and_risk_measures(
    #     data["start"], data["end"])

    val = data["goal"]
    print(val)
    b64_string1 = ""
    b64_string2 = ""
    b64_string3 = ""
    b64_string4 = ""
    b64_string5 = ""
    b64_string6 = ""
    b64_string7 = ""
    b64_string8 = ""
    if val == "1":
        # portfolio_optimisation(data["start"], data["end"])
        with open("./images1/plot1.jpg", "rb") as img_file:
            b64_string1 = base64.b64encode(img_file.read())
        with open("./images1/plot2.jpg", "rb") as img_file:
            b64_string2 = base64.b64encode(img_file.read())
        with open("./images1/plot3.jpg", "rb") as img_file:
            b64_string3 = base64.b64encode(img_file.read())
        with open("./images1/plot4.jpg", "rb") as img_file:
            b64_string4 = base64.b64encode(img_file.read())
        with open("./images1/plot5.jpg", "rb") as img_file:
            b64_string5 = base64.b64encode(img_file.read())
        with open("./images1/plot6.jpg", "rb") as img_file:
            b64_string6 = base64.b64encode(img_file.read())

    elif val == "2":
        # mean_risk_portfolio_optimization(
        #     data["start"], data["end"])
        with open("./images2/plot1.jpg", "rb") as img_file:
            b64_string1 = base64.b64encode(img_file.read())
        with open("./images2/plot2.jpg", "rb") as img_file:
            b64_string2 = base64.b64encode(img_file.read())
        with open("./images2/plot3.jpg", "rb") as img_file:
            b64_string3 = base64.b64encode(img_file.read())
        with open("./images2/plot4.jpg", "rb") as img_file:
            b64_string4 = base64.b64encode(img_file.read())
        with open("./images2/plot5.jpg", "rb") as img_file:
            b64_string5 = base64.b64encode(img_file.read())

    elif val == "3":
        # portfolio_optimisation_2_ulcer(data["start"], data["end"])
        with open("./images3/plot1.jpg", "rb") as img_file:
            b64_string1 = base64.b64encode(img_file.read())
        with open("./images3/plot2.jpg", "rb") as img_file:
            b64_string2 = base64.b64encode(img_file.read())
        with open("./images3/plot3.jpg", "rb") as img_file:
            b64_string3 = base64.b64encode(img_file.read())
        with open("./images3/plot4.jpg", "rb") as img_file:
            b64_string4 = base64.b64encode(img_file.read())
        with open("./images3/plot5.jpg", "rb") as img_file:
            b64_string5 = base64.b64encode(img_file.read())

    elif val == "4":
        # portfolio_optimisation_with_risk_factors(
        #     data["start"], data["end"])
        with open("./images4/plot1.jpg", "rb") as img_file:
            b64_string1 = base64.b64encode(img_file.read())
        with open("./images4/plot2.jpg", "rb") as img_file:
            b64_string2 = base64.b64encode(img_file.read())
        with open("./images4/plot3.jpg", "rb") as img_file:
            b64_string3 = base64.b64encode(img_file.read())

    elif val == "5":
        # risk_parity_portfolio_optimization(
        #     data["start"], data["end"])
        with open("./images5/plot1.jpg", "rb") as img_file:
            b64_string1 = base64.b64encode(img_file.read())
        with open("./images5/plot2.jpg", "rb") as img_file:
            b64_string2 = base64.b64encode(img_file.read())
        with open("./images5/plot3.jpg", "rb") as img_file:
            b64_string3 = base64.b64encode(img_file.read())

    elif val == "6":
        # constraints_on_return_and_risk_measures(
        #     data["start"], data["end"])
        with open("./images6/plot1.jpg", "rb") as img_file:
            b64_string1 = base64.b64encode(img_file.read())
        with open("./images6/plot2.jpg", "rb") as img_file:
            b64_string2 = base64.b64encode(img_file.read())
        with open("./images6/plot3.jpg", "rb") as img_file:
            b64_string3 = base64.b64encode(img_file.read())
        with open("./images6/plot4.jpg", "rb") as img_file:
            b64_string4 = base64.b64encode(img_file.read())
        with open("./images6/plot5.jpg", "rb") as img_file:
            b64_string5 = base64.b64encode(img_file.read())
        with open("./images6/plot6.jpg", "rb") as img_file:
            b64_string6 = base64.b64encode(img_file.read())
        with open("./images6/plot7.jpg", "rb") as img_file:
            b64_string7 = base64.b64encode(img_file.read())
        with open("./images6/plot8.jpg", "rb") as img_file:
            b64_string8 = base64.b64encode(img_file.read())

    if (b64_string1 != ""):
        b64_string1 = b64_string1.decode('utf-8')
    if (b64_string2 != ""):
        b64_string2 = b64_string2.decode('utf-8')
    if (b64_string3 != ""):
        b64_string3 = b64_string3.decode('utf-8')
    if (b64_string4 != ""):
        b64_string4 = b64_string4.decode('utf-8')
    if (b64_string5 != ""):
        b64_string5 = b64_string5.decode('utf-8')
    if (b64_string6 != ""):
        b64_string6 = b64_string6.decode('utf-8')
    if (b64_string7 != ""):
        b64_string7 = b64_string7.decode('utf-8')
    if (b64_string8 != ""):
        b64_string8 = b64_string8.decode('utf-8')
    res = jsonify(
        plot1=b64_string1,
        plot2=b64_string2,
        plot3=b64_string3,
        plot4=b64_string4,
        plot5=b64_string5,
        plot6=b64_string6,
        plot7=b64_string7,
        plot8=b64_string8
    )
    return res


if __name__ == "__main__":
    app.run(debug=True)
