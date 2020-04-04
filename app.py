from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Codewars API"

@app.route("/multiply/", methods=['POST'])
def multiply():
    data = request.get_json()
    res = str(data['a'] * data['b'])
    return res, 200

if __name__ == "__main__":
    app.run(debug=True)
