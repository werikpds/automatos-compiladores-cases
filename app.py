from flask import Flask, jsonify, request
from afd import afd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello", 200

@app.route('/doce', methods=['POST'])
def doce():
    data = request.get_json()
    print(data["dinheiro"])
    return afd(data["dinheiro"]) , 200

if __name__ == '__main__':
    app.run(debug=True)