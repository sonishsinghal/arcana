from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS, cross_origin
import base64
import json
import os
from onestock import plot_generator

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
    plot_generator(data["start"],data["end"],data["company"])
    with open("./images/image.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    data = jsonify(plot1=str(b64_string, 'UTF-8'),
                   plot2=str(b64_string, 'UTF-8'),
                   plot3=str(b64_string, 'UTF-8'),
                   plot4=str(b64_string, 'UTF-8'),

                   plot5=str(b64_string, 'UTF-8'),
                   plot6=str(b64_string, 'UTF-8'),
                   plot7=str(b64_string, 'UTF-8'),
                   plot8=str(b64_string, 'UTF-8'),
                   plot9=str(b64_string, 'UTF-8'),
                   )
    return data


@ app.route("/optimizer", methods=['POST'])
def optimizer():
    return "optimizer"


if __name__ == "__main__":
    app.run(debug=True)
