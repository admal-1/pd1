from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return ("Witaj w moim API!")
    
@app.route("/mojastrona")
def mojastrona():
    return ("To jest moja strona!")

@app.route("/hello")
def hello():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    return "Hello!"
    
@app.route("/api/v1.0/predict")
def predict():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    if num1+num2>5.8:
        return "1"
    return "0"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
