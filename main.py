# WEB-API

#!/usr/bin/env  python2.7

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', mthods={"GET"})
def hello_world():
  result = {"msg":"pong"}
  return jsonify(result)
  
if __name__ == '__main__':
    app.run(debug=True)

    
