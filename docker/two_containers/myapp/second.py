# second.py for the second container
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add_numbers", methods=["POST"])
def add_numbers():
    data = request.get_json()
    print(data)
    a = int(data["a"])
    b = int(data["b"])
    result = a + b
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
