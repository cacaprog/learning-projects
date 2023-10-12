from flask import Flask

app = Flask('churn-app') # web service name

@app.route('/ping',methods=['GET'])
def ping():
    return 'PONG'

if __name__=='__main__':
   app.run(debug=True, host='0.0.0.0', port=9696) # run the code in local machine with the debugging mode true and port 9696