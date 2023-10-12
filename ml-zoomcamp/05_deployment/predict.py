import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_C=1.0.bin'              # the file with our model

with open(model_file, 'rb') as f_in:        # load the model and dv
    dv, model = pickle.load(f_in)

app = Flask('churn')                        # the name of our app

@app.route('/predict', methods=['POST'])    # to send the customer information, we need to POST it
def predict():
    customer = request.get_json()           # web services works better with json         

    X = dv.transform([customer])            # one-hot encoding
    y_pred = model.predict_proba(X)[0, 1]   
    churn = y_pred >= 0.5                   # send the data with threshold defined 

    result = {
        'churn_probability': float(y_pred), # convert numnpy data into python data to use in flask
        'churn': bool(churn)                # convert the churn to bool
    }

    return jsonify(result)                  # send back the data in jason format to the user


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)