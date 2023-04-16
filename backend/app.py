from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS, cross_origin
import base64
import json
import os
from onestock import plot_generator
from information import information
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


@ app.route("/optimizer", methods=['POST'])
def optimizer():
    return "optimizer"


if __name__ == "__main__":
    app.run(debug=True)
