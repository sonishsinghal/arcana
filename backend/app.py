from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

import json
import os


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def hello_world():
    return "<h1>hello</h1>"


@app.route("/optimizer", methods=['POST'])
def optimizer():
    return "optimizer"


if __name__ == "__main__":
    app.run(debug=True)
