import pickle

from flask import Flask
from flask import request
from flask import jsonify


def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)
    

dv = load('dv.bin')
model = load('model1.bin')


app = Flask('credit-score')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'credit_probability': float(y_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)