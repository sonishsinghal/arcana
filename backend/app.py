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

    with open("./img/images6/plot1.jpg", "rb") as img_file:
        b64_string1 = base64.b64encode(img_file.read())
    with open("./img/images6/plot2.jpg", "rb") as img_file:
        b64_string2 = base64.b64encode(img_file.read())
    with open("./img/images6/plot3.jpg", "rb") as img_file:
        b64_string3 = base64.b64encode(img_file.read())
    with open("./img/images6/plot4.jpg", "rb") as img_file:
        b64_string4 = base64.b64encode(img_file.read())
    with open("./img/images6/plot5.jpg", "rb") as img_file:
        b64_string5 = base64.b64encode(img_file.read())
    with open("./img/images6/plot6.jpg", "rb") as img_file:
        b64_string6 = base64.b64encode(img_file.read())
    with open("./img/images6/plot7.jpg", "rb") as img_file:
        b64_string7 = base64.b64encode(img_file.read())
    with open("./img/images6/plot8.jpg", "rb") as img_file:
        b64_string8 = base64.b64encode(img_file.read())
    res = jsonify(
        plot1=str(b64_string1, 'UTF-8'),
        plot2=str(b64_string2, 'UTF-8'),
        plot3=str(b64_string3, 'UTF-8'),
        plot4=str(b64_string4, 'UTF-8'),

        plot5=str(b64_string5, 'UTF-8'),
        plot6=str(b64_string6, 'UTF-8'),
        plot7=str(b64_string7, 'UTF-8'),
        plot8=str(b64_string8, 'UTF-8'),
    )
    return res


if __name__ == "__main__":
    app.run(debug=True)
