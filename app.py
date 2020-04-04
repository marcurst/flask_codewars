from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route("/", methods=['POST', 'GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)

