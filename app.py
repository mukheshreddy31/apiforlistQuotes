from flask import Flask, jsonify
from flask_cors import CORS  



app = Flask(__name__)
CORS(app)

# Sample data
quotes = [
    {"id": 1, "quote": "The best way to get started is to quit talking and begin doing."},
    {"id": 2, "quote": "Don’t let yesterday take up too much of today."},
    {"id": 3, "quote": "It’s not whether you get knocked down, it’s whether you get up."}
]

# GET all quotes
@app.route("/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)

# GET single quote by id
@app.route("/quotes/<int:qid>", methods=["GET"])
def get_quote(qid):
    for q in quotes:
        if q["id"] == qid:
            return jsonify(q)
    return jsonify({"error": "Quote not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
