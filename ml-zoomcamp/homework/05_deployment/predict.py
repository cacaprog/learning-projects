import pickle


def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)
    

dv = load('dv.bin')
model = load('model1.bin')

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print('prediction: %.3f' % y_pred)
