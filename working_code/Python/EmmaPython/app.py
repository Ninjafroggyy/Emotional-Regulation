from flask import Flask, jsonify, request
from USERRUN import RegulationBreak

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Regulation Break"

@app.route('/zonechoice')
def print():
    return jsonify(RegulationBreak.self.)

if __name__ =='__main__':
    app.run(debug = True, port = 3001)