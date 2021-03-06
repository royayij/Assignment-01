from flask import Flask
import os
import requests
import pandas as pd
from resources import figure_maker

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/vizualization-cp/acc-fig', methods=['POST'])
def figure_acc():
    # db_api = os.environ['PREDICTIONDB_API']
    # # Make a GET request to training db service to retrieve the training data/features.
    # r = requests.get(db_api)
    # j = r.json()
    # df = pd.DataFrame.from_dict(j)
    resp = figure_maker.acc_fig()
    return resp


@app.route('/vizualization-cp/result-fig', methods=['POST'])
def figure_result():
    db_api = os.environ['PREDICT_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    resp = figure_maker.result_fig(df)
    return resp


app.run(host='0.0.0.0', port=5000)
