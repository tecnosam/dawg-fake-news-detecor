import numpy as np
import pandas as pd
import joblib as jb
from flask import *
from flask_cors import CORS

app = Flask(__name__)

app.config['X-api-key'] = "1019c2f0-9790-11ea-8aa8-733f376acd5f"

CORS(app)

model = jb.load("svc.model")
td = jb.load("td.model")
cv = jb.load("cv.model")

@app.route("/predict", methods = ['POST'])
def predict():
    headers = request.headers
    if ( 'X-RapidAPI-Proxy-Secret' not in headers ):
        abort(501)
    if ( headers['X-RapidAPI-Proxy-Secret'] != "1019c2f0-9790-11ea-8aa8-733f376acd5f" ):
        abort(501)
    if ('text' not in request.form):
        abort(400)
    text = request.form['text']
    X = td.transform( cv.transform( [text] ) )
    res = model.predict( X )
    if (res[0] == 'True'):
        return jsonify({'prediction': True})
    return jsonify({'prediction': False})

@app.route("/score", methods = ['POST'])
def score():

    text = request.form['text']
    real = request.form['real']
    X = td.transform( cv.transform( [text] ) )
    res = model.score(X, real)
    return jsonify({
        'score': res
    })

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)